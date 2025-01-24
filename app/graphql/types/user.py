import strawberry
from datetime import datetime
from typing import Optional
from app.schemas.user import (
    User as UserSchema,
    UserCreate as UserCreateSchema,
    UserUpdate as UserUpdateSchema,
)


@strawberry.experimental.pydantic.type(model=UserSchema, all_fields=True)
class UserType:
    pass


@strawberry.experimental.pydantic.input(model=UserCreateSchema, all_fields=True)
class UserCreateInput:
    pass


@strawberry.experimental.pydantic.input(model=UserUpdateSchema, all_fields=True)
class UserUpdateInput:
    pass
