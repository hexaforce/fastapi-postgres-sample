import json
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import BaseSettings
from pydantic import PostgresDsn
from pydantic import validator


class Settings(BaseSettings):
    APP_ENV: Optional[str] = None
    API_V1_STR: str = "/api"
    # API_V2_STR: str = "/api/v2"

    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_SERVER: Optional[str] = None
    POSTGRES_PORT: Optional[str] = "5432"
    POSTGRES_DB: Optional[str] = None

    NLUCLUSTER_SECRET: Optional[str] = None
    DATABASE_URI: List[Optional[PostgresDsn]] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> List[Any]:
        if isinstance(v, str):
            return v

        secret = values.get("NLUCLUSTER_SECRET")
        if secret is None:
            # localhost
            user = values.get("POSTGRES_USER")
            password = values.get("POSTGRES_PASSWORD")
            host = values.get("POSTGRES_SERVER")
            port = values.get("POSTGRES_PORT")
            db_name = values.get("POSTGRES_DB")
        else:
            # remote(AWS)
            secret_json = json.loads(secret)
            user = secret_json["username"]
            password = secret_json["password"]
            host = secret_json["host"]
            port = str(secret_json["port"])
            db_name = secret_json["dbname"]

        return [
            # MAIN DB
            PostgresDsn.build(
                scheme="postgresql",
                user=user,
                password=password,
                host=host,
                port=port,
                path=f"/{db_name}",
            ),
            # TEST DB
            PostgresDsn.build(
                scheme="postgresql",
                user=user,
                password=password,
                host=host,
                port=port,
                path=f"/{db_name}-test",
            ),
        ]

    SMTP_TLS: bool = True
    # SMTP_PORT: Optional[int] = None
    # SMTP_HOST: Optional[str] = None
    # SMTP_USER: Optional[str] = None
    # SMTP_PASSWORD: Optional[str] = None

    # EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    # EMAIL_TEMPLATES_DIR: str = "/app/app/utils/email-templates/build"

    # EMAILS_ENABLED: bool = False
    # @validator("EMAILS_ENABLED", pre=True)
    # def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
    #     return bool(
    #         values.get("SMTP_HOST")
    #         and values.get("SMTP_PORT")
    #         and values.get("EMAILS_FROM_EMAIL")
    #     )
    # EMAILS_FROM_NAME: Optional[str] = None
    # EMAILS_FROM_EMAIL: Optional[EmailStr] = None

    # class Config:
    #     case_sensitive = True


settings = Settings()
