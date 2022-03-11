from django.views.generic import TemplateView, CreateView
from .forms import SignUpForms

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from userprofile.models import Profile

from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'common/home.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user.id)
        context['book_list'] = self.request.user
        return context


class SignUpView(CreateView):
    form_class = SignUpForms
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'common/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'common/profile-update.html'

    def post(self, request):
        post_data = request.POST or None
        file_date = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_date, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.error( request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)