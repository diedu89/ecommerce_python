from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    category: Optional[str] = None
    image: Optional[str] = None
    stock: int = Field(ge=0, default=0)
    is_active: bool = True

    class Config:
        from_attributes = True


class ProductCreate(BaseModel):
    title: str
    price: float
    description: str
    category: str
    image: str
    stock: int
    is_active: bool = True


class ProductUpdate(ProductBase):
    title: Optional[str] = None
    price: Optional[float] = Field(gt=0, default=None)
    stock: Optional[int] = Field(ge=0, default=None)
    is_active: Optional[bool] = None


class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
