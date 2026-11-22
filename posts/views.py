from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["titulo", "contenido", "imagen"]
    template_name = "posts/post_form.html"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class AutorRequeridoMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().autor == self.request.user


class PostUpdateView(LoginRequiredMixin, AutorRequeridoMixin, UpdateView):
    model = Post
    fields = ["titulo", "contenido", "imagen"]
    template_name = "posts/post_form.html"


class PostDeleteView(LoginRequiredMixin, AutorRequeridoMixin, DeleteView):
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("posts:lista")