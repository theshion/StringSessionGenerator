from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to safely get an integer from environment variable
def get_env_int(var_name):
    value = getenv(var_name)
    if value is None:
        raise ValueError(f"The environment variable '{var_name}' must be set.")
    return int(value)

# Load required environment variables with error handling
try:
    API_ID = get_env_int("API_ID")
    API_HASH = getenv("API_HASH")
    if API_HASH is None:
        raise ValueError("The environment variable 'API_HASH' must be set.")
    
    BOT_TOKEN = getenv("BOT_TOKEN")
    if BOT_TOKEN is None:
        raise ValueError("The environment variable 'BOT_TOKEN' must be set.")

    OWNER_ID = get_env_int("OWNER_ID")
    
    MONGO_DB_URI = getenv("MONGO_DB_URI")
    if MONGO_DB_URI is None:
        raise ValueError("The environment variable 'MONGO_DB_URI' must be set.")

    MUST_JOIN = getenv("MUST_JOIN", None)

    # Optional: Log the loaded values for debugging (exclude sensitive data)
    print("Loaded configuration: API_ID={}, BOT_TOKEN={}, OWNER_ID={}".format(API_ID, BOT_TOKEN, OWNER_ID))

except ValueError as e:
    print(f"Configuration error: {e}")
    exit(1)  # Exit the script with an error code
