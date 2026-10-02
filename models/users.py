from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, EmailStr, Field

class StrictBaseModel(BaseModel):
    """Базовая строгая модель для контрактной валидации API-ответов."""

    model_config = ConfigDict(extra="forbid", strict=True)

class UserData(StrictBaseModel):
    """Модель одного пользователя из ответа ReqRes."""

    id: int
    email: EmailStr
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    avatar: str = Field(min_length=1)

class UsersListResponse(StrictBaseModel):
    """Модель ответа GET /api/users."""

    page: int = Field(gt=0)
    per_page: int = Field(gt=0)
    total: int = Field(ge=0)
    total_pages: int = Field(gt=0)
    data: List[UserData]

class SingleUserResponse(StrictBaseModel):
    """Модель ответа GET /api/users/{id}."""

    data: UserData

class UserCreatedResponse(StrictBaseModel):
    """Модель ответа POST /api/users."""

    name: str = Field(min_length=1)
    job: str = Field(min_length=1)
    id: str = Field(min_length=1)
    createdAt: datetime

class UserUpdatedResponse(StrictBaseModel):
    """Модель ответа PUT/PATCH /api/users/{id}."""

    name: str = Field(min_length=1)
    job: str = Field(min_length=1)
    updatedAt: datetime