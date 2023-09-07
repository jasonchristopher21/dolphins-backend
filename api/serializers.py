from rest_framework import serializers

from api.logic.parsing_logic import read_files

class S3FileSerializer(serializers.Serializer):
    files = serializers.ListField(child=serializers.CharField(), allow_empty=True)

    def create(self, validated_data):
        read_files(validated_data['files'])
        return validated_data