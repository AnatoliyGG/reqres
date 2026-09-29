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

    def update_user_full(self, user_id: int, name: str, job: str) -> requests.Response:
        """PUT /api/users/{id} — полное обновление данных пользователя."""
        payload = {"name": name, "job": job}
        return self._session.put(f"{self.BASE_PATH}/{user_id}", json=payload)

    def update_user_partial(self, user_id: int, name: Optional[str] = None,
                            job: Optional[str] = None) -> requests.Response:
        """PATCH /api/users/{id} — частичное обновление данных пользователя."""
        payload: Dict[str, Any] = {}
        if name is not None:
            payload["name"] = name
        if job is not None:
            payload["job"] = job
        return self._session.patch(f"{self.BASE_PATH}/{user_id}", json=payload)

    def delete_user(self, user_id: int) -> requests.Response:
        """DELETE /api/users/{id} — удаление пользователя по ID."""
        return self._session.delete(f"{self.BASE_PATH}/{user_id}")