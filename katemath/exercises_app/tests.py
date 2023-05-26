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
    # paginacji nie sprawdzamy, bo to jest funkcja wbudowana w django


@pytest.mark.django_db
def test_exercise_detail_view_get(exercises, answer):
    client = Client()
    url = reverse('exercise_details', kwargs={'pk': exercises[2].pk})
    response = client.get(url)
    assert response.status_code == 200
    assert exercises[2].description in response.content.decode()
    # ----------------- for future ---------------------------------
    # right_answer = exercises[2].answer_set.filter(correct=True)
    # right_answer = ', '.join(right_answer.values_list('answer', flat=True))
    # assert right_answer in response.content.decode()
    # będzie potrzebne, gdy będzie możliwość wyświetlania poprawnej odpowiedzi
    # ----------------- for future ---------------------------------


@pytest.mark.django_db
def test_exercise_detail_view_post_correct_answer(exercises, answer):
    client = Client()
    url = reverse('exercise_details', kwargs={'pk': exercises[2].pk})
    data = {'answer': 'correct answer'}
    response = client.post(url, data)

    right_answer = exercises[2].answer_set.filter(correct=True)
    # right_answer = ', '.join(right_answer.values_list('answer', flat=True))
    assert response.status_code == 302
    success_url = reverse('exercise_submit', kwargs={'pk': exercises[2].pk})
    # success_response = client.get(success_url)
    assert response.url == success_url
