from pydantic import BaseModel, Field
from typing import TypeVar, Generic, List

T = TypeVar("T")


class PaginationParams(BaseModel):
    page: int = Field(default=1, gt=0)
    size: int = Field(default=10, gt=0, le=100)


class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
    pages: int
