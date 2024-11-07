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


@bot.message_handler(commands=['add'])
def add_book(message):
    bot.send_message(message.chat.id, 'Gimme book name')
    bot.register_next_step_handler(message, add_book_name)


def add_book_name(message):
    bot.send_message(message.chat.id, f'Book name: {message.text}')
    bot.send_message(message.chat.id, 'Gimme authors list')
    bot.register_next_step_handler(message, add_book_authors)


def add_book_authors(message):
    bot.send_message(message.chat.id, f'Book authors: {message.text}')
    bot.send_message(message.chat.id, 'Successfully added!')


@bot.message_handler(commands=['pokemon'])
def get_pokemon(message):
    print(message.text)
    pokemon_name = message.text.split()[1]
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    data = requests.get(url).json()

    reply = (f'Pokemon name: {data["name"]}\n'
             f'Weight: {data["weight"]}\n'
             f'Height: {data["height"]}')

    bot.reply_to(message, reply)


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    bot.reply_to(message, "Great sticker!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, 'Unknown message')


bot.infinity_polling()
