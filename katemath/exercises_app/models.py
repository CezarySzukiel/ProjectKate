from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Exercises(models.Model):
    description = models.TextField()
    subsection = models.ForeignKey('Subsections', on_delete=models.PROTECT)
    difficult = models.IntegerField()
    points = models.IntegerField()
    solution_exactly = models.TextField(null=True, blank=True)
    solution_similar = models.ManyToManyField('self', blank=True)
    type = models.IntegerField()
    advanced_level = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Answer(models.Model):
    exercise = models.ForeignKey('Exercises', on_delete=models.CASCADE)
    answer = models.TextField()
    correct = models.BooleanField(default=True)

    def __str__(self):
        return self.answer


class Sections(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Subsections(models.Model):
    name = models.CharField(max_length=128)
    section = models.ForeignKey('Sections', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
