# Bookcart-Test_project - Automated Smoke Tests for Bookcart app 
Bookcart app is deployed here: (https://bookcart.azurewebsites.net/)
## Overview

This repository contains automated smoke tests for the [Name of Web Application Tested] application. The tests are written in Python using the `pytest` framework and `Selenium` for web browser automation.

The goal of these smoke tests is to perform a quick, high-level verification of the most critical functionalities (e.g., login, registration, core feature usage) to ensure the application is stable and usable after a build or deployment.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1.  **Python:** Version 3.8 or higher is recommended. You can download it from [python.org](https://www.python.org/downloads/). Verify installation by running `python --version` or `python3 --version` in your terminal.
2.  **pip:** Python's package installer. It usually comes with Python. Verify by running `pip --version` or `pip3 --version`.
3.  **Git:** For cloning the repository. Download from [git-scm.com](https://git-scm.com/).
4.  **Web Browser:** A modern web browser like Chrome, Firefox, or Edge. Google Chrome is recommended.
5.  **WebDriver:** Selenium requires a specific WebDriver executable that matches your browser type and version.
    *   **Why?** WebDriver acts as a bridge between your Selenium script and the browser, allowing the script to control the browser's actions.
    *   **Download:**
        *   **ChromeDriver:** [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) (Matches Chrome version)
        *   **GeckoDriver:** [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases) (Matches Firefox version)
        *   **Edge WebDriver:** [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) (Matches Edge version)
    *   **Setup:** After downloading, you **must** either:
        *   Place the WebDriver executable file in a directory that is part of your system's `PATH` environment variable.
        *   *Or*, specify the path to the executable directly in your test script's Selenium WebDriver initialization code (less common for shared projects).
        *   *Or*, consider using a library like `webdriver-manager` (see Dependencies section) which can automatically download and manage WebDriver executables.

## Setup Instructions

Follow these steps to set up the project environment:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/aljaljak2/Bookcart-Test_project] 
    cd [repository-folder-name]
    ```


2.  **Create a Virtual Environment:** (Highly Recommended)
    This isolates project dependencies from your global Python installation.
    ```bash
    # On Windows
    python -m venv venv

    # On macOS/Linux
    python3 -m venv venv
    ```
    This creates a `venv` folder in your project directory.

3.  **Activate the Virtual Environment:**
    You need to activate the environment each time you work on the project in a new terminal session.
    ```bash
    # On Windows (cmd.exe)
    venv\Scripts\activate.bat

    # On Windows (PowerShell)
    .\venv\Scripts\Activate.ps1
    # (If you encounter script execution policy issues, you might need to run: Set-ExecutionPolicy RemoteSigned -Scope Process)

    # On macOS/Linux (bash/zsh)
    source venv/bin/activate
    ```
    Your terminal prompt should now be prefixed with `(venv)`.

4.  **Install Dependencies:**
    Install all the required Python libraries listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

## Generating/Updating `requirements.txt`

The `requirements.txt` file lists all the Python packages needed for this project. If you add new dependencies or want to ensure it reflects your current working environment:

1.  Make sure your virtual environment (`venv`) is activated.
2.  Install any necessary packages using `pip install <package_name>`.
3.  Run the following command **in the root directory of the project** to generate/update the file:
    ```bash
    pip freeze > requirements.txt
    ```
4.  Commit the updated `requirements.txt` file to the repository.

**Core Dependencies likely needed in `requirements.txt`:**

*   `pytest`: The testing framework used to discover and run tests.
*   `selenium`: The library used for browser automation.
*   *(Optional)* `webdriver-manager`: If you choose to use it for automatic WebDriver downloading.

Your generated `requirements.txt` will include these and any other libraries they depend on, along with their specific versions (e.g., `pytest==7.4.0`, `selenium==4.11.2`).

## Running the Tests

1.  Ensure your virtual environment (`venv`) is **activated**.
2.  Ensure the appropriate **WebDriver** is installed and accessible (either in your `PATH` or managed automatically).
3.  Navigate to the root directory of the project in your terminal.
4.  Run pytest:
    ```bash
    pytest
    ```
    Pytest will automatically discover and run tests (files typically named `test_*.py` or `*_test.py`, and functions/methods named `test_*`).

5.  **Running with More Detail (Verbose):**
    To see the name of each test being run along with its status (PASSED/FAILED/SKIPPED):
    ```bash
    pytest -v
    ```

6.  **(Optional) Running Specific Tests:**
    You can run specific files or tests using markers or keywords (`-k` flag).
    ```bash
    # Run tests only in a specific file
    pytest tests/test_smoke.py -v

    # Run tests with "login" in their name
    pytest -k login -v
    ```

## Test Documentation

Manual test cases (including positive, negative, and the selection for smoke tests) can be found in:

*   `[Path/To/Your/Test/Case/Document.md]` (or `.pdf`, `.xlsx`, etc. - **Replace this placeholder**)

## Bug Reporting

Bugs found during testing (both manual and automated) are tracked using GitHub Issues for this repository.

*   View existing bugs or report new ones here:(https://github.com/aljaljak2/Bookcart-Test_project/issues)
