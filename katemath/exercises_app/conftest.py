import pytest

from .models import Exercises, Answer, Subsections, Sections


@pytest.fixture
def sections():
    lst = []
    lst.append(Sections.objects.create(name="Dział 1"))
    lst.append(Sections.objects.create(name="Dział 2"))
    return lst


@pytest.fixture
def subsections(sections):
    lst = []
    lst.append(Subsections.objects.create(name="Poddział 1", section=sections[0]))
    lst.append(Subsections.objects.create(name="Poddział 2", section=sections[1]))
    return lst


@pytest.fixture
def exercises(subsections):
    lst = []
    lst.append(Exercises.objects.create(descriotion="Zadanie 1",
                                        subsection=subsections[0],
                                        difficult=1,
                                        points=1,
                                        solution_exactly="solution 1",
                                        type=1,
                                        advanced_level=False))
    lst.append(Exercises.objects.create(description="Zadanie 2",
                                        subsection=subsections[1],
                                        difficult=2,
                                        points=2,
                                        solution_similar=exercises[0], # to nie zadziała bo exercises jeszcze nie istnieje?
                                        type=1,
                                        advanced_level=True))
    lst.append(Exercises.objects.create(description="Zadanie 3",
                                        subsection=subsections[0],
                                        difficult=3,
                                        points=3,
                                        type=2,
                                        advanced_level=True))
    lst.append(Exercises.objects.create(description="Zadanie 4",
                                        subsection=subsections[1],
                                        difficult=1,
                                        points=1,
                                        type=1,
                                        advanced_level=False))
    lst.append(Exercises.objects.create(description="Zadanie 5",
                                        subsection=subsections[1],
                                        difficult=1,
                                        points=1,
                                        type=1,
                                        advanced_level=False))
    lst.append(Exercises.objects.create(description="Zadanie 6",
                                        subsection=subsections[1],
                                        difficult=1,
                                        points=1,
                                        type=1,
                                        advanced_level=False))
    lst.append(Exercises.objects.create(description="Zadanie 7",
                                        subsection=subsections[1],
                                        difficult=1,
                                        points=1,
                                        type=1,
                                        advanced_level=False))
    lst.append(Exercises.objects.create(description="Zadanie 8",
                                        subsection=subsections[1],
                                        difficult=1,
                                        points=1,
                                        type=1,
                                        advanced_level=False))
    lst.append(Exercises.objects.create(description="Zadanie 9",
                                        subsection=subsections[1],
                                        difficult=1,
                                        points=1,
                                        type=1,
                                        advanced_level=False))
    lst.append(Exercises.objects.create(description="Zadanie 10",
                                        subsection=subsections[1],
                                        difficult=1,
                                        points=1,
                                        type=1,
                                        advanced_level=False))
    lst.append(Exercises.objects.create(description="Zadanie 11",
                                        subsection=subsections[1],
                                        difficult=1,
                                        points=1,
                                        type=1,
                                        advanced_level=False))
    return lst


@pytest.fixture
def answer(exercises):
    lst = []
    lst.append(Answer.objects.create(exercise=exercises[0],
                                     answer="Odpowiedź 1",
                                     correct=True))
    lst.append(Answer.objects.create(exercise=exercises[1],
                                     answer="Odpowiedź 2",
                                     correct=True))
    lst.append(Answer.objects.create(exercise=exercises[2],
                                     answer="Odpowiedź 3",
                                     correct=True))
    lst.append(Answer.objects.create(exercise=exercises[2],
                                     answer="Odpowiedź 4",
                                     correct=False))
    lst.append(Answer.objects.create(exercise=exercises[2],
                                     answer="Odpowiedź 5",
                                     correct=False))
    return lst
