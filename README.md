# 🎭 Playwright Python Automation Framework

A modular UI and API test automation framework built with Playwright and Python, designed for enterprise web application testing.

---

## 🛠️ Tech Stack

![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)

---

## 📁 Project Structure
playwright-python-automation/
    │
    ├── tests/
    │   ├── ui/
    │   ├── api/
    │   └── data/
    ├── pages/
    │   ├── base_page.py
    │   ├── login_page.py
    │   └── dashboard_page.py
    ├── fixtures/
    │   └── conftest.py
    ├── utils/
    │   ├── api_client.py
    │   └── data_helpers.py
    ├── config/
    │   └── config.py
    ├── reports/
    ├── requirements.txt
    └── pytest.ini
    ---

## ⚙️ Setup & Installation

```bash
# Clone the repo
git clone https://github.com/Kirthika-Krishnan/playwright-python-automation.git
cd playwright-python-automation

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

---

## ▶️ Running Tests

```bash
# Run all tests
pytest

# Run UI tests only
pytest tests/ui/

# Run API tests only
pytest tests/api/

# Run with HTML report
pytest --html=reports/report.html
```

---

## 📊 Features

- ✅ Page Object Model (POM) design pattern
- ✅ UI, API and data validation tests
- ✅ Pytest fixtures for reusable setup/teardown
- ✅ Environment-based configuration
- ✅ HTML test reporting
- ✅ Headless and headed browser support

---

## 📫 Author

**Kirthika Navaneetha Krishnan**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kirthika-navaneetha-krishnan-99a989179/)
