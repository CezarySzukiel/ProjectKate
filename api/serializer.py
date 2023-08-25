from exercises_app.models import Exercises, Answer, Sections, Subsections
from rest_framework import serializers


class ExercisesSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes exercises model"""
    class Meta:
        model = Exercises
        fields = ('description', 'subsection', 'difficult', 'points', 'solution_exactly', 'solution_similar', 'type', 'advanced_level')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes answers model"""
    class Meta:
        model = Answer
        fields = ('exercise', 'answer', 'correct')


class SectionsSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes sections model"""
    class Meta:
        model = Sections
        fields = ('name',)


class SubsectionsSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes subsections model"""
    class Meta:
        model = Subsections
        fields = ('name', 'section')
