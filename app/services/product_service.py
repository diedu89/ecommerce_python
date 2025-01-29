from sqlalchemy.orm import Session
from app.models.product import Product
from typing import List, Optional
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_products(self) -> List[Product]:
        return self.db.query(Product).filter(Product.is_active == True).all()

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        return self.db.query(Product).filter(Product.id == product_id).first()

    def create_product(self, product_data: ProductCreate) -> Product:
        product = Product(**product_data.model_dump())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update_product(
        self, product_id: int, product_data: ProductUpdate
    ) -> Optional[Product]:
        product = self.get_product_by_id(product_id)
        if not product:
            return None

        for key, value in product_data.model_dump(exclude_unset=True).items():
            setattr(product, key, value)

        self.db.commit()
        self.db.refresh(product)
        return product

    def delete_product(self, product_id: int) -> bool:
        product = self.get_product_by_id(product_id)
        if not product:
            return False

        product.is_active = False
        self.db.commit()
        return True
