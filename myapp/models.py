from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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



# 1 - *

class appReview(models.Model):
    app = models.ForeignKey(appVariety,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(max_length=5.0)
    comment = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(default= timezone.now)


    def __str__(self):
        return f'{self.user.username} reviewed {self.app.name} with rating {self.rating}'


# many to many

class Store(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    app_varieties = models.ManyToManyField(appVariety, related_name='stores')

    def __str__(self):
        return self.name

#one to one

class appCertificate(models.Model):
    app = models.OneToOneField(appVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate {self.certificate_number} for {self.app.name}'
