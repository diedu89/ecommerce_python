from .base import IsAuthenticated


class IsAdmin(IsAuthenticated):
    message = "Admin access required"

    def has_permission(self, source, info, **kwargs):
        is_auth = super().has_permission(source, info, **kwargs)
        return is_auth and info.context.user.is_superuser
