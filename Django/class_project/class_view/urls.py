from django.urls import path, include

from .views import  department_curd

urlpatterns = [
    path('department', department_curd.as_view()),
    path('department/<int:pk>/',department_curd.as_view())

]