from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from main_app.serializers import *
from main_app.models import *


@api_view(['GET'])
def list(request):

    try:
        model = SalePayment.objects.all()
        serializer = SalePaymentListSerializer(
            model, many=True, context={"request": request})

        return Response({"status": True, "getList": serializer.data})

    except BaseException as error:
        return Response({"status": "error", "errorMessage": str(error)})


@api_view(['GET'])
def single(request, id):

    try:
        model = SalePayment.objects.get(pk=id)
        serializer = SalePaymentSerializer(
            model, context={"request": request})

        return Response({"status": True, "getSingle": serializer.data})

    except BaseException as error:
        return Response({"status": "error", "errorMessage": str(error)})


@api_view(['POST'])
def create(request):

    try:

        # request.data['Category'] = Category.objects.filter(
        #     id=request.data['Category']).values().first()

        serializer = SalePaymentSerializer(
            data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "postMessage": "Create Success"})

        return Response({"status": False, "postError": serializer.errors})

    except BaseException as error:
        return Response({"status": "error", "errorMessage": str(error)})


@api_view(['PATCH'])
def edit(request, id):

    try:
        model = SalePayment.objects.get(pk=id)
        serializer = SalePaymentSerializer(model, data=request.data, context={
            "request": request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "patchMessage": "Update Success"})

        return Response({"status": False, "patchError": serializer.errors})

    except BaseException as error:
        return Response({"status": "error", "errorMessage": str(error)})


@api_view(['DELETE'])
def delete(request, id):

    try:
        model = SalePayment.objects.get(pk=id)
        model.delete()

        return Response({"status": True, "deleteMessage": "Delete Success"})

    except BaseException as error:
        return Response({"status": "error", "errorMessage": str(error)})
