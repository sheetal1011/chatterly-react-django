from rest_framework import serializers
from .models import Blog,Comments

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model:Blog
        fields=['id','title','description','image_path','created_at','user','comments']

class CommentsSerializer(serializers.ModelSerializer):  
    class Meta:
        model:Comments
        fields=['id','text','date']     

