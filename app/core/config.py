from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI E-commerce"
    DATABASE_URL: str = "sqlite:///./ecommerce.db"
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()
