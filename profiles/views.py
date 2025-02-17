from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileForm


class ProfileDetailedView(DetailView, LoginRequiredMixin):
    model = Profile
    template_name = "profiles/profile.html"
    context_object_name = "profile"

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profiles/edit_profile.html"

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('profile')


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = "profiles/delete_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)
