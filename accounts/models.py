from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser ,User

class Country(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'countries'


class Profile(models.Model): 
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(null=True ,blank =True , unique=True)
    country = models.ForeignKey(to = Country , on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    
    class Meta:
        
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'profiles'
        
class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS =2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_CHOICES = (
        (DEVICE_WEB, 'Web'),
        (DEVICE_IOS, 'IOS'),
        (DEVICE_ANDROID, 'Android'),
        (DEVICE_PC, 'PC'),
       
    )
    
    user= models.ForeignKey(to=settings.AUTH_USER_MODEL , related_name ='devices' , on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device UUID' , null = True)
    last_logine = models.DateTimeField( 'last login date',null = True)
    device_type =models.PositiveSmallIntegerField(choices = DEVICE_CHOICES , default = DEVICE_WEB)
    device_os = models.CharField('device os' , max_length = 50 , blank =True)
    device_model = models.CharField('device model' , max_length = 50 , blank =True)
    app_version = models.CharField('app version' , max_length = 50 , blank =True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True) 
    
    class Meta:
        
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        db_table = 'devices'