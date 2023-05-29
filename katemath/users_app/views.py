from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from users_app.forms import LoginForm, UserCreateForm, UserSettingsFormSet
from users_app.models import UserSettings


#UserSettingsForm


# Create your views here.


# _______________________________ todo do sprawdzenia _______________________________
class CreateUserView(View):
    def get(self, request):
        form = UserCreateForm()
        formset = UserSettingsFormSet(request.POST or None, instance=form.instance)
        return render(request, 'form.html', {'form': form, 'formset': formset})

    def post(self, request):
        form = UserCreateForm(request.POST or None)
        formset = UserSettingsFormSet(request.POST or None, instance=form.instance)
        if form.is_valid() and formset.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            user.usersettings = UserSettings.objects.create(user=user) # creates a relationship with the user, needed when the level field is not checked.
            user.save()
            formset.save()
            login(request, user)
            return redirect('base')
        return render(request, 'form.html', {'form': form, 'formset': formset})

# _______________________________ do sprawdzenia _______________________________


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None:
                login(request, user)
            return redirect('base')
        return render(request, 'form.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('base')


class UserPanelView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        points = user.usersettings.points
        # context = {'form': UserSettingsForm()}
        context = {'points': points}
        return render(request, 'user_panel.html', context)
