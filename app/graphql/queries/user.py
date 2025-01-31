from typing import Optional

import strawberry

from app.schemas.user import User as UserSchema
from app.services.user_service import UserService

from ..permissions import IsAdmin, IsAuthenticated
from ..types.pagination import PaginationInput
from ..types.user import UserPagination, UserType


@strawberry.type
class UserQueries:
    @strawberry.field(permission_classes=[IsAuthenticated])
    def me(self, info: strawberry.Info) -> UserType:
        return UserType.from_pydantic(
            UserSchema.model_validate(info.context.user)
        )

    @strawberry.field(permission_classes=[IsAdmin])
    def users(
        self,
        info: strawberry.Info,
        pagination: PaginationInput = {"page": 1, "size": 10},
    ) -> UserPagination:
        user_service = UserService(info.context.db)
        paginated_users = user_service.get_all_users(pagination.to_pydantic())

        return UserPagination(
            items=[
                UserType.from_pydantic(UserSchema.model_validate(user))
                for user in paginated_users.items
            ],
            total=paginated_users.total,
            page=paginated_users.page,
            size=paginated_users.size,
            pages=paginated_users.pages,
        )

    @strawberry.field(permission_classes=[IsAdmin])
    def user(self, info: strawberry.Info, user_id: int) -> Optional[UserType]:
        user_service = UserService(info.context.db)
        user = user_service.get_user_by_id(user_id)
        return (
            UserType.from_pydantic(UserSchema.model_validate(user))
            if user
            else None
        )
