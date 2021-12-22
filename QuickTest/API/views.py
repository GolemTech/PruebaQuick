from django import db
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
import json
from .models import Clients, Bills, Products, Bills_Products, CustomUser
from django.core.serializers import serialize
from django.conf import settings
from django.contrib.auth.hashers import make_password

import sqlite3
import pandas as pd


db_path = settings.DATABASES['default']['NAME']


class CRUDUser(View):

    def get(self, request, pk=None):
        if pk == None:
            queryset = CustomUser.objects.all().order_by("id")
        else:
            queryset = CustomUser.objects.filter(id=pk)
        name = queryset.model.__name__
        user = json.loads(serialize("json", queryset))
        dataJSON = {name: user}
        return JsonResponse(dataJSON, safe=True, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        data['password'] = make_password(data['password'])
        user, created = CustomUser.objects.get_or_create(**data)
        if created:
            message = "User created successfully."
            data = {"message": message, "user_id": user.id}
            return JsonResponse(data=data, safe=True, status=status.HTTP_201_CREATED)
        else:
            message = "User already existing."
            data = {"message": message, "user_id": user.id}
            return JsonResponse(data=data, safe=True, status=status.HTTP_200_OK)


class CRUDClients(View):

    def get(self, request, pk=None):
        if pk == None:
            queryset = Clients.objects.all().order_by("id")
        else:
            queryset = Clients.objects.filter(id=pk)
        name = queryset.model.__name__
        client = json.loads(serialize("json", queryset))
        dataJSON = {name: client}
        return JsonResponse(dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        client, created = Clients.objects.get_or_create(**data)
        message = "Client created successfully."
        data = {"message": message, "client_id": client.id}
        return JsonResponse(data=data, safe=True, status=200)

    def put(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        data_dict = data["fields"]
        Clients.objects.filter(id=pk).update(**data_dict)

        client_data = Clients.objects.filter(id=pk)
        client = json.loads(serialize("json", client_data))

        message = "Client Updated successfully."
        data = {"message": message, client_data.model.__name__: client}
        return JsonResponse(data=data, safe=True, status=200)

    def delete(self, request, pk=None):
        queryset = Clients.objects.filter(id=pk)
        name = queryset.model.__name__
        client = json.loads(serialize("json", queryset))

        Clients.objects.filter(id=pk).delete()

        message = "Client deleted succesfully."
        data = {"message": message, name: client}
        return JsonResponse(data=data, safe=True, status=200)


class CRUDBills(View):

    def get(self, request, pk=None):
        if pk == None:
            queryset = Bills.objects.all().order_by("id").select_related()
        else:
            print("sadasd")
            queryset = Bills.objects.filter(id=pk).select_related()
        name = queryset.model.__name__
        bill = json.loads(serialize("json", queryset,
                          use_natural_foreign_keys=True))
        dataJSON = {name: bill}
        return JsonResponse(dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        pk = data["client_id"]
        data["client_id"] = Clients.objects.get(id=pk)
        bill, created = Bills.objects.get_or_create(**data)
        message = "Bill created successfully."
        data = {"message": message, "Bill_id": bill.id}
        return JsonResponse(data=data, safe=True, status=200)

    def put(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        data_dict = data["fields"]
        Bills.objects.filter(id=pk).update(**data_dict)

        bill_data = Bills.objects.filter(id=pk)
        bill = json.loads(serialize("json", bill_data))

        message = "Bills Updated successfully."
        data = {"message": message, bill_data.model.__name__: bill}
        return JsonResponse(data=data, safe=True, status=200)

    def delete(self, request, pk=None):
        queryset = Bills.objects.filter(id=pk)
        name = queryset.model.__name__
        bill = json.loads(serialize("json", queryset))

        Bills.objects.filter(id=pk).delete()

        message = "Bills deleted succesfully."
        data = {"message": message, name: bill}
        return JsonResponse(data=data, safe=True, status=200)


class CRUDProducts(View):

    def get(self, request, pk=None):
        if pk == None:
            queryset = Products.objects.all().order_by("id")
        else:
            queryset = Products.objects.filter(id=pk)
        name = queryset.model.__name__
        product = json.loads(serialize("json", queryset))
        dataJSON = {name: product}
        return JsonResponse(dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        product, created = Products.objects.get_or_create(**data)
        message = "Products created successfully."
        data = {"message": message, "Product_id": product.id}
        return JsonResponse(data=data, safe=True, status=200)

    def put(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        data_dict = data["fields"]
        Products.objects.filter(id=pk).update(**data_dict)

        products_data = Products.objects.filter(id=pk)
        product = json.loads(serialize("json", products_data))

        message = "Products Updated successfully."
        data = {"message": message, products_data.model.__name__: product}
        return JsonResponse(data=data, safe=True, status=200)

    def delete(self, request, pk=None):
        queryset = Products.objects.filter(id=pk)
        name = queryset.model.__name__
        bill = json.loads(serialize("json", queryset))

        Products.objects.filter(id=pk).delete()

        message = "Products deleted succesfully."
        data = {"message": message, name: bill}
        return JsonResponse(data=data, safe=True, status=200)


class BillsProducts(View):
    def get(self, request, pk=None):
        if pk == None:
            queryset = Bills_Products.objects.all().order_by("id").select_related()
        else:
            queryset = Bills_Products.objects.filter(id=pk).select_related()

        name = queryset.model.__name__
        bill_product = json.loads(
            serialize("json", queryset, use_natural_foreign_keys=True))
        dataJSON = {name: bill_product}
        return JsonResponse(dataJSON, safe=True, status=200)

    def post(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        data["bill_id"] = Bills.objects.get(id=data["bill_id"])
        data["product_id"] = Products.objects.get(id=data["product_id"])
        bill_product, created = Bills_Products.objects.get_or_create(**data)
        message = "Bill Products created successfully."
        data = {"message": message, "Bill_Product_id": bill_product.id}
        return JsonResponse(data=data, safe=True, status=200)


@csrf_exempt
def exportCSV(request):
    """
    Endpoint que permite realizar la descarga de un archivo CSV
    con la lista de registros de Clientes: mostrando documento,
    nombre completo y la cantidad facturas relacionadas."""
    if request.method == 'GET':
        conn = sqlite3.connect(str(db_path))
        query_clients = conn.execute("SELECT * from API_clients")

        data = []
        for row in query_clients:
            query_bills = conn.execute(
                "select * from API_bills where client_id_id = ?", (row[0],))
            query_bills = query_bills.fetchall()
            data.append({
                "document": row[1],
                "full_name": f'{row[2]} {row[3]}',
                "bills": len(query_bills),
            })
        csv_object = pd.DataFrame.from_dict(data)

        file = csv_object.to_csv(index=None)
        response = HttpResponse(file, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=QuickTest.csv'
        return response


@csrf_exempt
def importCSV(request):
    if request.method == 'POST':
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        registries = "INSERT INTO API_clients (document, first_name, last_name, email) VALUES(?, ?, ?, ?)"
        csv_file = request.FILES["csv_file"]
        file_data = csv_file.read().decode("utf-8")

        file_data = [data.split(",") for data in file_data.split("\r\n")]
        del file_data[0]
        try:
            data_to_import = [(row[0], row[1], row[2], row[3])
                              for row in file_data]
            cursor.executemany(registries, data_to_import)
            conn.commit()
        except:
            return JsonResponse({"message": "error al importar archivo"}, status=400)
        return JsonResponse({"data": file_data}, safe=True, status=200)
