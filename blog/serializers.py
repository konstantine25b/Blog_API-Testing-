from rest_framework import serializers
from .models import Post ,Comment, Tag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)
        
    def create(self,validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author',)
        
    def create(self,validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
    
    
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']
    
    
    
