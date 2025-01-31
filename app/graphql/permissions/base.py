import typing

import strawberry
from strawberry.permission import BasePermission


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    def has_permission(
        self, source: typing.Any, info: strawberry.Info, **kwargs
    ) -> bool:
        return hasattr(info.context, "user") and info.context.user is not None
