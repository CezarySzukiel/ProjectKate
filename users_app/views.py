from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from exercises_app.models import Exercises
from users_app.forms import LoginForm, UserCreateForm, UserSettingsForm
from users_app.models import UserSettings


# Create your views here.


class CreateUserView(View):
    """Create new user"""
    def get(self, request):
        """Display forms for creating new user"""
        user_form = UserCreateForm()
        settings_form = UserSettingsForm()
        return render(request, 'users_app/create_user_form.html', {'user_form': user_form, 'settings_form': settings_form})

    def post(self, request):
        """Getting data from forms and creating new user"""
        user_form = UserCreateForm(request.POST or None)
        settings_form = UserSettingsForm(request.POST or None)
        if user_form.is_valid() and settings_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            user_settings = UserSettings.objects.create(user=user, level=settings_form.cleaned_data['level'])
            user.usersettings = user_settings
            user.save()
            login(request, user)
            return redirect('base')
        return render(request, 'users_app/create_user_form.html', {'user_form': user_form, 'settings_form': settings_form})


class LoginView(View):
    """Login user"""

    def get(self, request):
        """Display form for login user"""
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        """Getting data from form and login user"""
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']

            if user is not None:
                login(request, user)
            return redirect('base')
        return render(request, 'form.html', {'form': form})


class LogoutView(View):
    """Logout user"""
    def get(self, request):
        logout(request)
        return redirect('base')


class UserPanelView(LoginRequiredMixin, View):
    """Display user panel with user data"""
    def get(self, request):
        user = request.user
        context = {'user': user}
        return render(request, 'users_app/user_panel.html', context)


class UserExercisesListView(LoginRequiredMixin, ListView):
    """Display user exercises"""
    model = Exercises
    template_name = 'users_app/user_exercises_list.html'
    context_object_name = 'exercises'
    paginate_by = 10

    def get_queryset(self):
        """Return exercises for logged user"""
        return self.request.user.usersettings.exercises.all()



