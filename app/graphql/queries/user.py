import strawberry
from typing import List, Optional
from app.services.user_service import UserService
from app.schemas.user import User as UserSchema
from ..types.user import UserType
from ..permissions import IsAuthenticated, IsAdmin


@strawberry.type
class UserQueries:
    @strawberry.field(permission_classes=[IsAuthenticated])
    def me(self, info: strawberry.Info) -> UserType:
        return UserType.from_pydantic(UserSchema.model_validate(info.context.user))

    @strawberry.field(permission_classes=[IsAdmin])
    def users(self, info: strawberry.Info) -> List[UserType]:
        user_service = UserService(info.context.db)
        users = user_service.get_all_users()
        return [
            UserType.from_pydantic(UserSchema.model_validate(user)) for user in users
        ]

    @strawberry.field(permission_classes=[IsAdmin])
    def user(self, info: strawberry.Info, user_id: int) -> Optional[UserType]:
        user_service = UserService(info.context.db)
        user = user_service.get_user_by_id(user_id)
        return UserType.from_pydantic(UserSchema.model_validate(user)) if user else None
