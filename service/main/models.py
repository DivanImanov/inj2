from django.db import models
import datetime

# Create your models here.

class HomeNew(models.Model):
    content = models.TextField()
    time_create = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-time_create']
    
    def __str__(self) -> str:
        return self.time_create.strftime('%d-%m-%y %a %H:%M:%S')
    
    def save(self, *args, **kwargs):
        if self.time_create is None:
            self.time_create = datetime.datetime.now()
        super().save(*args, **kwargs)
