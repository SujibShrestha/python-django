from django.db import models
from django.utils import timezone
# Create your models here.

class appVariety(models.Model):
    APP_TYPE =[
        ("Hy", "Hybrid"),    
        ("In", "Indica"),
        ("Sa", "Sativa"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apps/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE, default="Hy")
    description = models.TextField(default="", max_length=500, blank=True)

    def __str__(self):
        return self.name 