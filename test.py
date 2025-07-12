# test.py

from smartenv import (
    load_env,
    get_env,
    require_env,
    secure_env,
    MissingEnvError,
    InvalidEnvTypeError
)

print("🔄 Loading .env file...")
try:
    load_env()
    print("✅ .env loaded.")
except FileNotFoundError as e:
    print("⚠️", e)

# Test get_env
try:
    print("\n🧪 Testing get_env...")
    debug = get_env("DEBUG", default=False, type=bool)
    print("DEBUG:", debug)

    port = get_env("PORT", default=8000, type=int)
    print("PORT:", port)

    name = get_env("APP_NAME", default="SmartApp")
    print("APP_NAME:", name)
except InvalidEnvTypeError as e:
    print("❌", e)

# Test require_env
try:
    print("\n🧪 Testing require_env...")
    api_key = require_env("API_KEY")
    print("API_KEY:", api_key)
except MissingEnvError as e:
    print("❌", e)

# Test secure_env
try:
    print("\n🧪 Testing secure_env...")
    db_pass = secure_env("DB_PASS")
    print("DB_PASS (hidden):", db_pass)
    print("Actual value (type check):", db_pass == "supersecret")  # Still works
except MissingEnvError as e:
    print("❌", e)
