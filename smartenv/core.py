# smartenv/core.py

import os
from pathlib import Path
from dotenv import load_dotenv

from .exceptions import MissingEnvError, InvalidEnvTypeError
from .utils import str_to_bool

__all__ = ['get_env', 'require_env', 'secure_env', 'load_env']

def load_env(path=None):
    """Auto-load environment variables from a .env file."""
    env_path = Path(path) if path else Path('.') / '.env'
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
    else:
        raise FileNotFoundError(f".env file not found at: {env_path}")

def get_env(key, default=None, type=str):
    """Get environment variable with optional default and type conversion."""
    value = os.getenv(key, default)
    try:
        if value is not None:
            if type == bool:
                return str_to_bool(value)
            return type(value)
    except (ValueError, TypeError):
        raise InvalidEnvTypeError(
            f"Environment variable '{key}' cannot be converted to {type.__name__}"
        )
    return value

def require_env(key, type=str):
    """Ensure the required environment variable exists, or raise an error."""
    value = os.getenv(key)
    if value is None:
        raise MissingEnvError(f"Required environment variable '{key}' is missing.")
    return get_env(key, type=type)

class SecureStr(str):
    def __str__(self):
        return "******"
    def __repr__(self):
        return "******"

def secure_env(key):
    """Get sensitive environment variable (masked in logs/print)."""
    value = os.getenv(key)
    if value is None:
        raise MissingEnvError(f"Secure environment variable '{key}' is missing.")
    return SecureStr(value)
