from django.urls import path
from coreApp.views import (
    LandingPageView,
    CategoryView,
    BusinessDetailView,
)

app_name = 'coreApp'

urlpatterns = [
    path('',LandingPageView, name='homepage'),
    path('category/<str:name>/', CategoryView, name='category_listing'),
    path('<str:slug>/', BusinessDetailView, name='detail_view')
]