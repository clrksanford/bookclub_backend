from rest_framework import routers
from api import views


router = routers.SimpleRouter()
router.register(r'events', views.EventViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = router.urls
