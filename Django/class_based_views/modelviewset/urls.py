from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
from .views import EmployeeCurd

router.register(r"EmployeeCurd", EmployeeCurd,basename=EmployeeCurd)

urlpatterns = [
    path('', include(router.urls))
]
