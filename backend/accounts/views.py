from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from rest_framework.views import APIView
from rest_framework import exceptions, status
from rest_framework.response import Response

from accounts.models import UserModel
from accounts.serializers import UserSerializer


class RegisterUser(APIView):
    def post(self, request):
        data = request.data
        if data['password'] !=  data['confirm_password']:
            raise exceptions.ValidationError(_('Your password does not match'))

        username = data['username']
        if UserModel.objects.filter(username=username).exists():
            raise exceptions.AuthenticationFailed(_('This username is already taken'))

        email = data['email']
        if UserModel.objects.filter(email=email).exists():
            raise exceptions.ValidationError(_('This email is already taken'))

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
