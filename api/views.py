from django.shortcuts import render
from django.http import HttpResponseBadRequest

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.serializers import (
    S3FileSerializer,
)
class ParserView(APIView):

    def post(self, request, *args, **kwargs):
        serializer_data = S3FileSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()
        return Response(serializer_data.data, status=status.HTTP_201_CREATED)