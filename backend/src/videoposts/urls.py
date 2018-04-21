from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'supervideoposts', views.SuperVideoPostViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    ]