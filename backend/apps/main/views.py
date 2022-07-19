
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_201_CREATED
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from apps.main.serializers import UserSerializer, CreateUserSerializer


class UserDetail(APIView):
    def get_object(self, username):
        return get_user_model().objects.filter(username=username).first()

    @extend_schema(request=UserSerializer, responses=UserSerializer, description='Get user information')
    def get(self, request, username, format=None):
        user = self.get_object(username)
        if(not user):
            return Response(status=HTTP_404_NOT_FOUND)
        else:
            return Response(UserSerializer(user).data)

    @extend_schema(request=UserSerializer, responses=UserSerializer, description='Update user information')
    def put(self, request, username, format=None):
        user = self.get_object(username)
        if(not user):
            return Response(status=HTTP_404_NOT_FOUND)
        else:
            serializer = UserSerializer(user, data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=UserSerializer, responses=UserSerializer, description='Delete user')
    def delete(self, request, username, format=None):
        user = self.get_object(username)
        if(not user):
            return Response(status=HTTP_404_NOT_FOUND)
        else:
            user.delete()
            return Response(status=HTTP_204_NO_CONTENT)


class UserList(APIView):
    @extend_schema(request=CreateUserSerializer, responses=CreateUserSerializer, description='Create one user.')
    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
