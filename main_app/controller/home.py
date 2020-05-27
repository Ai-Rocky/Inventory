from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def index(request):
    return Response("Hello World")
