import os
import pytest
from environment_variables_examples.core import load_env_vars


@pytest.fixture(scope="module")
def deployment_stage_env_var() -> pytest.fixture():
    os.environ["DEPLOYMENT_STAGE"] = "staging"
    return os.environ["DEPLOYMENT_STAGE"]


@pytest.fixture(scope="module")
def api_endpoint_env_var() -> pytest.fixture():
    os.environ["API_ENDPOINT"] = "https://api.TEST_URL2.com"
    return os.environ["API_ENDPOINT"]


@pytest.fixture(scope="module")
def account_id_env_var() -> pytest.fixture():
    os.environ["ACCOUNT_ID"] = "789"
    return os.environ["ACCOUNT_ID"]


def test_load_env_vars_fixtures(deployment_stage_env_var,
                                api_endpoint_env_var,
                                account_id_env_var) -> None:
    """
    Using Fixtures
    :return: None
    """
    expected_response = "The API endpoint `https://api.TEST_URL2.com` " \
                        "has been deployed to `staging` in Account # `789`"
    actual_response = load_env_vars()
    assert actual_response == expected_response


def test_load_env_vars_monkeypatch(monkeypatch) -> None:
    """
    Using Monkeypatch
    :return: None
    """
    monkeypatch.setenv("DEPLOYMENT_STAGE", "prod")
    monkeypatch.setenv("API_ENDPOINT", "https://api.TEST_URL3.com")
    monkeypatch.setenv("ACCOUNT_ID", "321")
    expected_response = "The API endpoint `https://api.TEST_URL3.com` " \
                        "has been deployed to `prod` in Account # `321`"
    actual_response = load_env_vars()
    assert actual_response == expected_response
