import strawberry
from typing import Any
from sqlalchemy.orm import Session
from fastapi import Depends
from strawberry.fastapi import BaseContext
from app.models.user import User
from app.db.session import get_db
from app.api.v1.auth import get_current_user_optional


class GraphQLContext(BaseContext):
    def __init__(
        self,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user_optional),
    ):
        self.db = db
        self.user = current_user


async def get_context(
    context: GraphQLContext = Depends(GraphQLContext),
) -> strawberry.Info:
    return context
