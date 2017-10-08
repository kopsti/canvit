from . import views
from django.conf.urls import url

urlpatterns = [
    ####### POST #######
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^post/(?P<post>[\w-]+)/$', views.PostDetail.as_view(), name='post_detail'),
]
