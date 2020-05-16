import boto3
from botocore.exceptions import ClientError


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

    def retrieve_secret(self):
        try:
            return self._create_boto_client().get_secret_value(
                SecretId=self.secret_name
            )

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
