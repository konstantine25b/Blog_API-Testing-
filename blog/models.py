from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length =True , unique =True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title= models.CharField(max_length =200)
    content= models.TextField()
    author = models.ForeignKey(User, on_delete =models.CASCADE , related_name = 'posts')
    tags = models.ManyToManyField(Tag , related_name='posts')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        indexes = [ 
            models.Index(fields='created_at')
       ]
    
    def __str__(self):
        return self.title
    
class comments(models.Model):
    post =models.ForeignKey(Post, on_delete =models.CASCADE, related_name = 'comments')
    author =models.ForeignKey(User, on_delete =models.CASCADE, related_name = 'comments')
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"comment by {self.author} on {self.post}"
    
    