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
    assert response.status_code == 302
    success_url = reverse('exercise_submit', kwargs={'pk': exercises[2].pk})
    assert response.url == success_url


@pytest.mark.django_db
def test_submit_view_get(client):
    url = reverse('exercise_submit', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_submit_view_cookies(client):
    url = reverse('exercise_submit', kwargs={'pk': 1})
    response = client.get(url)
    assert 'correct_answer' in response.cookies
    assert 'user_answer' in response.cookies


