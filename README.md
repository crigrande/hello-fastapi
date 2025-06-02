# Hello from FastAPI

This is a simple application that returns a welcome message from a parameter in the browser.

You can access the official FastAPI documentation [here](https://fastapi.tiangolo.com).

## Requirements

* Python 3.10+
* Virtual environment - It is advised to use a virtual environment at your choice to isolate requirements from the ones of the system.

## Installation

1. Clone this repo in any place in your local machine.
2. Create a virtual environment and activate it.
3. Install the requirements by running `pip install -e .`. The reason for this its because we use the `pyproject.toml` to manage our requirements.
4. Time to start the project:
    1. `cd` to `src/`;
    2. Start the development server: `fastapi dev`.

## Test the endpoint

Once the [installation](#installation) is setup and you have your development server up and running, you can now run:

* `http://127.0.0.1:8000/<A STRING>`, for example `http://127.0.0.1:8000/peter`.

You can also access the `swagger` by running:

* `http://127.0.0.1:8000/docs`.


Enjoy 🚀
