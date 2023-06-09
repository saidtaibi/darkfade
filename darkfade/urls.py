from django.urls import path
from . import views

app_name='darkfade'

urlpatterns = [
  path('slider/list',views.SliderImagesList.as_view(),name='slider-list'),
  path('social-media',views.SocialMediaView.as_view(),name='social-media'),
  path('my-data',views.MyDataView.as_view(),name='my-data'),
]