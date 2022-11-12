from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
from .views import DepartmentCurd


router.register(r"DepartmentCurd", DepartmentCurd,basename=DepartmentCurd)

urlpatterns = [
    path('', include(router.urls))
]
