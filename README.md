# coffee-cart.app

A Python application for managing a coffee cart.

## Features

- Manage products and inventory
- Process orders
- Track sales

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/UA-4700-taqc/coffee-cart.app_py_s.git
   ```
2. **Navigate to the project directory:**
   ```
   cd coffee-cart.app_py_s
   ```
3. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
5. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env file with your actual test credentials
   ```

6. **Install pre-commit hooks (optional but recommended):**
   ```bash
   pre-commit install
   ```

### Environment Configuration

Create a `.env` file based on `.env.example` and configure:

```env
# User credentials for testing
BASE_URL=http://localhost:3000
IMPLICITLY_WAIT=5

```

## 🧪 Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_login.py

# Run tests with specific marker
pytest -m login

# Run tests with verbose output
pytest -v

# Run tests with Allure reporting
pytest --alluredir=allure-results
```
## License

This project is licensed under the MIT License.
```
This template provides a clear overview and instructions for your project.
