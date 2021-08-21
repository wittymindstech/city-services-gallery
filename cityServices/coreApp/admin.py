from django.contrib import admin
from coreApp.models import (
    AmenitiesModel,
    BusinessProfileModel,
    OpeningHoursModel,
    ServiceModel,
    ReviewModel,
)
# Register your models here.
admin.site.register(AmenitiesModel)
admin.site.register(BusinessProfileModel)
admin.site.register(OpeningHoursModel)
admin.site.register(ServiceModel)
admin.site.register(ReviewModel)