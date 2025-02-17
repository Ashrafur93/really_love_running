from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import logout

class ProfileDetailedView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/profile.html"
    context_object_name = "profile"

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

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

    def form_valid(self, form):
        profile = self.get_object()
        user = profile.user
        print(f"Deleting user: {user.username}")  # Debug print statement
        logout(self.request)  # Log out the user
        print(f"User {user.username} logged out")  # Debug print statement
        user.delete()  # Delete the user account
        print(f"User {user.username} deleted")  # Debug print statement
        return redirect(self.success_url)