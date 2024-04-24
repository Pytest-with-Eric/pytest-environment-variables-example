# Pytest Environment Variables Example

This repo contains the sample code for the article - [3 Simple Ways To Define Environment Variables In Pytest](https://pytest-with-eric.com/pytest-best-practices/pytest-environment-variables/)


# Requirements
* Python (3.12)

Please install the dependencies via the `requirements.txt` file using 
```commandline
pip install -r requirements.txt
```
If you don't have Pip installed please follow instructions online on how to do it.

# How To Run the Unit Tests
To run the Unit Tests, from the root of the repo run
```commandline
pytest
```

**Note - Please run one test at a time to see the output as `pytest.ini` will override environment variables defined in `.env` files.**

If you have any questions about the project please raise an Issue on GitHub. 