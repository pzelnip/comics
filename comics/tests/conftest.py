import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def superadmin(client):
    user = User.objects.create_superuser("newadmin", "admin@example.com", "admin")
    client.force_login(user)


@pytest.fixture
def nonadmin(client):
    user = User.objects.create_user(username="notanadmin", password="notanadmin")
    client.force_login(user)
