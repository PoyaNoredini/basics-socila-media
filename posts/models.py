from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    captions = models.TextField(max_length=2048)
    is_active = models.BooleanField(default=True)
    is_public= models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True) 
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'posts'
        
    def __str__ (self):
        return  self.title
        
    
        
class PostFile(models.Model):
    post = models.ForeignKey(to=Post , on_delete = models.CASCADE )
    file_post = models.FileField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True) 
    
    class Meta : 
        verbose_name = 'PostFile'
        verbose_name_plural = 'PostFiles'
        db_table = 'post_files'

"""
class Comment(models.Model):
    pass
class Like(models.Model):
    pass
"""
