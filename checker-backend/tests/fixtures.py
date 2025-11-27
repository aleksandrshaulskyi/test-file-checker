from pytest import fixture
from rest_framework.test import APIClient


@fixture
def base_api_client() -> APIClient:
    """
    Returns:
        APIClient: an instance of DRF APIClient for making requests.
    """
    return APIClient()
