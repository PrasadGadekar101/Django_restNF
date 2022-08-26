import email
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True,)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    sus_status = models.BooleanField(default=True)
    sus_months = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(12)])
    email = models.EmailField()


    def __str__(self):
        return self.email

#to show models info in place it __str__ method should be defined like this in the model class
# def __str__(self):
#     return '{}'.format(self.name)