from .models import Post
from django.db.models import Q
from django.views.generic import DetailView, ListView

####### POST #######
#Allows a user to view the list of Posts.
class PostList(ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.filter(status='p').order_by("-published")
        query = self.request.GET.get("q")
        sort = self.request.GET.get("s")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(text__icontains=query)
                ).distinct()
        if sort:
            queryset = queryset.all().order_by(sort)
        return queryset

#Allows a user to view a published post.
class PostDetail(DetailView):
    model = Post
    slug_url_kwarg = 'post'

    def get_queryset(self):
        return Post.objects.filter(status='p')
