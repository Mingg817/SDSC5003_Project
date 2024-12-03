from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "SDSC5003"
    DATABASE_URL: str = "mysql+pymysql://root:123456@localhost:3306/SDSC5003"
    JWT_SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120


settings = Settings()  # type: ignore
