import sys
import os
from dotenv import load_dotenv

# Test 1: Verify if `python-dotenv` is installed and import works
try:
    from dotenv import load_dotenv
    print("Test 1: python-dotenv import: SUCCESS")
except ImportError:
    print("Test 1: python-dotenv import: FAILED")
    sys.exit(1)  # Exit if import fails

# Test 2: Check if dotenv works by loading the .flaskenv or .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
if not os.path.exists(dotenv_path):
    print("Test 2: .flaskenv file not found!")
    sys.exit(1)

load_dotenv(dotenv_path)  # Explicitly load .flaskenv
print("Test 2: dotenv loaded: SUCCESS")

# Test 3: Check if environment variables can be accessed
flask_app = os.getenv("FLASK_APP")
flask_env = os.getenv("FLASK_ENV")

# Print results of environment variable loading
if flask_app and flask_env:
    print("Test 3: Environment variables loaded:")
    print(f"    FLASK_APP: {flask_app}")
    print(f"    FLASK_ENV: {flask_env}")
else:
    print("Test 3: Environment variables not loaded correctly")
    sys.exit(1)  # Exit if variables are not set

# If all tests pass
print("\nAll tests passed successfully!")
