from django.http import HttpResponseBadRequest
from django.db.models import F

from api.serializers import ResultsSerializer

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
        return Response(predictions, status=status.HTTP_201_CREATED)

class RetrieveResultsView(generics.ListAPIView):
    
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer