# Integrating screenshots in Allure Report with Pytest and Selenium

This repository is a part of Allure Report documentation and contains code examples for integrating screenshots in Allure Report with Pytest and Selenium. You can find the original documentation:

- [English version](https://allurereport.org/docs/guides/pytest-selenium-screenshots/)
- [Spanish version](https://allurereport.org/es/docs/guides/pytest-selenium-screenshots//)

## Preparation

1. Make sure you have installed:

- [Python](https://www.python.org/downloads/) version 3.9 or higher
- [Allure Report](https://allurereport.org/docs/install/)

1. Clone the repository via HTTPS:

    ```shell
    git clone https://github.com/allure-examples/guide-pytest-selenium-screenshots.git
    ```

    or SSH:

    ```shell
    git clone git@github.com:allure-examples/guide-pytest-selenium-screenshots.git
    ```

1. In the shell of your choice, navigate to the repository directory:

    ```shell
    cd path/to/guide-pytest-selenium-screenshots
    ```

## Running code example

The repository provides with automatic scripts that install the virtual environment, necessary packages, and run the tests. Run the script correspondind to your operating system. For Linux and MacOS:

```
./run.sh
```

For OS Windows:

```shell
.\run.bat
```

Alternatively, create and activate Python virtual environment and install the packages manually:

```shell
python -m venv venv
source venv/bin/activate
pip install -m requirements.txt
```

After the installation, run:
```
pytest
```

## Run Allure Report

1. To start a local Allure Report server, in the project root directory run:

    ```shell
    allure serve -p <port-of-your-choice>
    ```

1. Browse Allure Report page on `http://127.0.0.1/<port-of-your-choice>`.