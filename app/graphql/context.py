import strawberry
from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext

from app.api.v1.auth import get_current_user_optional
from app.db.session import get_db
from app.models.user import User


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
