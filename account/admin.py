from django.contrib import admin

from .models import Favorites, Towatch

# Register your models here.
admin.site.register(Favorites)
admin.site.register(Towatch)
