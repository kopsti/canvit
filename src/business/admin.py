from .models import Company, ToolCategory, Tool, ToolField, ToolEntry
from django.contrib import admin

####### COMPANY #######
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title','author','section','url','published']

admin.site.register(Company, CompanyAdmin)

####### TOOL #######
class ToolCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

class ToolAdmin(admin.ModelAdmin):
    list_display = ['title','category','company','author','published']

class ToolFieldAdmin(admin.ModelAdmin):
    list_display = ['title','category']

class ToolEntryAdmin(admin.ModelAdmin):
    list_display = ['title','field','tool']

admin.site.register(ToolCategory, ToolCategoryAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(ToolField, ToolFieldAdmin)
admin.site.register(ToolEntry, ToolEntryAdmin)
