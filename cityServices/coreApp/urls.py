from django.urls import path
from coreApp.views import home

app_name = 'coreApp'

urlpatterns = [
    path('',home, name='homepage'),
]