from django.urls import path, include

from app1.views import add_call

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('add_call/', add_call),
]