from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from users_app.forms import LoginForm, UserCreateForm


# Create your views here.


class CreateUserView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('base')
        return render(request, 'form.html', {'form': form})


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