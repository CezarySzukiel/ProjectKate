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


@pytest.fixture
def user_settings(user, exercises):
    """Create user settings for tests"""
    exercise = exercises[0]
    a = type(exercise) # <class 'exercises_app.models.Exercises'> (ModelBase)
    exercise2 = exercises[1]
    user_settings = UserSettings.objects.create(user=user)
    exercise3 = exercises[2]
    return user_settings # type: #<class 'users_app.models.UserSettings.MultipleObjectsReturned'>


@pytest.fixture
def user_exercises(user_settings, exercises):
    """Add exercises to user settings"""
    lst = []
    lst.append(user_settings.exercises.add(exercises[0].pk))
    lst.append(user_settings.exercises.add(exercises[1].pk))
    lst.append(user_settings.exercises.add(exercises[2].pk))
    return lst

