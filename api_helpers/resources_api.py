import requests

class ResourceAPI:
    """Клиент для работы с эндпоинтами ресурсов (палитра) ReqRes."""

    BASE_PATH = "/api/unknown"

    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def get_resources_list(self) -> requests.Response:
        """GET /api/unknown — получение списка всех ресурсов."""
        return self._session.get(self.BASE_PATH)

    def get_resource_by_id(self, resource_id: int) -> requests.Response:
        """GET /api/unknown/{id} — получение одного ресурса по ID."""
        return self._session.get(f"{self.BASE_PATH}/{resource_id}")