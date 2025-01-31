import strawberry

from app.schemas.user import User as UserSchema
from app.schemas.user import UserCreate as UserCreateSchema
from app.schemas.user import UserUpdate as UserUpdateSchema

from .pagination import PaginatedResponse


@strawberry.experimental.pydantic.type(model=UserSchema, all_fields=True)
class UserType:
    pass


@strawberry.experimental.pydantic.input(
    model=UserCreateSchema, all_fields=True
)
class UserCreateInput:
    pass


@strawberry.experimental.pydantic.input(
    model=UserUpdateSchema, all_fields=True
)
class UserUpdateInput:
    pass


@strawberry.type
class UserPagination(PaginatedResponse[UserType]):
    pass
