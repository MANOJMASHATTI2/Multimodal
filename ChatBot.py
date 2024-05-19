import os
from dotenv import load_dotenv
import redis

# Load environment variables from .env file
load_dotenv()

# Debugging: Print environment variables
print("REDIS_URL:", os.getenv('REDIS_URL'))
print("OPENAI_API_KEY:", os.getenv('OPENAI_API_KEY'))

# Get Redis URL from environment variables
redis_url = os.getenv('REDIS_URL')

# Connect to Redis server
r = redis.Redis.from_url(redis_url)

# Test the connection
try:
    r.ping()
    print("Connected to Redis")
except redis.AuthenticationError as e:
    print(f"Authentication failed: {e}")
except redis.ConnectionError as e:
    print(f"Connection error: {e}")
