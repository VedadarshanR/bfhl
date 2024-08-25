from rest_framework import serializers

class DataInputSerializer(serializers.Serializer):
    data = serializers.ListField(
        child=serializers.CharField(),  
        allow_empty=False
    )