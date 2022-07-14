from random import random

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from apps.main.serializers import UserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def random_float(request):
    return Response(random())


@api_view(['GET'])
def user_list(request):
    if (request.method == 'GET'):
        return Response(UserSerializer(get_user_model().objects.all(), many=True).data)


@api_view(['GET'])
def user_detail(request, pk):
    if (request.method == 'GET'):
        return Response(UserSerializer(get_user_model().objects.filter(id=pk).first()).data)
