# Healthcare Claims UI Automation Framework

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-Ready-0E7FBF?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-Passing-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/SrinivasaraoThata/claims-ui-automation/actions)

## 🏥 Business Problem
The healthcare industry is plagued by manual claim processing errors, leading to multi-million dollar delays and member dissatisfaction. This project provides a **robust, automated solution** to ensure the integrity of the Member Portal, where patients track their claim status. By automating critical paths, we reduce human error and ensure that every member sees accurate, real-time data regarding their healthcare benefits.

---

## 🚀 Project Overview
This framework is a core component of the larger **[Claims-QA-Suite](https://github.com/SrinivasaraoThata/claims-qa-suite)** ecosystem—a comprehensive testing strategy for end-to-end healthcare automation. 

To demonstrate these capabilities in a secure, repeatable environment, we utilize **ParaBank** as a simulated Healthcare Member Portal. Using this enterprise-grade simulation allows for rigorous testing of complex claim logic, login security, and profile management without risking sensitive real-world healthcare data (PHI).

---

## ✨ Key Features
- **Page Object Model (POM)**: Engineered for maximum maintainability and cleaner test scripts.
- **Enterprise-Grade CI/CD**: Seamlessly integrated with GitHub Actions for automated regression testing on every push.
- **Scalable Architecture**: Support for parallel execution (`pytest-xdist`) and BDD patterns (`pytest-bdd`).
- **Deep Visibility**: Rich logging and support for Allure reporting to provide clear insights to stakeholders.
- **Code Excellence**: Strictly adheres to 10.00/10 `pylint` scores and `flake8` standards.

---

## 📂 Project Structure
```text
claims-ui-automation/
├── .github/workflows/   # Automated CI/CD pipelines
├── config/              # Centralized environment configuration
├── docs/                # Strategic documentation (Test Plan, RTM, etc.)
├── pages/               # Page Objects (POM design pattern)
├── tests/               # Automated Pytest test cases
├── utils/               # Shared logic and cross-functional helpers
├── conftest.py          # Global fixtures and browser setup
└── requirements.txt     # Standardized dependency list
```

---

## 📊 Strategic Documentation
For a deeper dive into the architecture and requirements, explore our **[docs/](docs/)** directory:
- [Business Problem Analysis](docs/business-problem.md)
- [Comprehensive Test Plan](docs/test-plan.md)
- [Requirements Traceability Matrix (RTM)](docs/rtm.md)

---

## 🛠️ Tech Stack & Prerequisites
- **Python 3.10+**: Core logic and scripting.
- **Selenium 4.x**: Direct browser interaction and automation.
- **Pytest**: The foundation for our test runner and reporting.
- **Chrome/Edge**: Supported browsers (runs headless in CI/CD).

---

## 🏃 Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/SrinivasaraoThata/claims-ui-automation.git
   cd claims-ui-automation
   ```
2. **Launch development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate # (On Windows: .\venv\Scripts\activate)
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Execute the suite**:
   ```bash
   pytest -v
   ```

---

## 👤 Author
**Srinivasa Rao Thata**  
*Senior QA Automation Engineer | 2026*
