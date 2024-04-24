import os


def test_load_env_vars_pytest_env():
    assert os.environ["DEPLOYMENT_STAGE"] == "staging"
    assert os.environ["API_ENDPOINT"] == "https://api.staging.example.com"
    assert os.environ["ACCOUNT_ID"] == "56789"
