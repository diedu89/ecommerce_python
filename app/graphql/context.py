import strawberry
from typing import Any
from sqlalchemy.orm import Session
from fastapi import Depends
from strawberry.fastapi import BaseContext
from app.db.session import get_db


class GraphQLContext(BaseContext):
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db


async def get_context(
    context: GraphQLContext = Depends(GraphQLContext),
) -> strawberry.Info:
    return context
