import strawberry
from typing import List, Optional
from app.services.product_service import ProductService
from app.schemas.product import Product as ProductSchema
from ..types.product import ProductType
from ..permissions import IsAuthenticated


@strawberry.type
class ProductQueries:
    @strawberry.field
    def products(self, info: strawberry.Info) -> List[ProductType]:
        product_service = ProductService(info.context.db)
        products = product_service.get_all_products()
        return [
            ProductType.from_pydantic(ProductSchema.model_validate(product))
            for product in products
        ]

    @strawberry.field
    def product(self, info: strawberry.Info, product_id: int) -> Optional[ProductType]:
        product_service = ProductService(info.context.db)
        product = product_service.get_product_by_id(product_id)
        return (
            ProductType.from_pydantic(ProductSchema.model_validate(product))
            if product
            else None
        )
