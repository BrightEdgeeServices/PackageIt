from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GH_APP_ACCESS_TOKEN_HDT: str = ""
    PYPI_API_TOKEN_PROD: str = ""
    PYPI_API_TOKEN_TEST: str = ""
    READTHEDOCS_TOKEN: str = ""


def get_settings() -> Settings:
    return Settings()
    # pass
