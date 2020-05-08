from django.views.generic import ListView
from django.views.generic.edit import CreateView


from .models import Post
from .forms import PostForm


class BlogList(ListView):
    queryset = Post.objects.all()[:10]
    context_object_name = 'blog_list'
    template_name = 'blog.html'


class BlogCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_form.html'