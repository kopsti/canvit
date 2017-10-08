from canvit.utils import unique_slug_generator
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save

class Profile(models.Model):
    user        = models.OneToOneField(User)
    slug        = models.SlugField(blank=True, editable=False)
    first_name  = models.CharField(max_length=200, blank=True)
    last_name   = models.CharField(max_length=200, blank=True)
    avatar      = CloudinaryField('image')
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('profile:profile_detail', kwargs={"profile": self.slug,})

    def __str__(self):
        return self.user.username

    @property
    def title(self):
        return  self.user.username

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=Profile)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
