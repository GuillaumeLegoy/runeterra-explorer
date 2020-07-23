import boto3
import json

from botocore.exceptions import ClientError
from explorer.logging import get_logger
from functools import wraps


logger = get_logger(__name__)


class CredentialsManager:
    def __init__(self, secret_name, region_name="us-east-1"):
        self.secret_name = secret_name
        self.region_name = region_name

    def _open_boto_session(self):
        return boto3.session.Session()

    def _create_boto_client(self):
        return self._open_boto_session().client(
            service_name="secretsmanager", region_name=self.region_name
        )

    def boto_error_handler(logger):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except ClientError as e:
                    if e.response["Error"]["Code"] == "DecryptionFailureException":
                        logger.exception(
                            f"Secrets Manager can't decrypt the protected secret text using the provided KMS key."
                        )
                        raise e

                    elif e.response["Error"]["Code"] == "InternalServiceErrorException":
                        logger.exception(f"An error occurred on the server side.")
                        raise e

                    elif e.response["Error"]["Code"] == "InvalidParameterException":
                        logger.exception(
                            f"You provided an invalid value for a parameter."
                        )
                        raise e

                    elif e.response["Error"]["Code"] == "InvalidRequestException":
                        logger.exception(
                            f"You provided a parameter value that is not valid for the current state of the resource."
                        )
                        raise e

                    elif e.response["Error"]["Code"] == "ResourceNotFoundException":
                        logger.info(f"We can't find the resource that you asked for.")
                        raise e

            return wrapper

        return decorator

    @boto_error_handler(logger)
    def retrieve_secret_string(self):
        return json.loads(
            self._create_boto_client().get_secret_value(SecretId=self.secret_name)[
                "SecretString"
            ]
        )
