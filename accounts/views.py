from django.contrib.auth import get_user_model

from rest_framework import generics

from .serializers import RgisteSeliazer

User =get_user_model()

class RgisterView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = RgisteSeliazer