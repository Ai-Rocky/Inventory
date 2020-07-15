from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from main_app.serializers import *
from main_app.models import *
from datetime import timedelta, date
import math


@api_view(['POST'])
def purchase(request):

    try:
        outlet = request.data[0]
        startDate = request.data[1]
        endDate = request.data[2]

        endDate = date.fromisoformat(endDate)
        endDate = endDate + timedelta(days=1)

        if(outlet == "all"):
            if(startDate == endDate):
                purchases = Purchase.objects.filter(Date__date=startDate)
            else:
                purchases = Purchase.objects.filter(
                    Date__range=(startDate, endDate))
                # purchases = Purchase.objects.filter(
                #     Date__gte=startDate, Date__lte=endDate)
        else:
            if(startDate == endDate):
                purchases = Purchase.objects.filter(
                    Outlet=outlet, Date__date=startDate)
            else:
                purchases = Purchase.objects.filter(Outlet=outlet,
                                                    Date__range=(startDate, endDate))

        items = PurchaseItem.objects.all()
        payments = PurchasePayment.objects.all()

        supAmount = supPaid = 0
        for purchase in purchases:
            subAmount = subPaid = 0
            for item in items:
                if purchase.id == item.Purchase.id:
                    subAmount += item.PurchasePrice * item.Quantity

            for payment in payments:
                if purchase.id == payment.Purchase.id:
                    subPaid += payment.Amount

            if purchase.Discount is None:
                purchase.Discount = 0

            supAmount += subAmount - (subAmount * purchase.Discount / 100)
            supPaid += subPaid

        numberOfInvoice = purchases.count()
        totalAmount = math.ceil(supAmount)
        totalPaid = math.ceil(supPaid)
        totalDue = totalAmount - totalPaid

        result = {"status": True, "purchase": {"count": numberOfInvoice,
                                               "amount": totalAmount, "paid": totalPaid, "due": totalDue}}
        return Response(result)

    except BaseException as error:
        return Response({"status": "error", "purchase": str(error)})


@api_view(['POST'])
def sale(request):

    try:
        outlet = request.data[0]
        startDate = request.data[1]
        endDate = request.data[2]

        endDate = date.fromisoformat(endDate)
        endDate = endDate + timedelta(days=1)

        if(outlet == "all"):
            if(startDate == endDate):
                sales = Sale.objects.filter(Date__date=startDate)
            else:
                sales = Sale.objects.filter(
                    Date__range=(startDate, endDate))
        else:
            if(startDate == endDate):
                sales = Sale.objects.filter(
                    Outlet=outlet, Date__date=startDate)
            else:
                sales = Sale.objects.filter(Outlet=outlet,
                                            Date__range=(startDate, endDate))

        sitems = SaleItem.objects.all()
        pitems = PurchaseItem.objects.all()
        payments = SalePayment.objects.all()

        supsAmount = suppAmount = supPaid = supProfit = 0
        for sale in sales:
            subsAmount = subpAmount = subPaid = subProfit = 0
            for sitem in sitems:
                if sale.id == sitem.Sale.id:
                    samount = sitem.Price * sitem.Quantity
                    subsAmount += samount
                    pPrice = 0
                    for pitem in pitems:
                        if sitem.Product.id == pitem.Product.id:
                            pPrice = pitem.PurchasePrice
                    pamount = pPrice * sitem.Quantity
                    subpAmount += pamount
                    subProfit += samount - pamount

            for payment in payments:
                if sale.id == payment.Sale.id:
                    subPaid += payment.Amount

            if sale.Discount is None:
                sale.Discount = 0

            supsAmount += subsAmount - (subsAmount * sale.Discount / 100)
            suppAmount += subpAmount
            supPaid += subPaid
            supProfit += subProfit

        numberOfInvoice = sales.count()
        totalsAmount = math.ceil(supsAmount)
        totalpAmount = math.ceil(suppAmount)
        totalPaid = math.ceil(supPaid)
        totalDue = totalsAmount - totalPaid
        profit = supProfit

        result = {"status": True, "sale": {"count": numberOfInvoice,
                                           "amount": totalsAmount, "paid": totalPaid, "due": totalDue, "profit": profit}}
        return Response(result)

    except BaseException as error:
        return Response({"status": "error", "sale": str(error)})
