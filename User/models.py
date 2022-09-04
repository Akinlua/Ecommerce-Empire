from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=250)
    email= models.EmailField(max_length=500, unique= True, null=True, blank=True)
    username= models.CharField(max_length=200)
    is_admin= models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique= True, primary_key= True, editable=False)

    def __str__(self):
        return str(self.user) 

