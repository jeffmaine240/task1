from django.urls import path
from . import views

urlpatterns = [
    path('api/hello', views.HelloView.as_view(), name='hello'),
]