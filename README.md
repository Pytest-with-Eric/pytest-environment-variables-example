# PyTest Environment Variables Example

[//]: # (This repo contains the sample code for the article - [Save Money On You CI/CD Pipelines Using Pytest Parallel &#40;with Example&#41;]&#40;https://pytest-with-eric.com/pytest-best-practices/pytest-parallel/&#41;)


# Requirements
* Python (3.10.6)

Please install the dependencies via the `requirements.txt` file using 
```commandline
pip install -r requirements.txt
```
If you don't have Pip installed please follow instructions online on how to do it.

# How To Run the Unit Tests - Sequential
To run the Unit Tests, from the root of the repo run
```commandline
pytest ./tests/unit/
```

# How To Run the Unit Tests - Parallel using the `xdist` plugin
To run the Unit Tests, from the root of the repo run
```commandline
pytest ./tests/unit/ -v -s -n auto
```

If you have any questions about the project please raise an Issue on GitHub. 