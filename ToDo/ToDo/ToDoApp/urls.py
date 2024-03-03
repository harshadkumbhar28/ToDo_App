from django.contrib import admin
from django.urls import path, include
from .views import ToDoApp, create, edit, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ToDoApp, name="index"),
    path('create/', create, name="create"),
    path('edit/', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),

]