from  rest_framework import routers

from django.urls import path, include

from .views import home, TeacherCurd
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

router = routers.DefaultRouter()

router.register(r'teacher',TeacherCurd,basename='teacher')

urlpatterns = [
    path("",include(router.urls)),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('home/', home),

]