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
