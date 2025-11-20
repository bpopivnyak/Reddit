from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from . import models
from .forms import PostForm
from .models import Post
class PostView(ListView):
    model = Post
    template_name = "main/posts.html"
    form_class = PostForm



