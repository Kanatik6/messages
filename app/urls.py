from rest_framework.routers import SimpleRouter
from app.views import (MessageViewSet,AboutUsViewSet,
                       CommentsViewSet,HomePageViewSet,ContactViewSet,
                       OurServicesViewSet,QuickProjectStartViewSet)

router = SimpleRouter()
router.register('messages',MessageViewSet)
router.register('about_us',AboutUsViewSet)
router.register('home_page',HomePageViewSet)
router.register('comments',CommentsViewSet)
router.register('our_services',OurServicesViewSet)
router.register('quick_project_start',QuickProjectStartViewSet)
router.register('contacts',ContactViewSet)

urlpatterns = []
urlpatterns +=router.urls
