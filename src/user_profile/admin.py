from .models import Profile
from django.contrib import admin

####### PROFILE #######
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Profile, ProfileAdmin)
