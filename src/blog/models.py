from canvit.utils import unique_slug_generator
from cloudinary.models import CloudinaryField
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    status          = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    title           = models.CharField(max_length=200)
    slug            = models.SlugField(blank=True, editable=False)
    featured_image  = CloudinaryField('image')
    text            = models.TextField()
    published       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={"post": self.slug})

    def __str__(self):
        return self.title

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=Post)
