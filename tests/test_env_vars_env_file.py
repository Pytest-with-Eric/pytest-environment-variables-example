import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env


def test_env_vars_from_env_file():
    assert os.environ["DEPLOYMENT_STAGE"] == "dev"
    assert os.environ["API_ENDPOINT"] == "https://api.dev.example.com"
    assert os.environ["ACCOUNT_ID"] == "987654321"
