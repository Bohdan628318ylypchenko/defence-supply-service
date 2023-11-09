from pydantic import BaseSettings   

_PREFIX = "ADMIN_SERVICE_"


class Service(BaseSettings):
    host: str
    port: int
    
    class Config:
        env_prefix: str = _PREFIX
    

class Postgres(BaseSettings):
    postgres_db_name: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int

    class Config:
        env_prefix: str = _PREFIX

