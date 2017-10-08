from blog.models import Post
from django.template import Library

register = Library()

@register.simple_tag
def get_posts(number=0):
    if number <= 0:
        posts = Post.objects.filter(status="p").order_by("-published")
    else:
        posts = Post.objects.filter(status="p").order_by("-published")[:number]
    return posts
