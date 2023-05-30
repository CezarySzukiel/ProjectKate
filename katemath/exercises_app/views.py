from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, FormView
from django.views.generic.edit import FormMixin

from exercises_app.models import Exercises, Subsections, Sections, Answer
from exercises_app.forms import AnswerForm


class ExercisesListView(ListView):
    """Displays a list of exercises"""
    template_name = 'exercises_app/exercises_list_view.html'
    model = Exercises
    paginate_by = 10


class ExerciseDetailsView(View):
    """Displays exercise details and form to submit answer"""
    template_name = 'exercises_app/exercise_detail_view.html'

    def get(self, request, pk):
        """Displays exercise and form to submit answer"""
        exercise = Exercises.objects.get(pk=pk)
        answers = Answer.objects.filter(exercise=exercise)
        context = {
            'exercise': exercise,
            'answers': answers,
            'form': AnswerForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        """Gets user's answer and checks it with correct answer.
        If answer is correct, user gets points"""
        answer = request.POST.get('answer', '')
        exercise = Exercises.objects.get(pk=pk)
        correct_answer = Answer.objects.filter(exercise=exercise, correct=True)
        correct_answer = str(correct_answer.values_list('answer', flat=True)[0])
        res = redirect('exercise_submit', pk=pk)
        if answer == correct_answer:
            if request.user.is_authenticated:
                user = request.user
                user.usersettings.points += exercise.points
                user.usersettings.save()
            res.set_cookie('user_answer', answer)
            res.set_cookie('correct_answer', correct_answer)
            return res
        return res


class SubmitView(View):
    """If user's answer is correct, displays a message"""
    template_name = 'exercises_app/submit_view.html'

    def get(self, request, pk):
        res = render(request, self.template_name)
        res.delete_cookie('correct_answer')
        res.delete_cookie('user_answer')
        return res



