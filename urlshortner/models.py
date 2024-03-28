from django.db import models
from django.utils import timezone
# Create your models here.

class urlModel(models.Model):

    url = models.URLField(max_length=700)
    miniurl = models.CharField(max_length=15, primary_key = True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.miniurl
    
