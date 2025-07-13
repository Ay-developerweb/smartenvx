<p align="center">
  <img src="logo.png" width="150" alt="smartenvx logo" />
</p>

# smartenvx

[![PyPI version](https://badge.fury.io/py/smartenvx.svg)](https://pypi.org/project/smartenvx/)

**Smart .env loader with validation, fallback values, and secure variable handling.**  
Simplify your environment variable management across any Python project with smart defaults, type conversion, required flags, and secure masking.

---

## 🚀 Features

- 📦 Load variables from a `.env` file
- 🔐 Secure environment variables (masked in logs)
- ✅ Required variable enforcement
- 🧠 Smart default values with type conversion
- 📜 Simple API for any Python project (CLI, backend, scripts, etc.)

---

## 📦 Installation

```bash
pip install smartenvx
```
---

## ⚡ Quick Usage
```python
from smartenvx import load_env, get_env, require_env, secure_env

load_env()  # Loads from .env

DEBUG = get_env("DEBUG", default=False, type=bool)
PORT = get_env("PORT", default=8000, type=int)
API_KEY = require_env("API_KEY")
DB_PASS = secure_env("DB_PASS")

print("DEBUG:", DEBUG)
print("DB_PASS (safe):", DB_PASS)
```
---
### 📄 .env Example
```ini
DEBUG=true
PORT=5000
API_KEY=supersecretkey
DB_PASS=sensitivepassword
```
---
### 📛 Exceptions
| Exception             | Raised When                                   |
| --------------------- | --------------------------------------------- |
| `MissingEnvError`     | A required or secure variable is not found    |
| `InvalidEnvTypeError` | Type conversion fails (e.g., `"abc"` → `int`) |
---
### 🔧 Supported Types
- str (default)

- int

- float

- bool (true, 1, yes, etc.)
---
### 🛡 Secure Variables
```python
password = secure_env("SECRET")
print(password)      # prints: ******
str(password)        # prints: ******
actual = password == "SECRET"  # ✅ True
```
---
### 📚 License
MIT License © 2025 Ayomide Adediran
https://github.com/Ay-developerweb/smartenvx

---
