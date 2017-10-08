from .models import Post
from django.contrib import admin

####### POST #######
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status','published',]

admin.site.register(Post, PostAdmin)
