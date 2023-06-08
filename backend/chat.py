import openai
import json
import string

CACHE_FILE = "backend/cache.json"

# Loads cache from file. If it doesn't exists we create a new cache
try:
    with open(CACHE_FILE, 'r') as file:
        cache = json.load(file)
except FileNotFoundError:
    cache = {}

with open('hidden.txt') as file:
    openai.api_key = file.read()

def getResponse(message):

    cleaned_message = message.strip().lower().translate(str.maketrans('', '', string.punctuation))
    print(cleaned_message)
    if cleaned_message in cache:
        return cache[cleaned_message]
    
    messages = [{"role": "system", "content": "You are Sheldon Cooper and you should talk like him and your role is to give advice to students in building a personal portfolio for jobs and internships"}]
    messages.append({"role":"user", "content":message})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    text_reply = response["choices"][0]["message"]["content"]
    cache[cleaned_message] = text_reply

    with open(CACHE_FILE, 'w') as file:
        json.dump(cache, file)

    return text_reply