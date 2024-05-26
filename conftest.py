# pylint: disable=unused-argument, unused-import

import pytest
from django.contrib.auth import get_user_model
from model_bakery.recipe import Recipe
from rest_framework.test import APIClient
from checker.fixtures import fixture_mock_task_data

custom_user = Recipe(
    get_user_model(),
    first_name="Test",
    last_name="Test",
)


@pytest.fixture(name="user")
def fixture_user():
    return custom_user.make()


@pytest.fixture(name="auth_client")
def fixture_auth_client(user) -> APIClient:
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture(name="not_auth_client")
def fixture_not_auth_client() -> APIClient:
    client = APIClient()
    return client
