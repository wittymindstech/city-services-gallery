from rest_framework import serializers
from coreApp.models import BusinessProfileModel, CategoyModel
class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfileModel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoyModel
        fields = '__all__'
