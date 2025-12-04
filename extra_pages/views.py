from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from .forms import ProfileForm
from extra_pages.models import Profile


class ProfileDetail(DetailView):
    model = Profile
    template_name = "extra_pages/profile.html"
    form_class = ProfileForm
    context_object_name = "profile"
