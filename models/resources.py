from typing import List

from pydantic import BaseModel, ConfigDict, Field


class StrictBaseModel(BaseModel):
    """Базовая строгая модель для контрактной валидации API-ответов."""

    model_config = ConfigDict(extra="forbid", strict=True)

class ResourceData(StrictBaseModel):
    """Модель одного цветового ресурса ReqRes."""

    id: int
    name: str = Field(min_length=1)
    year: int = Field(ge=0)
    color: str = Field(min_length=1)
    pantone_value: str = Field(min_length=1)

class ResourcesListResponse(StrictBaseModel):
    """Модель ответа GET /api/unknown."""

    page: int = Field(gt=0)
    per_page: int = Field(gt=0)
    total: int = Field(ge=0)
    total_pages: int = Field(gt=0)
    data: List[ResourceData]

class SingleResourceResponse(StrictBaseModel):
    """Модель ответа GET /api/unknown/{id}."""

    data: ResourceData