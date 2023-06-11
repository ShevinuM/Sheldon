from dotenv import load_dotenv
import os

# Load environment variables from a custom file
load_dotenv('../hidden.env')

# Access environment variables
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)