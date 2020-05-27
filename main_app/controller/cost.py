from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from main_app.serializers import *
from main_app.models import *


@api_view(['GET'])
def list(request):

    try:
        model = Cost.objects.all()
        serializer = CostSerializer(
            model, many=True, context={"request": request})
        data = serializer.data
        return Response({'data': data})

    except BaseException as error:
        return Response({'error': str(error)})


@api_view(['GET'])
def single(request, id):

    try:
        model = Cost.objects.get(pk=id)
        serializer = CostSerializer(
            model, context={"request": request})
        data = serializer.data
        return Response({'data': data})

    except BaseException as error:
        return Response({'error': str(error)})


@api_view(['POST'])
def create(request):

    try:
        serializer = CostSerializer(
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
        model = Cost.objects.get(pk=id)
        serializer = CostSerializer(model, data=request.data, context={
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
        model = Cost.objects.get(pk=id)
        name = model.Name

        model.delete()

        return Response({'Success': f'The Cost {name} is Deleted'})

    except BaseException as error:
        return Response({'error': str(error)})