from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
from .views import StudentCurd



router.register(r"StudentCurd",StudentCurd,basename="StudentCurd")


urlpatterns = [
    path('', include(router.urls))
]




