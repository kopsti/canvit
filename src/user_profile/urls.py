from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<profile>[\w-]+)/$', views.ProfileDetail.as_view(), name='profile_detail'),
    url(r'^(?P<profile>[\w-]+)/edit-profile/$', views.ProfileUpdate.as_view(), name='profile_update'),
]
