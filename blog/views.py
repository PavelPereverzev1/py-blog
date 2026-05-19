from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-created_time']
    paginate_by = 5