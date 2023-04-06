from django.db import models

# SuperUser
# userName: Tharvin
# Password: Tharvin_24
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    manufacturing_since = models.DateField()

    def __str__(self):
        return f'{self.name}'

class PhoneModel(models.Model):
    name = models.CharField(max_length=50)
    launch_date = models.DateField()
    platform = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    title = models.CharField(max_length=100)
    article = models.TextField()
    date_published = models.DateTimeField()
    models = models.ManyToManyField(PhoneModel)

    def __str__(self):
        return f'{self.title}'