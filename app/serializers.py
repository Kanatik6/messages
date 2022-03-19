from rest_framework import serializers
from app.models import Message,Title,Descriptions

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        exclude = []


class TitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Title
        exclude = []


class DescriptionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Descriptions
        exclude = []

