from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.views import APIView
from .models import SliderImages, SocialMedia, MyData
from .serializers import SliderImageSerializer, SocialMediaSerializer, MyDataSerializer
from rest_framework.response import Response

# Create your views here.
class SliderImagesList(mixins.ListModelMixin,generics.GenericAPIView):
  queryset = SliderImages.objects.all()
  serializer_class = SliderImageSerializer

  def get(self,request,*args,**kwargs):
    return self.list(request,*args,**kwargs)


class SocialMediaView(APIView):

  def get(self,request,format=None):
    obj = SocialMedia.objects.last()
    serializer = SocialMediaSerializer(obj)
    return Response(serializer.data)

class MyDataView(APIView):

  def get(self,request,format=None):
    obj = MyData.objects.last()
    serializer = MyDataSerializer(obj)
    return Response(serializer.data)

