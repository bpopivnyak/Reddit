from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from .forms import PostForm, CommentsForm
from .models import Post
class PostView(ListView):
    model = Post
    template_name = "main/posts.html"
    form_class = PostForm
    context_object_name = "posts"


class PostDetail(DetailView):
    model = Post
    template_name = "main/post_detail.html"
    form_class = PostForm
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comment_form'] = CommentsForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentsForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('', pk=comment.pk)
        else:
            pass

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "main/post_form.html"
    form_class = PostForm
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class PostDelete(DeleteView):
    model = Post
    template_name = "main/post_destruction.html"
    success_url = reverse_lazy('posts')
