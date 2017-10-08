from business.models import Company, ToolCategory, Tool, ToolField, ToolEntry
from django.template import Library

register = Library()

####### COMPANY #######
@register.simple_tag
def get_companies(number=0):
    if number <= 0:
        companies = Company.objects.all().order_by("-published")
    else:
        companies = Company.objects.all().order_by("-published")[:number]
    return companies

####### TOOL #######
@register.simple_tag
def get_tool_categories():
    tool_categories = ToolCategory.objects.all().order_by("order")
    return tool_categories

@register.simple_tag
def get_tools(category, author, company, number=0):
    tools = Tool.objects.filter(category=category)
    if company != "":
        tools = tools.filter(company=company)
    if author != "":
        tools = tools.filter(author=author)
    if number > 0:
        tools = tools.all()[:number]
    return tools

@register.simple_tag
def get_fields(tool):
    fields = ToolField.objects.filter(category=tool.category).order_by("order")
    return fields

@register.simple_tag
def get_entries(field, tool):
    tools = ToolEntry.objects.filter(field=field, tool=tool)
    return tools
