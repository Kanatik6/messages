from rest_framework.viewsets  import ModelViewSet
from app.models import Message,Title,Descriptions
from app.serializers import MessageSerializer,TitleSerializer,DescriptionsSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class DescriptionsViewSet(ModelViewSet):
    queryset = Descriptions.objects.all()
    serializer_class = DescriptionsSerializer
