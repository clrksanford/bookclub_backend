from django.urls import path
from rest_framework import routers
from api import views


router = routers.SimpleRouter()
router.register(r'events', views.EventViewSet)

urlpatterns = router.urls
