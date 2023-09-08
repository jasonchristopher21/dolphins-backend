from django.http import HttpResponseBadRequest
from django.db.models import F

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.models import (
    Results,
    Client,
    ClientInsight
)

from api.serializers import (
    S3FileSerializer,
)


from api.logic.parsing_logic import read_files
from api.logic.openai_logic import parse_text_to_ML_format
from api.logic.ml_logic import predict

class ProcessFilesView(APIView):

    def post(self, request, *args, **kwargs):
        parsed_data = read_files(request.data['files'])
        predictions = predict(None)
        # serializer_data = S3FileSerializer(data=request.data)
        # serializer_data.is_valid(raise_exception=True)
        # serializer_data.save()
        return Response(predictions, status=status.HTTP_201_CREATED)


class RetrieveResultsView(generics.ListAPIView):

    def get_queryset(self):
        qs = Results.objects.annotate(client_name=F('client__name')).values(
            'client_id', 'client_name', 'result')
        return qs