from django.db import models

# Create your models here.
class Services(models.Model):
    services_type = models.CharField(max_length=50)

