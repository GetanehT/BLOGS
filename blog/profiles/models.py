from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=225, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_hba20g.jpg'

    )

class Meta: 
    ordering = ['created_at']

def __str__(self):
    return  f"{self.owner}'s profiles"  

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)

# Create your models here.
 