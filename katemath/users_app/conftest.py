import pytest
from django.contrib.auth.models import User

from .models import UserSettings


@pytest.fixture
def user():
    return User.objects.create(username='test_user',
                               email='testuser@wp.pl',
                               password1='testpassword')


@pytest.fixture
def user_settings():
    lst = []
    lst.append(UserSettings.objects.create(user_id=1,
                                           level=False,
                                           points=0))
