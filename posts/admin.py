from django.contrib import admin

from .models import Post, PostFile



class PostFildInLineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('file_post',)
    extra = 0
    can_delete = False
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','title','is_active','created_time' , 'pk' )
    inlines = (PostFildInLineAdmin,)


