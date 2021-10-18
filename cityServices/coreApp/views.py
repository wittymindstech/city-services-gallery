from django.shortcuts import render

from coreApp.serializers import (
    BusinessSerializer,
    CategorySerializer,
    )

from coreApp.models import (
    CategoyModel,
    BusinessProfileModel,
    OpeningHoursModel,
    )

from rest_framework.views import APIView

# Create your views here.
def LandingPageView(request):
    context = {
        'categories':CategoyModel.objects.all()[0:9],
        'businesses':BusinessProfileModel.objects.all()[0:9]
    }
    return render(request, 'coreApp/index.html', context)


def CategoryView(request, name):
    
    context = {
        'businesses' : BusinessProfileModel.objects.filter(category__name = name)
    }
    return render(request, 'coreApp/listing-list.html', context)

def BusinessDetailView(request, slug):
    
    business = BusinessProfileModel.objects.get(slug=slug)
    opening_hours = OpeningHoursModel.objects.filter(business=business)
    context = {
        'business': business,
        'opening_hours': opening_hours, 
    }
    return render(request, 'coreApp/listing-single.html', context)
