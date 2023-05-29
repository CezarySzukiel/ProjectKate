import pytest
from django.contrib.auth.models import User

from .models import UserSettings


@pytest.fixture
def user():
    """Create user for tests"""
    return User.objects.create_user(username='test_user',
                                    email='testuser@wp.pl',
                                    password='testpassword')
