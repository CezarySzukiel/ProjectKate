from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from exercises_app.models import Exercises, Subsections, Sections, Answer
from exercises_app.forms import SortForm, SortBySubsectionForm


class ExercisesListView(ListView):
    template_name = 'exercises_app/exercises_list_view.html'
    model = Exercises
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subsections'] = Subsections.objects.all()
        context['sections'] = Sections.objects.all()
        context['sort_form'] = SortBySubsectionForm()
        return context


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     sort_by = self.request.GET.get('sort_by', '')

        # related = Exercises.objects.select_related('subsections').all()
        # context['related'] = Exercises.objects.select_related('subsections').all()

    # def get_queryset(self):
    #     return super().get_queryset().order_by('description')


# class ExercisesCreateView(CreateView):
    # template_name = 'form.html'
    # models = [Exercises, Subsections]
    # fields = '__all__'
    # success_url = reverse_lazy('exercises_list')
