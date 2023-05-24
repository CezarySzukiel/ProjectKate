from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, FormView
from django.views.generic.edit import FormMixin

from exercises_app.models import Exercises, Subsections, Sections, Answer
from exercises_app.forms import SortForm, SortBySubsectionsForm, SortBySectionsForm


class ExercisesListView(FormMixin, ListView):
    template_name = 'exercises_app/exercises_list_view.html'
    model = Exercises
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['subsections'] = Subsections.objects.all() #todo potrzebne tylko roboczo
        # context['sections'] = Sections.objects.all() #todo potrzebne tylko roboczo
        context['sort_by_subsections_form'] = SortBySubsectionsForm()
        context['sort_by_sections_form'] = SortBySectionsForm()
        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     subsection = self.request.GET.get('sort_by_subsections_form', '')
    #     section = self.request.GET.get('sort_by_sections_form', '')
    #     if subsection:
    #         queryset = queryset.filter(subsection__name=subsection)
    #     if section:
    #         queryset = queryset.filter(subsection__section__name=section)
    #     return queryset



# jakiego widoku użyć do wyświetlenia zadania, pobrania odpowiedzi i porównania odpowiedzi z rozwiązaniem?























# class ExercisesCreateView(CreateView):
    # template_name = 'form.html'
    # models = [Exercises, Subsections]
    # fields = '__all__'
    # success_url = reverse_lazy('exercises_list')
