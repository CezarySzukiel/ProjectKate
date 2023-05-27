from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


def test_create_user_get(client):
    """check if register page is displayed correctly"""
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200


def test_create_user_get_content(client):
    """Powtarzam kod, aby mieć 2 testy, można było umieścić 2 asserty w jednym teście"""
    url = reverse('register')
    response = client.get(url)
    assert 'form' in response.context


@pytest.mark.django_db
def test_create_user_post_valid_form(client):
    """check if user is created when form is valid"""
    url = reverse('register')
    data = {
        'username': 'testuser',
        'email': 'testuser@wp.pl',
        'password1': 'testpassword',
        'password2': 'testpassword'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('base')
    assert User.objects.get(username='testuser')


@pytest.mark.django_db
def test_create_user_post_invalid_form(client):
    """check if user is not created when passwords are different"""
    url = reverse('register')
    data = {
        'username': 'testuser',
        'password1': 'testpassword',
        'password2': 'differentpassword'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'form' in response.context
    assert not User.objects.filter(username=data['username']).exists()

