from rest_framework import serializers
from .models import *


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class MyUserRelationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        depth = 1


class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    # Category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        exists = Product.objects.exists()
        id = 0

        if exists is True:
            latest = Product.objects.latest('id')
            id = latest.id + 1

        txt = "P{}-C{}B{}"
        validated_data['SKU'] = txt.format(
            id, validated_data['Category'].id, validated_data['Brand'].id)

        return Product.objects.create(**validated_data)


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class PurchaseListSerializer(serializers.ModelSerializer):
    # Category = CategorySerializer()

    class Meta:
        model = Purchase
        fields = '__all__'
        depth = 1


class PurchaseSerializer(serializers.ModelSerializer):
    #  InvoiceNumber = serializers.CharField(read_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'

    def create(self, validated_data):
        exists = Purchase.objects.exists()
        id = 0

        if exists is True:
            latest = Purchase.objects.latest('id')
            id = latest.id + 1

        txt = "PI{}-O{}S{}"
        validated_data['InvoiceNumber'] = txt.format(
            id, validated_data['Outlet'].id, validated_data['Supplier'].id)

        return Purchase.objects.create(**validated_data)


class PurchaseItemListSerializer(serializers.ModelSerializer):
    # Category = CategorySerializer()

    class Meta:
        model = PurchaseItem
        fields = '__all__'
        depth = 1


class PurchaseItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseItem
        fields = '__all__'


class PurchasePaymentListSerializer(serializers.ModelSerializer):
    # Category = CategorySerializer()

    class Meta:
        model = PurchasePayment
        fields = '__all__'
        depth = 1


class PurchasePaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchasePayment
        fields = '__all__'


class CostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cost
        fields = '__all__'


class PurchaseCostListSerializer(serializers.ModelSerializer):
    # Category = CategorySerializer()

    class Meta:
        model = PurchaseCost
        fields = '__all__'
        depth = 1


class PurchaseCostSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseCost
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SaleListSerializer(serializers.ModelSerializer):
    # Category = CategorySerializer()

    class Meta:
        model = Sale
        fields = '__all__'
        depth = 1


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = '__all__'

    def create(self, validated_data):
        exists = Sale.objects.exists()
        id = 0

        if exists is True:
            latest = Sale.objects.latest('id')
            id = latest.id + 1

        txt = "SI{}-O{}C{}"
        validated_data['InvoiceNumber'] = txt.format(
            id, validated_data['Outlet'].id, validated_data['Customer'].id)

        return Sale.objects.create(**validated_data)


class SaleItemListSerializer(serializers.ModelSerializer):
    # Category = CategorySerializer()

    class Meta:
        model = SaleItem
        fields = '__all__'
        depth = 1


class SaleItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleItem
        fields = '__all__'


class SalePaymentListSerializer(serializers.ModelSerializer):
    # Category = CategorySerializer()

    class Meta:
        model = SalePayment
        fields = '__all__'
        depth = 1


class SalePaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalePayment
        fields = '__all__'
