from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = "postgresql+asyncpg://postgres:####@localhost:5432/Shop"
    db_echo: bool = True


settings = Settings()


# DB_HOST = "localhost"
# DB_PORT = 5432
# DB_USER = "postgres"
# DB_PASS = ####
# DB_NAME = "Books"
