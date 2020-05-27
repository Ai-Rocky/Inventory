from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from main_app.serializers import *
from main_app.models import *


@api_view(['GET'])
def list(request):

    try:
        model = Brand.objects.all()
        serializer = BrandSerializer(
            model, many=True, context={"request": request})
        data = serializer.data
        return Response({'data': data})

    except BaseException as error:
        return Response({'error': str(error)})


@api_view(['GET'])
def single(request, id):

    try:
        model = Brand.objects.get(pk=id)
        serializer = BrandSerializer(
            model, context={"request": request})
        data = serializer.data
        return Response({'data': data})

    except BaseException as error:
        return Response({'error': str(error)})


@api_view(['POST'])
def create(request):

    try:
        serializer = BrandSerializer(
            data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    except BaseException as error:
        return Response({'error': str(error)})


@api_view(['PATCH'])
def edit(request, id):

    try:
        model = Brand.objects.get(pk=id)
        serializer = BrandSerializer(model, data=request.data, context={
            "request": request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    except BaseException as error:
        return Response({'error': str(error)})


@api_view(['DELETE'])
def delete(request, id):

    try:
        model = Brand.objects.get(pk=id)
        brandName = model.Name

        model.delete()

        return Response({'Success': f'The Brand {brandName} is Deleted'})

    except BaseException as error:
        return Response({'error': str(error)})