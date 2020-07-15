from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from main_app.serializers import *
from main_app.models import *


@api_view(['POST'])
def login(request):
    try:
        email, password = request.data["Email"], request.data["Password"]
        model = MyUser.objects.get(Email=email, Password=password)

        serializer = MyUserRelationalSerializer(model)
        return Response({"status": True, "login": serializer.data})

    except BaseException as error:
        return Response({"status": False, "login": str(error)})


@api_view(['PATCH'])
def update(request, id):

    try:
        model = MyUser.objects.get(pk=id)
        serializer = MyUserSerializer(model, data=request.data, context={
            "request": request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "patchMessage": "Update Success"})

        return Response({"status": False, "patchError": serializer.errors})

    except BaseException as error:
        return Response({"status": "error", "errorMessage": str(error)})
