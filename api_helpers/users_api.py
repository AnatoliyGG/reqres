from typing import Optional, Dict, Any
import requests


class UserAPI:
    """Клиент для работы с эндпоинтами пользователей ReqRes."""

    BASE_PATH = "/api/users"

    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def get_users_list(self, page: Optional[int] = None) -> requests.Response:
        """GET /api/users — получение списка пользователей с пагинацией."""
        params: Dict[str, Any] = {}
        if page is not None:
          params["page"] = page
        return self._session.get(f"({self.BASE_PATH}", params=params)

    def get_user_by_id(self, user_id: int) -> requests.Response:
        """GET /api/users/{id} — получение одного пользователя по ID."""
        return self._session.get(f"{self.BASE_PATH}/{user_id}")

    def create_user(self, name: str, job: str) -> requests.Response:
        """POST /api/users — создание нового пользователя."""
        payload = {"name": name, "job": job}
        return self._session.post(self.BASE_PATH, json=payload)