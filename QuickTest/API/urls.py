from os import name
from .views import CRUDUser, CRUDClients, CRUDBills, CRUDProducts, BillsProducts, exportCSV, importCSV
from rest_framework.authtoken import views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.urls import path, include


urlpatterns = [
    path('api/client/new/', csrf_exempt(CRUDClients.as_view())),
    path('api/client/<int:pk>/', csrf_exempt(CRUDClients.as_view())),
    path('api/client/all/', csrf_exempt(CRUDClients.as_view())),

    path('api/bill/new/', csrf_exempt(CRUDBills.as_view())),
    path('api/bill/<int:pk>/', csrf_exempt(CRUDBills.as_view())),
    path('api/bill/all/', csrf_exempt(CRUDBills.as_view())),

    path('api/products/new/', csrf_exempt(CRUDProducts.as_view())),
    path('api/products/<int:pk>/', csrf_exempt(CRUDProducts.as_view())),
    path('api/products/all/', csrf_exempt(CRUDProducts.as_view())),

    path('api/bill_products/new/', csrf_exempt(BillsProducts.as_view())),
    path('api/bill_products/<int:pk>/', csrf_exempt(BillsProducts.as_view())),
    path('api/bill_products/all/', csrf_exempt(BillsProducts.as_view())),

    path('api/user/new/', csrf_exempt(CRUDUser.as_view())),
    path('api/user/all/', csrf_exempt(CRUDUser.as_view())),

    path('api/export/all/', exportCSV, name='export_csv'),
    path('api/import/', importCSV, name='import_csv'),

    path('api-token-auth/', views.obtain_auth_token)

]
