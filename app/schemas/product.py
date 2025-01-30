from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    title: str
    price: float = Field(gt=0)
    description: str
    category: str
    image: str
    stock: int
    is_active: bool = True

    class Config:
        from_attributes = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    title: Optional[str] = None
    price: Optional[float] = Field(gt=0, default=None)
    stock: Optional[int] = Field(ge=0, default=None)
    is_active: Optional[bool] = None


class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
