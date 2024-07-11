from rest_framework import serializers
from .models import Blog,Comments


class CommentsSerializer(serializers.ModelSerializer):  
    class Meta:
        model=Comments
        fields=['id','text','date'] 


class BlogSerializer(serializers.ModelSerializer):
    comments=CommentsSerializer(many=True,read_only=True)
    class Meta:
        model=Blog
        fields=['id','title','description','image_path','created_at','user','comments']  

