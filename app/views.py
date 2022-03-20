from rest_framework.viewsets  import ModelViewSet
from app.models import (Message,AboutUs,HomePage, Comments,
                        OurServices, QuickProjectStart)
from app.serializers import (MessageSerializer,OurServicesSerializer,
                             AboutUsSerializer,CommentsSerializer,
                             OurServices,HomePageSerializer,
                             QuickProjectStartSerializer)


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class AboutUsViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class HomePageViewSet(ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class OurServicesViewSet(ModelViewSet):
    queryset = OurServices.objects.all()
    serializer_class = OurServicesSerializer


class QuickProjectStartViewSet(ModelViewSet):
    queryset = QuickProjectStart.objects.all()
    serializer_class = QuickProjectStartSerializer
