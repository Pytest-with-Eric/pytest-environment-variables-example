import os

# Manually Define Env Variables in Test
os.environ["DEPLOYMENT_STAGE"] = "prod"
os.environ["API_ENDPOINT"] = "https://api.prod.example.com"
os.environ["ACCOUNT_ID"] = "123456789"


def test_load_env_vars():
    assert os.environ["DEPLOYMENT_STAGE"] == "prod"
    assert os.environ["API_ENDPOINT"] == "https://api.prod.example.com"
    assert os.environ["ACCOUNT_ID"] == "123456789"
