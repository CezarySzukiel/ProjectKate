from django.test import TestCase
import pytest as pytest
from django.test import Client
from django.urls import reverse

# Create your tests here.


@pytest.mark.django_db
def test_exercises_list_view():
    client = Client()
    url = reverse('exercises_list')
    response = client.get(url)
    assert response.status_code == 200
    # paginacji nie sprawdzamy, bo to jest funkcja wbudowana w django

