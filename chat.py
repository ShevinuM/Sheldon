# This code contains snippets from the open-source repository "https://github.com/patrickloeber/pytorch-chatbot.git
# Original authors: Patrick Loeber

# Original source: https://github.com/patrickloeber/pytorch-chatbot/blob/master/chat.py

# [I have modified and added code to allow the use of OpenAI API to respond to user inputs in the case that the 
# dataset is unable to answer]

import openai
import random
import json
import torch
from train_model import NeuralNet
from backend.nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('train_data.json', 'r') as f:
    train_data = json.load(f)
with open('hidden.txt') as file:
    openai.api_key = file.read()

FILE = "saved_data/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words_arr = data["all_words"]
tags = data["tags"]
model = data["all_words"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

chat_history = []
bot_name = "Sheldon"
def getResponse(message):
    global chat_history
    unable_to_find_response = "Ah, it appears that the inquiry you've posed falls outside the realm of portfolio building, or perhaps it is a subject that has eluded my vast knowledge. Fear not, for I have a brilliant solution at hand. I happen to be acquainted with an esteemed colleague who possesses expertise in this very matter. Shall I take it upon myself to consult with him and seek an answer to your intriguing question?"

    sentence = tokenize(message)
    X = bag_of_words(sentence, all_words_arr)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.90 or message.startswith("yes"):
        for intent in train_data["intents"]:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
    else:
        response = generateOpenAIResponse(message)
    
    chat_history.append([message, response])
    return response
    
def retrieveChatHistory():
    global chat_history
    return chat_history


def generateOpenAIResponse(message):
    messages = [{"role": "system", "content": "You are Sheldon Cooper and you should talk like him and your role is to give advice to students in building a personal portfolio for jobs and internships"}]
    messages.append({"role":"user", "content":message})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    text_reply = response["choices"][0]["message"]["content"]
    print(text_reply)
    return text_reply


