from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView, name="home"),
    path('updateView/<int:pk>/', views.updateView, name="update"),
    path('deleteView/<int:pk>/', views.deleteView, name="delete"),
]
