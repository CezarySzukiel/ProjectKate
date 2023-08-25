from django.shortcuts import render, redirect
from django.views import View

from exercises_app.models import Exercises, Subsections, Sections, Answer
from exercises_app.forms import AnswerForm, FilterForm


# class ExercisesListView(ListView):
#     """Displays a list of exercises"""
#     template_name = 'exercises_app/exercises_list_view.html'
#     model = Exercises
#     paginate_by = 10


class ExercisesListView(View):
    """Displays a list of exercises"""
    template_name = 'exercises_app/exercises_list_view.html'

    def get(self, request):
        """Displays a list of exercises with filters"""
        exercises = Exercises.objects.all()
        context = {
            'exercises': exercises,
            'form': FilterForm(),
            }
        return render(request, self.template_name, context)

    def post(self, request):
        """Displays a list of exercises with filters"""
        # prawie dobrze, ale jeśli zaznaczę subsekcję z geometrii a następnie sekcję ciągi to jest błąd
        form = FilterForm(request.POST)
        sections_form = form.data.getlist('sections') #zwraca listę idików przesłaną w formularzu
        subsections_form = form.data.getlist('subsections')
        sections = Sections.objects.filter(pk__in=sections_form) # zwraca queryset z obiektami Sections o id z listy sectionsform
        subsections = Subsections.objects.filter(pk__in=subsections_form)
        if sections:
            form.set_subsections_queryset(sections)
            exercises = Exercises.objects.filter(subsection__in=Subsections.objects.filter(section__in=sections_form))
        if subsections:
            exercises = Exercises.objects.filter(subsection__in=subsections)
        elif not sections and not subsections:
            exercises = Exercises.objects.all()
        context = {
            'exercises': exercises,
            'form': form,
            }
        return render(request, self.template_name, context)


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
        user = request.user
        correct_answer = Answer.objects.filter(exercise=exercise, correct=True)
        correct_answer = str(correct_answer.values_list('answer', flat=True)[0])
        res = redirect('exercise_submit', pk=pk)
        if answer == correct_answer:
            if request.user.is_authenticated and exercise not in user.usersettings.exercises.all():
                user.usersettings.points += exercise.points
                user.usersettings.save()
                user.usersettings.exercises.add(exercise)
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


