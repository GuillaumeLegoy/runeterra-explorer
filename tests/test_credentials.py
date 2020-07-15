from explorer.credentials import CredentialsManager
import pytest


def test_retrieve_secret_string():
    credentials_client = CredentialsManager("dev/test")

    assert credentials_client.retrieve_secret_string() == {
        "username": "test_user_name",
        "password": "test_password",
        "engine": "postgres",
        "host": "test_host",
        "port": 5432,
        "dbInstanceIdentifier": "",
        "database": "test_database",
    }


def test_wrong_secret_spelling():
    credentials_client = CredentialsManager("wrong_secret")

    with pytest.raises(Exception) as excinfo:
        credentials_client.retrieve_secret_string()

    assert "Secrets Manager can't find the specified secret" in str(excinfo.value)
