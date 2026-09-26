# Python Selenium Pytest Framework Demo

A starter repository for exploring how to design and implement an automated test framework with Python, Selenium, and Pytest. The project layout separates reusable framework code from page objects, test data, and tests so it can grow beyond a collection of one-off scripts.

> **Status:** This repository currently provides the directory scaffold. Framework modules, sample tests, dependency files, and Pytest configuration still need to be implemented.

## Goals

- Demonstrate a maintainable structure for UI, API, database, and ETL tests.
- Keep browser and other infrastructure setup out of individual test cases.
- Encourage reusable page objects, locators, test data, and shared utilities.
- Provide a starting point that can be adapted to a real application and CI pipeline.

## Project Layout

| Directory | Intended purpose |
| --- | --- |
| `core/` | Shared framework code, including API, database, driver, ETL, exception, and utility modules. |
| `pages/` | Page objects and reusable UI components. |
| `locators/` | Centralized selectors used by page objects. |
| `tests/ui/` | Browser-based UI tests. |
| `tests/api/` | API tests. |
| `tests/db/` | Database tests. |
| `tests/etl/` | ETL tests. |
| `test_data/` | Input data and fixtures grouped by test area. |
| `config/` | Environment and framework configuration. |
| `api_resources/` | API schemas, payloads, or other API test resources. |
| `ci/` | Continuous-integration configuration and scripts. |
| `docker/` | Docker-related files for repeatable test environments. |
| `reports/` | Generated test reports. |
| `logs/` | Generated runtime and test logs. |

These directories describe the intended organization; not all areas are implemented yet.

## Getting Started

### Prerequisites

- Python 3.10 or newer (adjust this to match the version selected for the project).
- A supported browser for UI testing, such as Chrome or Firefox.
- Git.

Selenium's driver setup depends on the Selenium version and browser environment. Use Selenium Manager where supported, or configure a compatible browser driver as part of your environment setup.

### Create an environment

From the repository root, create and activate a virtual environment.

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the initial test dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install pytest selenium
```

Once dependency management is added to the repository, install from its committed dependency file instead.

## Running Tests

Run the complete Pytest suite from the repository root:

```bash
python -m pytest -v
```

Run one test area while developing:

```bash
python -m pytest tests/ui -v
python -m pytest tests/api -v
```

There are no tests in the scaffold yet, so these commands will not exercise framework behavior until tests are implemented.

## Suggested First Implementation Steps

1. Add a dependency file and a Pytest configuration for shared options and markers.
2. Implement environment configuration and a browser driver fixture with reliable cleanup.
3. Add a base page object and one page object with its locators.
4. Write a small UI test, then add reporting and CI execution as needed.

Keep credentials and environment-specific secrets out of source control. Load them from environment variables or a local, ignored configuration file.
