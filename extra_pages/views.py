from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from .forms import ProfileForm, NoteForm
from extra_pages.models import Profile, Notes


class ProfileDetail(DetailView):
    model = Profile
    template_name = "extra_pages/profile.html"
    context_object_name = "profile"

class ProfileUpdate(UpdateView):
    model = Profile
    template_name = "extra_pages/edit_profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

class AboutYourself(DetailView):
    template_name = "extra_pages/about_us.html"
    context_object_name = "about_us"

class NoteListView(ListView):
    model = Notes
    template_name = "extra_pages/notes.html"
    context_object_name = 'notes'

class NoteDetailView(DetailView):
    model = Notes
    template_name = "extra_pages/notes_detail.html"
    context_object_name = 'note'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    template_name = "extra_pages/notes_form.html"
    form_class = NoteForm
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteDeleteView(DeleteView):
    model = Notes
    template_name = "extra_pages/notes_exploding.html"
    success_url = reverse_lazy('notes')
    context_object_name = 'note'


class NoteEditView(UpdateView):
    model = Notes
    template_name = "extra_pages/notes_edit.html"
    form_class = NoteForm
    success_url = reverse_lazy('notes')
    context_object_name = 'note'
