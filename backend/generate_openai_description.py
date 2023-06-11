from dotenv import load_dotenv
import os
import openai

# Load environment variables from a custom file
load_dotenv('hidden.env')

# Access environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_openai_description(userDescription):
    messages = [{"role": "system", "content": "You will be given a description of a tech project or job and you should rewrite the description in a more professional way including keywords"}]
    messages.append({"role":"user", "content":userDescription})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    reply = response["choices"][0]["message"]["content"]

    return reply