from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sheet(models.Model):
    name=models.CharField(max_length=80)
    rows=models.IntegerField()
    colomns=models.IntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.name