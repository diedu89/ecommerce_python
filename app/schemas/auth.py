from pydantic import BaseModel


class TokenData(BaseModel):
    user_id: int | None = None


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    email: str
    password: str
