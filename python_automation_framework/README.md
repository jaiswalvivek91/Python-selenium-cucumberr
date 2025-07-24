
# ✅ Python Automation Framework – UI, API, DB (BDD + Selenium + Allure)

> 💡 Robust, modular automation framework built using Python, Selenium, Behave (BDD), MySQL, and Allure reporting.  
> Handles UI, API, and DB testing end-to-end with tagging, environment support, custom drivers, reusable actions, and validations.

---

## 📁 Folder Structure

```
automation_framework/
├── api/                  # API client logic (GET/POST etc)
├── config/               # config.ini + config_manager.py
├── database/             # DBClient for MySQL (previously db/)
├── features/             # All Behave feature files (.feature)
├── pages/                # Page Object Models (LoginPage, BasePage)
├── schemas/              # API JSON schema files for validation
├── steps/                # Step definitions for BDD scenarios
├── utility/              # Reusable actions + validators
├── reports/              # Allure results + reports (timestamped)
├── driver_manager        # DriverManager for Chrome/Firefox/Edge
├── environment.py        #  hooks (e.g. before_scenario)
├── requirements.txt      #  all the required libraries
├── .gitlab-ci.yml        #  to run the script in gitlab ( will be updated later )
└── test_runner.py        # CLI runner with tagging + allure
```

---

## ⚙️ Technologies Used

| Layer             | Tool                               |
|------------------|------------------------------------|
| 🧪 BDD Framework   | Behave (Cucumber-like Gherkin)     |
| 🌐 UI Automation  | Selenium WebDriver                 |
| 📡 API Testing    | requests + stepdefs                |
| 🧮 DB Access      | mysql-connector-python             |
| 📊 Reporting      | Allure with timestamped reports    |
| 🔀 Config Mgmt     | config.ini + ConfigManager         |
| 💻 Driver Setup   | webdriver-manager + DriverManager  |

---

## 🚦 Setup Instructions

### Step 1: Create & activate virtualenv

```
python -m venv .venv
source .venv/bin/activate   # on Mac      
.venv\Scripts\activate   # on Windows
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Edit config file

📄 config/config.ini

```
[DEFAULT]
base_url = https://the-internet.herokuapp.com
browser = chrome
headless = false
window_size = 1920x1080
implicit_wait = 10

[MYSQL]
host = localhost
user = root
password = your_password
database = test_db
port = 3306

[API]
base_api_url = https://jsonplaceholder.typicode.com
timeout = 30
```

---

## 🚀 Run Tests

### ✅ All tests

```
python test_runner.py
```

### ✅ Run by tag (bdd style)

```
python test_runner.py --tags @ui
python test_runner.py --tags @api
python test_runner.py --tags @db
```

---

## 🏷️ Behave Tag Reference

| Tag         | Description                      |
|-------------|----------------------------------|
| @ui         | UI tests via Selenium            |
| @api        | API GET/POST tests               |
| @postApi    | API tests with schema validation |
| @db         | MySQL DB query validations       |

---


## 🧰 Utilities Overview

📁 Located in: `utility/`

This folder includes all reusable helper modules across UI, API, and DB test layers.

| File name             | Purpose                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| `actions.py`          | Generic browser actions (safe_click, send_keys, scroll, JS, dropdowns) |
| `apivalidations.py`   | API response assertions, JSON field checks, JSON schema validation      |
| `dbvalidations.py`    | Checks on DB query results (e.g. value present, count > expected, etc.) |
| `helpers.py`          | Cross-cut helper functions used in step definitions across layers       |
| `wait_utils.py`       | Explicit wait logic for UI: visible, clickable, present, etc.           |

✅ These modules are used by step definitions and page objects to keep logic clean and DRY (Don’t Repeat Yourself).

---

## 🧪 Test Framework Configuration: behave.ini

📄 File: behave.ini (located in project root)

This configures global Behave options so you don’t have to specify them repeatedly on the command line.

Example:

```
[behave]
paths = features
format = pretty
no_color = false
wip = false
show_skipped = true
junit = yes
```

✅ This ensures consistent discovery of `.feature` files, well-formatted output, and enables reruns or report generation.

---

## ⚙️ CI/CD Integration: .gitlab-ci.yml

📄 File: .gitlab-ci.yml

This file defines your GitLab CI pipeline and automates execution of your automation framework on every push or merge request.
It will be modified at later stage

```

## 📊 Allure Reports

1. Automatically generated with each run into:
   ```
   reports/allure-results-
   reports/allure-report-
   ```

2. View report:

```
allure open reports/allure-report-20250724_012345 --- example
```

> ✅ Requires Allure CLI:
- macOS: `brew install allure`
- Windows: via Chocolatey or Scoop

---

## 🔧 Requirements Summary

```
behave==1.2.6
selenium==4.18.0
allure-behave==2.13.5
requests==2.32.3
pymysql==1.1.0
mysql-connector-python==8.4.0
python-dotenv==1.0.1
webdriver-manager==4.0.2
configparser==6.0.0
jsonschema>=4.0.0
```

---

## ✅ What's Working

- ✅ Behave BDD for test writing
- ✅ Custom driver setup via config.ini
- ✅ UI automation via Page Objects
- ✅ API automation (GET + POST)
- ✅ JSON Schema validation
- ✅ DB query validations (MySQL)
- ✅ Tags to isolate @ui / @api / @db
- ✅ Allure results + viewer
- ✅ Modular & scalable folder structure

---

## 🙌 Author

**Vivek Jaiswal**  
Framework designed with extensibility for CI/CD, Allure Analytics, and real-world applications.

---
```
