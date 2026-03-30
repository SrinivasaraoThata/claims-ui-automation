# Claims UI Automation Framework

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-Ready-0E7FBF?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-Passing-2088FF?logo=github-actions&logoColor=white)](https://github.com/SrinivasaraoThata/claims-ui-automation/actions)

## The Problem Space
Automating a healthcare portal isn't just about clicking buttons; it's about handling sensitive workflows without the luxury of real member data (PHI). I built this framework to solve three specific challenges:

1.  **Status Uncertainty**: Members often face delays or confusion regarding their claim status (Pending vs. Approved). This suite validates that the UI reflects the core business logic.
2.  **Data Consistency**: Ensuring that a claim submitted in one session is accurately reflected across the portal in the next.
3.  **Safe Simulation**: Using **ParaBank** as a sandbox to demonstrate high-coverage automation without the compliance risks of a real-world healthcare environment.

## Design Decisions & Patterns
I chose **Python + Selenium 4** for this project because of its industry-standard status and the improved stability of Selenium 4's relative locators and asynchronous handling.

*   **Page Object Model (POM)**: Every UI component is isolated into its own class. If an ID changes, we fix it in one file, not 50 tests.
*   **Wait Strategy over Implicit Waits**: I avoid `driver.implicitly_wait` in favor of per-element `WebDriverWait`. This prevents "false positives" and ensures the DOM is truly interactive before we fire an event.
*   **Root Cause Analysis (RCA)**: Integrated a `pytest` hook in `conftest.py` that automatically captures and saves screenshots of failing tests to the `screenshots/` directory for faster debugging.
*   **Environment Agnostic**: Configuration is externalized via `config.yaml`. This allows the suite to toggle between local development and headless CI/CD environments without any code changes.
*   **Scalable Execution**: Integrated `pytest-xdist` to cut down regression time. Even a small suite should be built to scale.

## Challenges & Lessons Learned
Real-world automation is never as clean as the documentation suggests. Here is how I solved the biggest hurdles:

*   **Solved Flaky Sessions**: ParaBank's session timeouts were inconsistent during long regression runs. I implemented a pre-test "Health Check" in the BasePage to ensure the user is still authenticated before proceeding with sensitive transactions.
*   **Tactical Synchronization**: Some pages in the simulated environment hang indefinitely. Moving to a more tactical `FluentWait` (ignoring `NoSuchElementException`) significantly reduced flakiness in the registration flow.
*   **Data Integrity (Re-runnable Tests)**: Testing account balances is tricky because the data changes as you interact with it. I implemented a "Relative Assertion" strategy where we capture the starting balance and verify the change, rather than hardcoding expected final values.

## Requirements Traceability Matrix (RTM)
| Requirement ID | Feature | Test Case | Complexity | Technical Notes |
|----------------|---------|-----------|------------|-----------------|
| **REQ-01** | User Auth | Login with Valid Credentials | Low | Standard POM implementation. |
| **REQ-02** | Accounts | Dashboard Data Validation | Medium | Uses Regex to scrub currency symbols before assertion. |
| **REQ-03** | Transfers | Funds Transfer Between Accounts | High | Requires "Session Health Check" to ensure login didn't drop mid-flow. |
| **REQ-04** | Services | Loan Request Submission | High | Challenge: Asynchronous success message; uses FluentWait. |

## Project Structure
```text
claims-ui-automation/
├── .github/      # CI/CD workflows (GitHub Actions)
├── config/       # Environment and browser settings
├── docs/         # Extended Docs: RTM (Requirements Matrix)
├── pages/        # Page Object classes (POM Pattern)
├── tests/        # The actual test scripts
├── utils/        # Generic helpers and logging
└── conftest.py   # Global fixtures and driver setup
```

## Getting Started
1. **Clone it**: `git clone https://github.com/SrinivasaraoThata/claims-ui-automation.git`
2. **Environment Setup**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Running Tests**:
   - **Full Regression**: `pytest -v` (Default is --headless=true for CI/CD)
   - **Parallel Execution (Fast)**: `pytest -n 3`
   - **Generate HTML Report**: `pytest --html=report.html`

> [!TIP]
> **CI/CD Note**: This project is configured to run in **headless mode** by default in GitHub Actions to optimize performance. You can toggle this in the `config/config.yaml`.

## Known Issues & Road Map
Even a mature suite has room for growth. Currently identifying:
- **Firefox Overlap**: Investigating a minor race condition when asserting "Loan Success" messages specifically in Firefox Headless mode; current workaround is a dynamic poll.
- **Data Cleanup**: Exploring a DB-level cleanup script to reset account balances post-regression to ensure the environment remains pristine.

## Traceability & Compliance
For a breakdown of how automation maps to business needs, see the [RTM (Requirements Traceability Matrix)](docs/rtm.md).

## Author
**Srinivasa Rao Thata**  
Senior QA Automation Engineer  
Python | Selenium | Pytest | CI/CD Implementation
