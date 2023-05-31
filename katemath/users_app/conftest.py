import pytest
from django.contrib.auth.models import User
from .models import UserSettings, Exercises
from django.test import Client
from exercises_app.conftest import exercises, subsections, sections


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
    user_settings = UserSettings.objects.create(user=user)
    return user_settings


@pytest.fixture
def user_exercises(user_settings, exercises):
    print('wyprintowano', user_settings.exercises.all()) #pusty queryset
    u_exercises = [exercises[0], exercises[1], exercises[2]]
    # user_settings.exercises.add(exercises[0])
    # user_settings.exercises.add(exercises[1])
    # user_settings.exercises.add(exercises[2])
    result = user_settings.exercises.add(*u_exercises)
    return result
# albo tworząc user_settings dodać exercises zaraz po userze.
# @ pytest.fixture
# def user_exercises(user_settings, exercises):
#     """Create user exercises for tests"""
#     lst = []
#     lst.append()

    # user_exercises.append(user.user_settings.exercises.create(exercises[0]))
    # user_exercises.append('alamakota')
    # for exercise in exercises:
    #     user_exercises.append(user.user_settings.exercises.add(exercise))
    return user_exercises

