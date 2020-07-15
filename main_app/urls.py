from django.urls import path, include
from main_app.controller import myuser, manager, stuff, home, outlet, category, brand, unit, product, supplier, purchase, purchaseItems, purchasePayment, cost, purchaseCost, customer, sale, saleItems, salePayment

urlpatterns = [
    path('user/login/', myuser.login),
    path('user/update/<id>/', myuser.update),

    path('home/purchase/', home.purchase),
    path('home/sale/', home.sale),

    path('manager/create/', manager.create, name='managerCreate'),
    path('manager/', manager.list),
    path('manager/<id>/', manager.single),
    path('manager/edit/<id>/', manager.edit),
    path('manager/delete/<id>/', manager.delete),

    path('stuff/create/', stuff.create, name='stuffCreate'),
    path('stuff/', stuff.list),
    path('stuff/<id>/', stuff.single),
    path('stuff/edit/<id>/', stuff.edit),
    path('stuff/delete/<id>/', stuff.delete),

    path('outlet/create/', outlet.create, name='outletCreate'),
    path('outlet/', outlet.list),
    path('outlet/<id>/', outlet.single),
    path('outlet/edit/<id>/', outlet.edit),
    path('outlet/delete/<id>/', outlet.delete),

    path('category/create/', category.create, name='categoryCreate'),
    path('category/', category.list),
    path('category/<id>/', category.single),
    path('category/edit/<id>/', category.edit),
    path('category/delete/<id>/', category.delete),

    path('brand/create/', brand.create, name='brandCreate'),
    path('brand/', brand.list),
    path('brand/<id>/', brand.single),
    path('brand/edit/<id>/', brand.edit),
    path('brand/delete/<id>/', brand.delete),

    path('unit/create/', unit.create, name='unitCreate'),
    path('unit/', unit.list),
    path('unit/<id>/', unit.single),
    path('unit/edit/<id>/', unit.edit),
    path('unit/delete/<id>/', unit.delete),

    path('product/create/', product.create, name='productCreate'),
    path('product/', product.list),
    path('product/<id>/', product.single),
    path('product/edit/<id>/', product.edit),
    path('product/delete/<id>/', product.delete),

    path('supplier/create/', supplier.create, name='supplierCreate'),
    path('supplier/', supplier.list),
    path('supplier/<id>/', supplier.single),
    path('supplier/edit/<id>/', supplier.edit),
    path('supplier/delete/<id>/', supplier.delete),

    path('purchase/create/', purchase.create, name='purchaseCreate'),
    path('purchase/', purchase.list),
    path('purchase/<id>/', purchase.single),
    path('purchase/edit/<id>/', purchase.edit),
    path('purchase/delete/<id>/', purchase.delete),

    path('purchaseItems/create/', purchaseItems.create,
         name='purchaseItemsCreate'),
    path('purchaseItems/', purchaseItems.list),
    path('purchaseItems/<id>/', purchaseItems.single),
    path('purchaseItems/edit/<id>/', purchaseItems.edit),
    path('purchaseItems/delete/<id>/', purchaseItems.delete),

    path('purchasePayment/create/', purchasePayment.create,
         name='purchasePaymentCreate'),
    path('purchasePayment/', purchasePayment.list),
    path('purchasePayment/<id>/', purchasePayment.single),
    path('purchasePayment/edit/<id>/', purchasePayment.edit),
    path('purchasePayment/delete/<id>/', purchasePayment.delete),

    #     path('cost/create/', cost.create,
    #          name='costCreate'),
    #     path('cost/', cost.list),
    #     path('cost/<id>/', cost.single),
    #     path('cost/edit/<id>/', cost.edit),
    #     path('cost/delete/<id>/', cost.delete),


    path('purchaseCost/create/', purchaseCost.create,
         name='purchaseCostCreate'),
    path('purchaseCost/', purchaseCost.list),
    path('purchaseCost/<id>/', purchaseCost.single),
    path('purchaseCost/edit/<id>/', purchaseCost.edit),
    path('purchaseCost/delete/<id>/', purchaseCost.delete),


    path('customer/create/', customer.create, name='customerCreate'),
    path('customer/', customer.list),
    path('customer/<id>/', customer.single),
    path('customer/edit/<id>/', customer.edit),
    path('customer/delete/<id>/', customer.delete),

    path('sale/create/', sale.create, name='saleCreate'),
    path('sale/', sale.list),
    path('sale/<id>/', sale.single),
    path('sale/edit/<id>/', sale.edit),
    path('sale/delete/<id>/', sale.delete),

    path('saleItems/create/', saleItems.create,
         name='saleItemsCreate'),
    path('saleItems/', saleItems.list),
    path('saleItems/<id>/', saleItems.single),
    path('saleItems/edit/<id>/', saleItems.edit),
    path('saleItems/delete/<id>/', saleItems.delete),

    path('salePayment/create/', salePayment.create,
         name='salePaymentCreate'),
    path('salePayment/', salePayment.list),
    path('salePayment/<id>/', salePayment.single),
    path('salePayment/edit/<id>/', salePayment.edit),
    path('salePayment/delete/<id>/', salePayment.delete),
]
