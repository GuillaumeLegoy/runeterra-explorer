import boto3
from botocore.exceptions import ClientError
from pathlib import Path
from dataclasses import dataclass, field
from contextlib import contextmanager
import git
import json


class SecretManager:
    def __init__(self, secret_name, region_name="us-east-1"):
        self.secret_name = secret_name
        self.region_name = region_name

    def _open_boto_session(self):
        return boto3.session.Session()

    def _create_boto_client(self):
        return self._open_boto_session().client(
            service_name="secretsmanager", region_name=self.region_name
        )

    @contextmanager
    def _boto_client_error_handler(self):
        try:
            yield
        except ClientError as e:
            if e.response["Error"]["Code"] == "DecryptionFailureException":
                raise e
            elif e.response["Error"]["Code"] == "InternalServiceErrorException":
                raise e
            elif e.response["Error"]["Code"] == "InvalidParameterException":
                raise e
            elif e.response["Error"]["Code"] == "InvalidRequestException":
                raise e
            elif e.response["Error"]["Code"] == "ResourceNotFoundException":
                raise e

    def retrieve_secret_string(self):
        with self._boto_error_handler():
            return json.loads(
                self._create_boto_client().get_secret_value(SecretId=self.secret_name)[
                    "SecretString"
                ]
            )


def get_repository_root_path() -> Path:
    return Path(git.Repo(".", search_parent_directories=True).working_tree_dir)


def get_cards_path() -> Path:
    return get_repository_root_path().joinpath("data/cards/en_us/data/set1-en_us.json")


def get_global_path() -> Path:
    return get_repository_root_path().joinpath(
        "data/global/en_us/data/globals-en_us.json"
    )


def get_dbt_seeds_path() -> Path:
    return get_repository_root_path().joinpath("explorer/dbt/data")


@dataclass
class ProjectPaths:
    root: Path = field(default_factory=get_repository_root_path)
    cards: Path = field(default_factory=get_cards_path)
    globals: Path = field(default_factory=get_global_path)
    dbt_seeds: Path = field(default_factory=get_dbt_seeds_path)
