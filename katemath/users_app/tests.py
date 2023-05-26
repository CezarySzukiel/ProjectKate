from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse

# Create your tests here.


def test_create_user_get():
    client = Client()
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200


def test_create_user_get_content():
    client = Client()
    url = reverse('register')
    response = client.get(url)
    assert 'Username' in response.content.decode()

