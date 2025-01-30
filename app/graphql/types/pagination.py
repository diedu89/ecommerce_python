from typing import TypeVar, Generic, List
import strawberry
from app.schemas.pagination import PaginationParams

T = TypeVar("T")


@strawberry.experimental.pydantic.input(model=PaginationParams, all_fields=True)
class PaginationInput:
    pass


@strawberry.type
class PaginatedResponse(Generic[T]):
    items: List[T] = strawberry.field(description="List of items in current page")
    total: int = strawberry.field(description="Total number of items")
    page: int = strawberry.field(description="Current page number")
    size: int = strawberry.field(description="Items per page")
    pages: int = strawberry.field(description="Total number of pages")
