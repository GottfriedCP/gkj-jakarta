from django.contrib import admin
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_expired', 'summary')

# Register your models here.
admin.site.register(Announcement, AnnouncementAdmin)