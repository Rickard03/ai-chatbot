# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import requests

x = requests.get('https://w3schools.com/python/demopage.htm')




## tutiral https://realpython.com/build-a-chatbot-python-chatterbot/


# from datetime import datetime 



# dateNow = datetime.now()

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
        "Welcome, geh2 🤗",
])


trainer.train([
    "Sveriges huvudstad",
    "Det är Stockholm",
])



trainer.train([
    "Datum",
    x.text
])


trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])


exit_conditions = (":q", "quit", "exit")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")