import pandas as pd
from io import StringIO

from rest_framework import serializers

from api.models import Results

from api.logic.parsing_logic import read_files
from api.logic.openai_logic import parse_text_to_ML_format
from api.logic.ml_logic import predict

class S3FileSerializer(serializers.Serializer):
    files = serializers.ListField(child=serializers.CharField(), allow_empty=True)

    def create(self, validated_data):
        parsed_data = read_files(validated_data['files'])
        # parsed_csv = parse_text_to_ML_format(parsed_data)
        # dataframe = pd.read_csv("yada-yada-yada.csv")
        predictions = predict(None)
        return predictions

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'