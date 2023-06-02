from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View


# Create your views here.
class BaseView(View):
    """Displays the welcome page"""
    def get(self, request):
        return render(request, 'base.html')
