import pytest
import requests
from typing import Generator

from config import BASE_URL, REQUEST_TIMEOUT

@pytest.fixture(scope="session")
def api_session() -> Generator[requests.Session, None, None]:
    """Создаёт единую сессию requests на весь запуск тестов."""
    session = requests.Session()
    session.base_url = BASE_URL
    session.timeout = REQUEST_TIMEOUT
    yield session
    session.close()

@pytest.fixture(scope="function")
def users_api_client(api_session: requests.Session) -> "UsersAPI":
    """Фикстура для клиента Users API."""
    from api_helpers.users_api import UsersAPI
    return UsersAPI(api_session)

@pytest.fixture(scope="function")
def resources_api_client(api_session: requests.Session) -> "ResourceAPI":
    """Фикстура для клиента Resources API."""
    from api_helpers.resources_api import ResourceAPI
    return ResourcesAPI(api_session)

@pytest.fixture(scope="function")
def auth_api_client(api_session: requests.Session) -> "AuthAPI":
    """Фикстура для клиента Auth API."""
    from api_helpers.auth_api import AuthAPI
    return AuthAPI(api_session)