from django.contrib import admin
from .models import Image,Location,Category

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Location)