from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = "postgresql+asyncpg://postgres:1884@localhost:5432/Shop"
    db_echo: bool = True


settings = Settings()


# DB_HOST = "localhost"
# DB_PORT = 5432
# DB_USER = "postgres"
# DB_PASS = 1884
# DB_NAME = "Books"
