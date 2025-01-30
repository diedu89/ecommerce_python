import math
from sqlalchemy.orm import Session
from typing import Optional
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, User as UserSchema
from app.schemas.pagination import PaginationParams, PaginatedResponse
from app.core.security import get_password_hash


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(
        self, pagination: Optional[PaginationParams] = PaginationParams(page=1, size=10)
    ) -> PaginatedResponse[UserSchema]:

        query = self.db.query(User).filter(User.is_active == True)

        # Get total count
        total = query.count()

        # Calculate total pages
        total_pages = math.ceil(total / pagination.size)

        # Apply pagination
        users = (
            query.offset((pagination.page - 1) * pagination.size)
            .limit(pagination.size)
            .all()
        )

        return PaginatedResponse(
            items=users,
            total=total,
            page=pagination.page,
            size=pagination.size,
            pages=total_pages,
        )

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user_data: UserCreate) -> User:
        hashed_password = get_password_hash(user_data.password)
        user = User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=hashed_password,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            is_superuser=user_data.is_superuser,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
