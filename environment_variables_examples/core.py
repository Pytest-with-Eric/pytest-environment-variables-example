import os
from dotenv import load_dotenv

load_dotenv()


def load_env_vars() -> str:
    """
    Function to load and print environment variables
    :return: String containing env vars
    """
    account_id = os.getenv("ACCOUNT_ID")
    api_endpoint = os.getenv("API_ENDPOINT")
    deployment_stage = os.getenv("DEPLOYMENT_STAGE")
    return f"The API endpoint `{api_endpoint}` has been deployed to " \
           f"`{deployment_stage}` in Account # `{account_id}`"
