from pydantic import BaseSettings   

_PREFIX = "DATA_SERVICE_"


class Service(BaseSettings):
    host: str
    port: int
    
    class Config:
        env_prefix: str = _PREFIX
    

class Postgres(BaseSettings):
    db_name: str
    user: str
    password: str
    host: str
    port: int

    class Config:
        env_prefix: str = _PREFIX + "POSTGRES_"

