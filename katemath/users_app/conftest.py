import pytest
from django.contrib.auth.models import User
from .models import Exercises

from .models import UserSettings
from django.test import Client
from exercises_app.conftest import exercises


@pytest.fixture
def user():
    """Create user for tests"""
    return User.objects.create_user(username='test_user',
                                    password='test_password')

# @ pytest.fixture
# def users():
#     """Create users for tests""" # czy można tak? czy trzeba dopisać też hasło?
#     users = []
#     usernames = ['user1', 'user2', 'user3']
#     for username in usernames:
#         user = User.objects.create(username=username)
#         users.append(user)
#     return users


@pytest.fixture
def user_settings(user):
    """Create user settings for tests"""
    return UserSettings.objects.create(user=user)


@pytest.fixture
def user_exercises(user_settings, exercises):
    user_exercises = []

    for exercise in exercises:
        user_exercises.append(user.user_settings.exercises.add(exercise))
    return user_exercises

