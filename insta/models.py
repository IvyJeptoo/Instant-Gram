from django.db import models
from django.contrib.auth.models import User


# user, profile, post, comments


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_picture=models.ImageField()
    
    def __str__(self):
        return self.bio
    
    
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField()
    caption=models.TextField(max_length=100)
    # likes=models.ForeignKey('Likes',on_delete=models.SET_NULL)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
    
class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.TextField(max_length=200)
    
    
    def __str__(self):
        return self.comment
    
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE,related_name='follower')
    total_followings= models.ForeignKey(User, on_delete=models.CASCADE,related_name='followers')
    
    def __str__(self):
        return self.follower
    
    

    


