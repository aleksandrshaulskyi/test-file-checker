from time import time

from pytest import mark
from unittest.mock import patch

from tests.fixtures import *


@mark.django_db
def test_registration_endpoint(base_api_client):
    """
    Ensures that registration endpoint works properly with valid data.
    """
    with patch('applications.users.viewsets.users.CreateUserViewSet.perform_create'):
        request_data = {'email': f'test_{time()}@test.com', 'password': '1'}
        response = base_api_client.post('/api/users/', request_data)

        assert response.status_code == 201
