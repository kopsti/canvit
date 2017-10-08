from canvit.utils import unique_slug_generator
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from smart_selects.db_fields import ChainedForeignKey
from star_ratings.models import Rating

class Company(models.Model):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(blank=True, editable=False)
    author      = models.ForeignKey(User)
    logo        = CloudinaryField('image')
    section     = models.CharField(max_length=200)
    description = models.TextField()
    wiki        = models.URLField(blank=True)
    url         = models.URLField(blank=True)
    ratings     = GenericRelation(Rating, related_query_name='stars')
    published       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Companies"

    def get_absolute_url(self):
        return reverse('business:company_detail', kwargs={"company": self.slug,})

    def __str__(self):
        return self.title

class ToolCategory(models.Model):
    title   = models.CharField(max_length=200)
    slug    = models.SlugField(blank=True, editable=False)
    order   = models.IntegerField(default=1)

    class Meta:
        verbose_name        = "Tool Category"
        verbose_name_plural = "Tool Categories"

    def get_absolute_url(self):
        return reverse('business:tool_category_detail', kwargs={"category": self.slug,})

    def __str__(self):
        return self.title

class Tool(models.Model):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(blank=True, editable=False)
    category    = models.ForeignKey(ToolCategory)
    company     = models.ForeignKey(Company)
    author      = models.ForeignKey(User)
    published   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('business:tool_detail', kwargs={"company": self.company.slug, "category": self.category.slug, "tool": self.slug,})

    def __str__(self):
        return self.title

class ToolField(models.Model):
    title       = models.CharField(max_length=200)
    category    = models.ForeignKey(ToolCategory)
    icon        = CloudinaryField('image')
    hint        = models.TextField()
    order       = models.IntegerField(default=1)

    class Meta:
        verbose_name        = "Tool Field"
        verbose_name_plural = "Tool Fields"

    def get_entries(self):
        return ToolEntry.objects.filter(field=self)

    def __str__(self):
        return self.title

class ToolEntry(models.Model):
    category    = models.ForeignKey(ToolCategory)
    author      = models.ForeignKey(User)
    title       = models.CharField(max_length=200)
    field       = ChainedForeignKey(
        ToolField,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True)
    tool        = ChainedForeignKey(
        Tool,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True)

    class Meta:
        verbose_name        = "Tool Entry"
        verbose_name_plural = "Tool Entries"

    def get_absolute_url(self):
        return reverse('business:tool_detail', kwargs={"company": self.tool.company.slug, "category": self.tool.category.slug, "tool": self.tool.slug,})

    def __str__(self):
        return self.title

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=Company)
pre_save.connect(pre_save_receiver, sender=ToolCategory)
pre_save.connect(pre_save_receiver, sender=Tool)
