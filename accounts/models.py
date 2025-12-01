from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150,unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,unique=True,blank=True,null=True)
    phone = models.CharField(max_length=13,blank=True,null=True)

    def __str__(self):
        return self.username
    
class Profil(models.Model):
    first_name = models.CharField(max_length=150,blank=True,null=True)
    last_name = models.CharField(max_length=150,blank=True,null=True)
    bio = models.CharField(max_length=250,blank=True,null=False)
    avatar = models.ImageField(upload_to='avatars/',default='avatars/avatar.png')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    def __str__(self):
        return self.user.username
