from django.urls import path
from apps.pages.front.views import index

urlpatterns = [
    path('', index, name='index'),
]