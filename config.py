from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Function to safely get an integer from environment variable
def get_env_int(var_name):
    value = getenv(var_name)
    if value is None:
        raise ValueError(f"The environment variable '{var_name}' must be set.")
    return int(value)

# Load environment variables
API_ID = get_env_int("API_ID")
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = get_env_int("OWNER_ID")
MONGO_DB_URI = getenv("MONGO_DB_URI")
MUST_JOIN = getenv("MUST_JOIN", None)

# Optional: Log the loaded values for debugging
print(f"Loaded configuration: API_ID={API_ID}, BOT_TOKEN={BOT_TOKEN}, OWNER_ID={OWNER_ID}")
