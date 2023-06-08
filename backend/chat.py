import openai


with open('hidden.txt') as file:
    openai.api_key = file.read()

def getResponse(message):
    messages = [{"role": "system", "content": "You are Sheldon Cooper and you should talk like him and your role is to give advice to students in building a personal portfolio for jobs and internships"}]
    messages.append({"role":"user", "content":message})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    text_reply = response["choices"][0]["message"]["content"]
    print(text_reply)
    return text_reply