from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, FormView
from django.views.generic.edit import FormMixin

from exercises_app.models import Exercises, Subsections, Sections, Answer
from exercises_app.forms import SortForm, SortBySubsectionsForm, SortBySectionsForm, AnswerForm


class ExercisesListView(ListView):
    template_name = 'exercises_app/exercises_list_view.html'
    model = Exercises
    paginate_by = 10


class ExerciseDetailsView(View):
    # jakiego widoku użyć do wyświetlenia zadania, pobrania odpowiedzi i porównania odpowiedzi z rozwiązaniem?
    template_name = 'exercises_app/exercise_detail_view.html'

    def get(self, request, pk):
        """Wyświetla zadanie i formularz do wpisania odpowiedzi"""
        exercise = Exercises.objects.get(pk=pk)
        answers = Answer.objects.filter(exercise=exercise)
        context = {
            'exercise': exercise,
            'answers': answers,
            'form': AnswerForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        """Pobiera odpowiedź użytkownika i sprawdza z poprawną odpowiedzią"""
        answer = request.POST.get('answer', '')
        exercise = Exercises.objects.get(pk=pk)
        correct_answer = Answer.objects.filter(exercise=exercise, correct=True)
        correct_answer = str(correct_answer.values_list('answer', flat=True)[0])
        # fake_answers = Answer.objects.filter(exercise=exercise, correct=False)
        context = {
            'exercise': exercise,
            'answer': answer,
            'correct_answer': correct_answer,
        }
        if answer == correct_answer:
            context['correct'] = True
        else:
            context['correct'] = False
            # przekierowanie zrobić ciasteczkami i redirectem
            res = redirect('exercise_submit', pk=pk)
            res.set_cookie('correct_answer', correct_answer)
            return res
        # return render(request, 'exercises_app/submit_view.html', context)


class SubmitView(View):
    template_name = 'exercises_app/submit_view.html'

    def get(self, request, pk):
        print(request.COOKIES)
        res = render(request, self.template_name)
        res.delete_cookie('correct_answer')
        return res



















# class ExercisesCreateView(CreateView):
    # template_name = 'form.html'
    # models = [Exercises, Subsections]
    # fields = '__all__'
    # success_url = reverse_lazy('exercises_list')
