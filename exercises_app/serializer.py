from .models import Exercises, Subsections, Sections, Answer
from rest_framework import serializers

class ExercisesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercises
        fields = ('description', 'subsection', 'difficult', 'points', 'solution_exactly', 'solution_similar', 'type', 'advanced_level')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('exercise', 'answer', 'correct')

class SectionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sections
        fields = ('name',)

class SubsectionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subsections
        fields = ('name', 'section')

