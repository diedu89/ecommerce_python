import strawberry
from typing import List, Optional
from ..types.user import UserType
from ..context import GraphQLContext
from app.services.user_service import UserService
from app.schemas.user import User as UserSchema


@strawberry.type
class UserQueries:
    @strawberry.field
    def users(self, info: strawberry.Info) -> List[UserType]:
        user_service = UserService(info.context.db)
        users = user_service.get_all_users()
        return [
            UserType.from_pydantic(UserSchema.model_validate(user)) for user in users
        ]

    @strawberry.field
    def user(self, info: strawberry.Info, user_id: int) -> Optional[UserType]:
        user_service = UserService(info.context.db)
        user = user_service.get_user_by_id(user_id)
        return UserType.from_pydantic(UserSchema.model_validate(user)) if user else None
