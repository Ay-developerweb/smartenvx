# smartenv/exceptions.py

class MissingEnvError(Exception):
    """Raised when a required environment variable is missing."""
    pass

class InvalidEnvTypeError(Exception):
    """Raised when a variable cannot be cast to the specified type."""
    pass
