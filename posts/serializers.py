from rest_framework import serializers 


from .models import Post


class PostSerializers(serializers.ModelSerializer): 
    class Meta: 
        model = Post
        fields = ('user','title','captions','is_active','is_public')
        
        extra_kwargs = {
            'user' : {'read_only' : True}
            }
  