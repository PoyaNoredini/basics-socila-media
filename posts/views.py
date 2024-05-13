from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializers

from .models import Post


class PostView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request ,post_pk):
        try : 
            post = Post.objects.get(pk=post_pk , user = request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializers = PostSerializers(post)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = PostSerializers(data = request.data )
        if serializers.is_valid(raise_exception=True):
            serializers.save(user=request.user)
            return Response(serializers.data)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class PostListView(APIView):
    
    def get(self , request):
        
        post = Post.objects.filter(is_active = True)
        serializers = PostSerializers(post , many = True)
        
        return Response(serializers.data)