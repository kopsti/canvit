from .forms import ProfileForm
from .models import Profile
from django.views.generic import DetailView, UpdateView

#Allows a user to view a published company.
class ProfileDetail(DetailView):
    model = Profile
    slug_url_kwarg = 'profile'

    def get_queryset(self):
        return Profile.objects.all()

#Allows an auth user to update his profile.
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    slug_url_kwarg = 'profile'

    def get_template_names(self):
        if self.request.is_ajax():
            return ['user_profile/profile_update_form.html']
        else:
            raise Http404

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
