from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the post")
    subtitle = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField()
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment