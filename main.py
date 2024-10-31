import json
import requests
import telebot
import dotenv
import os

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    bot.reply_to(message, "Great sticker!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

# -----

url = 'https://pokeapi.co/api/v2/pokemon/ditto'
data = requests.get(url).json()

print(data)
print(data['abilities'][1]['ability']['name'])

with open('data.json') as f:
    print(json.load(f))

info = {
    'name': 'Nikolai Andreev',
    'age': 26,
}

print(json.dumps(info, indent=2))
