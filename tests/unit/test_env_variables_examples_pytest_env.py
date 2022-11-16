from environment_variables_examples.core import load_env_vars


def test_load_env_vars_using_pytest_env():
    """
    Using pytest_env and pytest.ini
    :return:
    """
    expected_response = "The API endpoint `www.test_api_endpoint.com` " \
                        "has been deployed to `dev2` in Account # `9876`"
    actual_response = load_env_vars()
    assert actual_response == expected_response
