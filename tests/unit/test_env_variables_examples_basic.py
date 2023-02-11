import os
from environment_variables_examples.core import load_env_vars


def test_load_env_vars() -> None:
    """
    Basic
    :return:
    """
    actual_response = load_env_vars()
    expected_response = "The API endpoint `https://api.TEST_URL.com` " \
                        "has been deployed to `prod` in Account # `123456789`"
    assert actual_response == expected_response


def test_load_env_vars_define_in_test() -> None:
    """
    Using os.environ
    :return: None
    """
    os.environ["DEPLOYMENT_STAGE"] = "dev"
    os.environ["API_ENDPOINT"] = "https://api.TEST_URL1.com"
    os.environ["ACCOUNT_ID"] = "123"
    expected_response = "The API endpoint `https://api.TEST_URL1.com` " \
                        "has been deployed to `dev` in Account # `123`"
    actual_response = load_env_vars()
    assert actual_response == expected_response
