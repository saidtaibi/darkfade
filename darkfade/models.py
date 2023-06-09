from django.db import models

# Create your models here.

class SocialMedia(models.Model):
  twitter = models.CharField(max_length=2000,null=True)
  facebook = models.CharField(max_length=2000,null=True)
  youtube = models.CharField(max_length=2000,null=True)
  instagram = models.CharField(max_length=2000,null=True)
  def __str__(self):
    return self.twitter

class MyData(models.Model):
  address = models.CharField(max_length=2000,null=True)
  address_link = models.CharField(max_length=3000,null=True)
  phone = models.CharField(max_length=50,null=True)
  phone_link = models.CharField(max_length=50,null=True)
  email = models.EmailField(max_length=300,null=True)
  email_link = models.EmailField(max_length=1000,null=True)
  def __str__(self):
    return self.address

def image_upload(instance,filename):
  name = instance.name
  ext = filename.split('.')[-1]
  return f'slider/{name}.{ext}'

class SliderImages(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to=image_upload,max_length=300)
  def __str__(self):
    return self.name