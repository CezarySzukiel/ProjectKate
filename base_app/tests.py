import pytest as pytest
from django.test import Client
from django.urls import reverse


# Create your tests here.
def test_configuration():
    """Test that configuration is OK."""
    assert True


@pytest.mark.django_db
def test_base_view():
    """Test that base view is working."""
    client = Client()
    url = reverse('base')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_base_view_content():
    """Test that base view is working."""
    client = Client()
    url = reverse('base')
    response = client.get(url)
    assert 'Katemath' in response.content.decode()
