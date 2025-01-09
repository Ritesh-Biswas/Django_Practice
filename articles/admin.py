from django.contrib import admin

# Register your models here.
from .models import Article

class ArtcleAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Article,ArtcleAdmin)