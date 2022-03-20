from rest_framework import serializers
from app.models import (Message,AboutUs,HomePage, Comments,
                        OurServices, QuickProjectStart)


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        exclude = []


class AboutUsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AboutUs
        exclude = []


class HomePageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HomePage
        exclude = []


class CommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        exclude = []


class OurServicesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OurServices
        exclude = []


class QuickProjectStartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuickProjectStart
        exclude = []
