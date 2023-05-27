import pytest as pytest
from django.test import Client
from django.urls import reverse


# Create your tests here.
def test_configuration():
    assert True

@pytest.mark.django_db
def test_base_view():
    client = Client()
    url = reverse('base')
    response = client.get(url)
    assert response.status_code == 200
