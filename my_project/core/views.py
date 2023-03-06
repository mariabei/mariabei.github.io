from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from core.models import Post

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.all().order_by('created_at')[:10]
        return {
            'posts': posts
        }


class PostDetail(DetailView):
    template_name = 'post_detail.html'

    model = Post


class CreatePostView(CreateView):
    template_name = 'create_post_view.html'
    model = Post
    fields = ('title', 'text', 'tags')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('/')



