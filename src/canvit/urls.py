from canvit import views
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from registration.backends.hmac.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

urlpatterns = [
    url(r'^$', views.home_redirect, name='home_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^profile/', include('user_profile.urls', namespace='profile')),
    url(r'^business/', include('business.urls', namespace='business')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^accounts/register/$',  RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='auth_signup'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^comments/', include('django_comments_xtd.urls')),
]

urlpatterns += staticfiles_urlpatterns()
