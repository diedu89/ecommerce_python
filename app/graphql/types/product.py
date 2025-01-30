import strawberry
from .pagination import PaginatedResponse
from app.schemas.product import (
    Product as ProductSchema,
    ProductCreate as ProductCreateSchema,
    ProductUpdate as ProductUpdateSchema,
)


@strawberry.experimental.pydantic.type(model=ProductSchema, all_fields=True)
class ProductType:
    pass


@strawberry.experimental.pydantic.input(model=ProductCreateSchema, all_fields=True)
class ProductCreateInput:
    pass


@strawberry.experimental.pydantic.input(model=ProductUpdateSchema, all_fields=True)
class ProductUpdateInput:
    pass


@strawberry.type
class ProductPagination(PaginatedResponse[ProductType]):
    pass
