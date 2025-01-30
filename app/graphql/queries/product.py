import strawberry
from typing import Optional
from app.services.product_service import ProductService
from app.schemas.product import Product as ProductSchema
from ..types.product import ProductType, ProductPagination
from ..types.pagination import PaginationInput


@strawberry.type
class ProductQueries:
    @strawberry.field
    def products(
        self,
        info: strawberry.Info,
        pagination: PaginationInput = {"page": 1, "size": 10},
    ) -> ProductPagination:
        product_service = ProductService(info.context.db)
        paginated_products = product_service.get_all_products(pagination.to_pydantic())

        return ProductPagination(
            items=[
                ProductType.from_pydantic(ProductSchema.model_validate(product))
                for product in paginated_products.items
            ],
            total=paginated_products.total,
            page=paginated_products.page,
            size=paginated_products.size,
            pages=paginated_products.pages,
        )

    @strawberry.field
    def product(self, info: strawberry.Info, product_id: int) -> Optional[ProductType]:
        product_service = ProductService(info.context.db)
        product = product_service.get_product_by_id(product_id)
        return (
            ProductType.from_pydantic(ProductSchema.model_validate(product))
            if product
            else None
        )
