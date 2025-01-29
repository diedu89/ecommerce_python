import strawberry
from typing import Optional
from app.services.product_service import ProductService
from app.schemas.product import Product as ProductSchema
from ..types.product import ProductType, ProductCreateInput, ProductUpdateInput
from ..permissions import IsAdmin


@strawberry.type
class ProductMutations:
    @strawberry.mutation(permission_classes=[IsAdmin])
    def create_product(
        self, info: strawberry.Info, product_data: ProductCreateInput
    ) -> ProductType:
        product_service = ProductService(info.context.db)
        product = product_service.create_product(product_data.to_pydantic())
        return ProductType.from_pydantic(ProductSchema.model_validate(product))

    @strawberry.mutation(permission_classes=[IsAdmin])
    def update_product(
        self, info: strawberry.Info, product_id: int, product_data: ProductUpdateInput
    ) -> Optional[ProductType]:
        product_service = ProductService(info.context.db)
        product = product_service.update_product(product_id, product_data.to_pydantic())
        return (
            ProductType.from_pydantic(ProductSchema.model_validate(product))
            if product
            else None
        )

    @strawberry.mutation(permission_classes=[IsAdmin])
    def delete_product(self, info: strawberry.Info, product_id: int) -> bool:
        product_service = ProductService(info.context.db)
        return product_service.delete_product(product_id)
