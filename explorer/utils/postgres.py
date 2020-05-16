from secrets import SecretManager
from dataclasses import dataclass


@dataclass
class PostgresCredentials:
    username: str
    password: str
    host: str
    port: int
    database: str


print(SecretManager("dev/guillaumelegoy").retrieve_secret())
