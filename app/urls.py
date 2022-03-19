from rest_framework.routers import SimpleRouter
from app.views import MessageViewSet,TitleViewSet,DescriptionsViewSet

router = SimpleRouter()
router.register('messages',MessageViewSet)
router.register('title',TitleViewSet)
router.register('descriptions',DescriptionsViewSet)

urlpatterns = []
urlpatterns +=router.urls
