from typing import Optional
import requests

class AuthAPI:
    """Клиент для работы с эндпоинтами регистрации и логина ReqRes."""

    REGISTER_PATH = "/api/register"
    LOGIN_PATH = "/api/login"

    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def register(self, email: str, password: str) -> requests.Response:
        """POST /api/register — регистрация пользователя."""
        payload = {"email": email, "password": password}
        return self._session.post(self.REGISTER_PATH, json=payload)

    def login(self, email: str, password: str) -> requests.Response:
        """POST /api/login — авторизация пользователя."""
        payload = {"email": email, "password": password}
        return self._session.post(self.LOGIN_PATH, json=payload)