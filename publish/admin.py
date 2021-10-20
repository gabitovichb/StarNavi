from django.contrib import admin
from .models import Report, Like, Dislike


admin.site.register(Report)
admin.site.register(Like)
admin.site.register(Dislike)