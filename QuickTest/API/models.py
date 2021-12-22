from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class CustomUser(models.Model):
#     username = models.CharField(max_length=100, blank=False, unique=True)
#     first_name = models.CharField(max_length=100, blank=False)
#     last_name = models.CharField(max_length=100, blank=False)
#     password = models.CharField(max_length=100, blank=False)
#     email = models.EmailField(max_length=100, blank=False, unique=True)
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return f"{self.email} - {self.first_name} {self.last_name}"

class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']


class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"

    def natural_key(self):
        return ({"id": self.id, "document": self.document, "first_name": self.first_name, "last_name": self.last_name, "email": self.email})
    objects = models.Manager()


class Bills(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=False)
    nit = models.IntegerField(unique=True)
    code = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.id} - {self.company_name} {self.nit}"

    class Meta:
        ordering = ["id"]

    def natural_key(self):
        return ({"id": self.id, "company_name": self.company_name, "nit": self.nit, "code": self.code, "client_id": self.client_id.natural_key()})
    natural_key.dependencies = ['API.Clients']
    objects = models.Manager()


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    attribute = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.id} - {self.name} {self.description}"
    objects = models.Manager()

    def natural_key(self):
        return ({"id": self.id, "name": self.name, "description": self.description})


class Bills_Products(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.bill_id} {self.product_id}"

    class Meta:
        ordering = ["id"]

    def natural_key(self):
        return ({"id": self.id, "bill_id": self.bill_id, "product_id": self.product_id})
    objects = models.Manager()
