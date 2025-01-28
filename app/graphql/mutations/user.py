import strawberry
from ..types.user import UserType, UserCreateInput, UserUpdateInput
from app.services.user_service import UserService
from ..permissions import IsAdmin


@strawberry.type
class UserMutations:
    @strawberry.mutation
    def create_user(
        self, info: strawberry.Info, user_data: UserCreateInput
    ) -> UserType:
        user_service = UserService(info.context.db)
        user = user_service.create_user(user_data.to_pydantic())
        return UserType.from_pydantic(user)

    @strawberry.mutation(permission_classes=[IsAdmin])
    def update_user(
        self, info: strawberry.Info, user_id: int, user_data: UserUpdateInput
    ) -> UserType:
        user_service = UserService(info.context.db)
        user = user_service.update_user(user_id, user_data.to_pydantic())
        return UserType.from_pydantic(user)
