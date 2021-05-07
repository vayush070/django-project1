from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField()
    mobile=models.CharField(max_length=12)
    description=models.TextField()
    date = models.DateTimeField(default=datetime.now(), blank=True)


    def __str__(self):
        return self.email
    