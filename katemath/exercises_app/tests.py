from django.test import TestCase
import pytest as pytest
from django.test import Client
from django.urls import reverse
from exercises_app.models import Exercises, Answer
from exercises_app.forms import AnswerForm

# Create your tests here.


@pytest.mark.django_db
def test_exercises_list_view():
    client = Client()
    url = reverse('exercises_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_exercises_list_view_content(exercises):
    client = Client()
    url = reverse('exercises_list')
    response = client.get(url)
    assert exercises[0].description in response.content.decode()
    for e in exercises[:10]:
        assert e.description in response.content.decode()


@pytest.mark.django_db
def test_exercise_detail_view_get(exercises, answer):
    client = Client()
    url = reverse('exercise_details', kwargs={'pk': exercises[2].pk})
    response = client.get(url)
    assert response.status_code == 200

    # ----------------- for future ---------------------------------
    # right_answer = exercises[2].answer_set.filter(correct=True)
    # right_answer = ', '.join(right_answer.values_list('answer', flat=True))
    # assert right_answer in response.content.decode()
    # będzie potrzebne, gdy będzie możliwość wyświetlania poprawnej odpowiedzi
    # ----------------- for future ---------------------------------


def test_exercise_detail_view_get_content(exercises, answer):
    """check if context in content in detail view"""
    client = Client()
    url = reverse('exercise_details', kwargs={'pk': exercises[2].pk})
    response = client.get(url)
    assert exercises[2].description in response.content.decode()


@pytest.mark.django_db
def test_exercise_detail_view_post(exercises, answer):
    """check if post ok and redirect to submit view ok"""
    client = Client()
    url = reverse('exercise_details', kwargs={'pk': exercises[2].pk})
    data = {'user_answer': 'correct answer'}
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_exercise_detail_view_post_correct_answer(exercises, answer):
    """check if correct answer is in content in submit view"""
    client = Client()
    url = reverse('exercise_details', kwargs={'pk': exercises[2].pk})
    data = {'user_answer': 'correct answer'}
    response = client.post(url, data, follow=True)
    assert 'Poprawna' in response.content.decode()
