from django.db import models


class Category(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Note = models.CharField(max_length=500, null=True)


class Brand(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Note = models.CharField(max_length=500, null=True)


class Unit(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Note = models.CharField(max_length=500, null=True)


class Cost(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Note = models.CharField(max_length=500, null=True)


class Product(models.Model):
    SKU = models.CharField(max_length=100, unique=True)
    Category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    Brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    Unit = models.ForeignKey('Unit', on_delete=models.SET_NULL, null=True)
    Name = models.CharField(max_length=100, unique=True)
    Mfg = models.DateField(null=True)
    Exp = models.DateField(null=True)
    Details = models.TextField()


class Supplier(models.Model):
    Company = models.CharField(max_length=100, unique=True)
    Owner = models.CharField(max_length=100, unique=True, null=True)
    Number = models.IntegerField(unique=True, null=True)
    Email = models.CharField(max_length=100, unique=True, null=True)
    Address = models.CharField(max_length=100, unique=True, null=True)
    Note = models.CharField(max_length=500, null=True)


class Purchase(models.Model):
    Supplier = models.ForeignKey(
        'Supplier', on_delete=models.SET_NULL, null=True)
    SalesMan = models.CharField(max_length=100, null=True)
    Number = models.IntegerField(unique=True, null=True)
    Receiver = models.CharField(max_length=100, null=True)
    Date = models.DateTimeField(auto_now=True)
    PaymentStatus = models.CharField(max_length=100)


class PurchaseItem(models.Model):
    Purchase = models.ForeignKey(
        'Purchase', on_delete=models.SET_NULL, null=True)
    Product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True)
    SalesMan = models.CharField(max_length=100, null=True)
    PurchasePrice = models.FloatField()
    SalePrice = models.FloatField()
    Quantity = models.IntegerField()


class PurchaseCost(models.Model):
    Purchase = models.ForeignKey(
        'Purchase', on_delete=models.SET_NULL, null=True)
    Cost = models.ForeignKey(
        'Cost', on_delete=models.SET_NULL, null=True)
    Amount = models.FloatField()


class PurchasePayment(models.Model):
    Purchase = models.ForeignKey(
        'Purchase', on_delete=models.SET_NULL, null=True)
    Amount = models.FloatField()
    Date = models.DateTimeField(auto_now=True)
