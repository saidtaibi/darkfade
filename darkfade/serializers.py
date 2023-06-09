from rest_framework import serializers
from .models import SocialMedia, SliderImages, MyData

class SliderImageSerializer(serializers.ModelSerializer):
  class Meta:
    model= SliderImages
    fields = ['id','image']

class SocialMediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = SocialMedia
    fields = '__all__'

class MyDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = MyData
    fields = '__all__'
