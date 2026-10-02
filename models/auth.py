from pydantic import BaseModel, ConfigDict, Field

class StrictBaseModel(BaseModel):
    """Базовая строгая модель для контрактной валидации API-ответов."""

    model_config = ConfigDict(extra="forbid", strict=True)

class AuthSuccessResponse(StrictBaseModel):
    """Модель успешного ответа регистрации или авторизации."""

    id: int
    token: str = Field(min_length=1)

class AuthErrorResponse(StrictBaseModel):
    """Модель ответа API при ошибке регистрации или авторизации."""

    error: str = Field(min_length=1)