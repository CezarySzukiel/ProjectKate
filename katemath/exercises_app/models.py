from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


# TODO add related name to all many to many and foreign keys


class Exercises(models.Model):
    """Model representing an exercise.
    solution_exactly means solution exactly for this exercise,
    solution_similar means solution for a similar task
    type means the type of task: 1 - open task, 2 - multiple choice, etc.
    advanced_level means whether the task is advanced or basic"""
    description = models.TextField()
    subsection = models.ForeignKey('Subsections', on_delete=models.PROTECT)
    difficult = models.IntegerField()
    points = models.IntegerField()
    solution_exactly = models.TextField(null=True, blank=True)
    solution_similar = models.ManyToManyField('self', blank=True)
    type = models.IntegerField()
    advanced_level = models.BooleanField(default=False)

    def get_absolute_url(self):
        """Returns a link to the exercise details"""
        return reverse('exercise_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.description


class Answer(models.Model):
    """Model representing an answer to an exercise.
    For multiple choice exercises, correct means whether the answer is one of the correct answers"""
    exercise = models.ForeignKey('Exercises', on_delete=models.CASCADE)
    answer = models.TextField()
    correct = models.BooleanField(default=True)

    def __str__(self):
        return self.answer


class Sections(models.Model):
    """Model representing a section of exercises"""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Subsections(models.Model):
    """Model representing a subsection of exercises"""
    name = models.CharField(max_length=128)
    section = models.ForeignKey('Sections', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    @staticmethod
    def get_sort_choices():
        """Gets unique values and returns a list of tuples"""
        sort_values = Subsections.objects.values_list('name', flat=True).distinct().order_by('name')
        return [(value, value) for value in sort_values]
