from . import views
from django.conf.urls import url

urlpatterns = [
    ####### COMPANY #######
    url(r'^$', views.CompanyList.as_view(), name='company_list'),
    url(r'^company-auth/(?P<user>[\w-]+)/$', views.CompanyAuthorList.as_view(), name='company_author'),
    url(r'^create/$', views.CompanyCreate.as_view(), name='company_create'),
    url(r'^company/(?P<company>[\w-]+)/$', views.CompanyDetail.as_view(), name='company_detail'),
    url(r'^company/(?P<company>[\w-]+)/update/$', views.CompanyUpdate.as_view(), name='company_update'),
    url(r'^company/(?P<company>[\w-]+)/delete/$', views.CompanyDelete.as_view(), name='company_delete'),
    ####### TOOL #######
    url(r'^(?P<category>[\w-]+)/$', views.ToolCategoryDetail.as_view(), name='tool_category_detail'),
    url(r'^author/(?P<category>[\w-]+)/(?P<user>[\w-]+)/$', views.ToolAuthorList.as_view(), name='tool_author'),
    url(r'^(?P<company>[\w-]+)/(?P<category>[\w-]+)/create/$', views.ToolCreate.as_view(), name='tool_create'),
    url(r'^(?P<company>[\w-]+)/(?P<category>[\w-]+)/(?P<tool>[\w-]+)/$', views.ToolDetail.as_view(), name='tool_detail'),
    url(r'^(?P<company>[\w-]+)/(?P<category>[\w-]+)/(?P<tool>[\w-]+)/update/$', views.ToolUpdate.as_view(), name='tool_update'),
    url(r'^(?P<company>[\w-]+)/(?P<category>[\w-]+)/(?P<tool>[\w-]+)/delete/$', views.ToolDelete.as_view(), name='tool_delete'),
    url(r'^(?P<category>[\w-]+)/(?P<tool>[\w-]+)/(?P<field_pk>\d+)/create/$', views.ToolEntryCreate.as_view(), name='tool_entry_create'),
    url(r'^(?P<category>[\w-]+)/(?P<tool>[\w-]+)/(?P<field_pk>\d+)/(?P<entry_pk>\d+)/update/$', views.ToolEntryUpdate.as_view(), name='tool_entry_update'),
    url(r'^(?P<category>[\w-]+)/(?P<tool>[\w-]+)/(?P<field_pk>\d+)/(?P<entry_pk>\d+)/delete/$', views.ToolEntryDelete.as_view(), name='tool_entry_delete'),
]
