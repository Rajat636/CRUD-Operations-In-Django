from django.db import models

# Create your models here.
#After creating models here we need to register them in admin so that we can access it from admin database.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

