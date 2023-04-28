import pytest
from django.urls import reverse
from django.test import Client


def test_index_view(client: Client):

    url = reverse('index')

    response = client.get(url)

    assert response.status_code == 200
    assert 'market/index.html' in [t.name for t in response.templates]