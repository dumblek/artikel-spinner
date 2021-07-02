from django.contrib import admin

from .models import Words, StopWords

admin.site.register(Words)
admin.site.register(StopWords)