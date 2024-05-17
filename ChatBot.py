import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
redis_url = os.getenv('REDIS_URL')

# Now you can use these variables in your code
print(f"OpenAI API Key: {openai_api_key}")
print(f"Redis URL: {redis_url}")
