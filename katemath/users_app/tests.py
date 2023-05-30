from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


def test_create_user_get(client):
    """Check if register page is displayed correctly"""
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200


def test_create_user_get_context(client):
    """Check if register page contains form"""
    url = reverse('register')
    response = client.get(url)
    assert 'form' in response.context


@pytest.mark.django_db
def test_create_user_post_valid_form(client):
    """Check if user is created when form is valid"""
    url = reverse('register')
    data = {
        'username': 'testuser',
        'email': 'testuser@wp.pl',
        'password1': 'testpassword',
        'password2': 'testpassword'
    }
    response = client.post(url, data)
    user = User.objects.get(username=data['username'])
    assert response.status_code == 302
    assert response.url == reverse('base')
    assert User.objects.get(username='testuser')
    assert user.is_authenticated


@pytest.mark.django_db
def test_create_user_post_invalid_form(client):
    """Check if user is not created when passwords are different"""
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


def test_login_get(client):
    """Check if login page is displayed correctly"""
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


def test_login_get_context(client):
    """Check if login page contains form"""
    url = reverse('login')
    response = client.get(url)
    assert 'form' in response.context


@pytest.mark.django_db
def test_login_post_valid_form(client, user):
    """Check if user is logged in when form is valid"""
    url = reverse('login')
    data = {
        'username': 'test_user',
        'password': 'testpassword'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('base')
    assert user.is_authenticated


@pytest.mark.django_db
def test_login_post_invalid_form(client):
    """Check if user is not logged in when form is invalid"""
    url = reverse('login')
    data = {
        'username': 'test_user',
        'password': 'wrong_password'
    }
    User.objects.create_user(username='test_user', password='testpassword')
    response = client.post(url, data)
    assert response.status_code == 200
    assert not response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_logout(client, user):
    """Check if user is logged out"""
    client.force_login(user)
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == reverse('base')


@pytest.mark.django_db
def test_logout(client, user):
    """Check if user is logged out"""
    client.force_login(user)
    url = reverse('logout')
    response = client.get(url)
    assert not response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_user_panel_get(client, user):
    """Check if user panel is displayed correctly"""
    client.force_login(user)
    url = reverse('user_panel')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_panel_get_context(client, user):
    """Check if user panel is displayed correctly"""
    client.force_login(user)
    url = reverse('user_panel')
    response = client.get(url)
    assert 'user' in response.context
