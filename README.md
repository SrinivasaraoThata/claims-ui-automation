# Healthcare Claims UI Automation Framework

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.x-green.svg)
![Pytest](https://img.shields.io/badge/pytest-ready-brightgreen.svg)
![GitHub Actions](https://github.com/SrinivasaraoThata/claims-ui-automation/actions/workflows/ui-tests.yml/badge.svg)

A professional-grade UI automation framework built with Python, Selenium 4, and Pytest. This suite is designed to validate the **Healthcare Member Portal (ParaBank)** with a focus on claim status verification, secure login, and member profile management.

---

## 🚀 Key Features

- **Page Object Model (POM)**: Robust and maintainable architecture separating page logic from test scripts.
- **CI/CD Integrated**: Fully automated pipeline via GitHub Actions for continuous quality assurance.
- **Reporting & Logging**: Comprehensive session logs and support for Allure reporting.
- **Code Quality**: Enforced high standards using `pylint` and `flake8` (rated 10/10).
- **Scalable Design**: Support for parallel execution and BDD (Behavior Driven Development) patterns.

---

## 📂 Project Structure

```text
claims-ui-automation/
├── .github/workflows/   # CI/CD pipeline definitions
├── config/              # YAML configuration files
├── docs/                # Business & technical documentation
├── pages/               # POM Page Classes
├── tests/               # Pytest Test Cases
├── utils/               # Shared helper functions & utilities
├── conftest.py          # Pytest fixtures & browser setup
└── requirements.txt     # Project dependencies
```

---

## 🛠️ Prerequisites

- **Python**: 3.10 or higher
- **Chrome Browser**: Latest version for headless execution
- **ChromeDriver**: Managed automatically by Selenium 4 Manager

---

## 🏃 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SrinivasaraoThata/claims-ui-automation.git
   cd claims-ui-automation
   ```

2. **Setup virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests**:
   ```bash
   # Run all tests
   pytest

   # Run with specific configuration
   pytest --maxfail=1 --disable-warnings
   ```

---

## 📊 Documentation

For detailed architecture and strategy, please refer to the [docs/](docs/) directory:
- [Business Problem Analysis](docs/business-problem.md)
- [Test Plan & Strategy](docs/test-plan.md)
- [Requirements Traceability Matrix (RTM)](docs/rtm.md)

---

## 👤 Author
- **Srinivasa Rao Thata** (2026)
