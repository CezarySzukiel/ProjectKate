from django.shortcuts import render
from rest_framework import viewsets

from exercises_app.models import Exercises, Answer, Sections, Subsections
from .serializer import ExercisesSerializer, AnswerSerializer, SectionsSerializer, SubsectionsSerializer
# Create your views here.


class ExercisesViewSet(viewsets.ModelViewSet):
    """API endpoint that allows exercises to be viewed or edited."""
    queryset = Exercises.objects.all().order_by('id')
    serializer_class = ExercisesSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows answers to be viewed or edited."""
    queryset = Answer.objects.all().order_by('id')
    serializer_class = AnswerSerializer


class SectionsViewSet(viewsets.ModelViewSet):
    """API endpoint that allows sections to be viewed or edited."""
    queryset = Sections.objects.all().order_by('id')
    serializer_class = SectionsSerializer


class SubsectionsViewSet(viewsets.ModelViewSet):
    """API endpoint that allows subsections to be viewed or edited."""
    queryset = Subsections.objects.all().order_by('id')
    serializer_class = SubsectionsSerializer