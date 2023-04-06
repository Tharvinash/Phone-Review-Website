from django.contrib import admin
from .models import PhoneModel, Brand, Review

# Register your models here.
admin.site.register(Brand)
admin.site.register(PhoneModel)
admin.site.register(Review)