from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Email = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=20)
    Role = models.CharField(max_length=20)
    Outlet = models.ForeignKey(
        'Outlet', on_delete=models.CASCADE)


class Outlet(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Address = models.CharField(max_length=100, unique=True)
    Number = models.BigIntegerField(unique=True, null=True)
    Email = models.CharField(max_length=100, unique=True, null=True)
    Note = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ['-id']


class Category(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Note = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ['-id']


class Brand(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Note = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ['-id']


class Unit(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Note = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ['-id']


class Cost(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Note = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ['-id']


class Supplier(models.Model):
    Company = models.CharField(max_length=100, unique=True)
    Owner = models.CharField(max_length=100, unique=True, null=True)
    Number = models.BigIntegerField(unique=True, null=True)
    Email = models.CharField(max_length=100, unique=True, null=True)
    Address = models.CharField(max_length=100, null=True)
    Note = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ['-id']


class Customer(models.Model):
    Name = models.CharField(max_length=100)
    Number = models.BigIntegerField(unique=True)
    Email = models.CharField(max_length=100, unique=True, null=True)
    Address = models.CharField(max_length=100, null=True)
    Note = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ['-id']


class Product(models.Model):
    SKU = models.CharField(max_length=100, unique=True, editable=False)
    Category = models.ForeignKey(
        'Category', on_delete=models.CASCADE)
    Brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    Unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, unique=True)
    Mfg = models.DateField(null=True)
    Exp = models.DateField(null=True)
    Details = models.TextField(null=True)

    class Meta:
        ordering = ['-id']


class Purchase(models.Model):
    InvoiceNumber = models.CharField(
        max_length=100, unique=True, editable=False)
    Outlet = models.ForeignKey(
        'Outlet', on_delete=models.CASCADE)
    Supplier = models.ForeignKey(
        'Supplier', on_delete=models.CASCADE)
    Discount = models.FloatField(null=True)
    Date = models.DateTimeField()

    class Meta:
        ordering = ['-id']


class PurchaseItem(models.Model):
    Purchase = models.ForeignKey(
        'Purchase', on_delete=models.CASCADE)
    Product = models.ForeignKey(
        'Product', on_delete=models.CASCADE)
    PurchasePrice = models.FloatField()
    SalePrice = models.FloatField()
    Quantity = models.IntegerField()

    class Meta:
        ordering = ['-id']


class PurchaseCost(models.Model):
    Purchase = models.ForeignKey(
        'Purchase', on_delete=models.CASCADE)
    Cost = models.ForeignKey(
        'Cost', on_delete=models.CASCADE)
    Amount = models.FloatField()

    class Meta:
        ordering = ['-id']


class PurchasePayment(models.Model):
    Purchase = models.ForeignKey(
        'Purchase', on_delete=models.CASCADE)
    Amount = models.FloatField()
    Date = models.DateTimeField()

    class Meta:
        ordering = ['-id']


class Sale(models.Model):
    InvoiceNumber = models.CharField(
        max_length=100, unique=True, editable=False)
    Outlet = models.ForeignKey(
        'Outlet', on_delete=models.CASCADE)
    Customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE)
    Discount = models.FloatField(null=True)
    Date = models.DateTimeField()

    class Meta:
        ordering = ['-id']


class SaleItem(models.Model):
    Sale = models.ForeignKey(
        'Sale', on_delete=models.CASCADE)
    Product = models.ForeignKey(
        'Product', on_delete=models.CASCADE)
    Price = models.FloatField()
    Quantity = models.IntegerField()

    class Meta:
        ordering = ['-id']


class SalePayment(models.Model):
    Sale = models.ForeignKey(
        'Sale', on_delete=models.CASCADE)
    Amount = models.FloatField()
    Date = models.DateTimeField()

    class Meta:
        ordering = ['-id']
