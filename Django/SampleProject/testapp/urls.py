from django.urls import path

from .views import home, town, table, user_table, create, edit, update, delete, registration, login, user_logout

urlpatterns = [
    path('',home),
    path('town/',town),
    path('table/',table),
    path('user/',user_table),
    path('create/',create),
    path('edit/<int:id>/',edit),
    path('update/<int:id>/',update),
    path('delete/<int:id>/',delete),
    path('register/',registration),
    path('login/',login),
    path('logout/',user_logout)
]