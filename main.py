import requests
import telebot
import dotenv
import os

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

users = {}

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['list'])
def get_books_list(message):
    if message.from_user.id not in users or not users[message.from_user.id]:
        bot.send_message(message.chat.id, 'You don\'t have any books yet, but you can /add them')
        return

    books = users[message.from_user.id]
    reply = '\n\n'.join([f'{title}\n{authors}' for title, authors in books])
    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['add'])
def add_book(message):
    if message.from_user.id not in users:
        users[message.from_user.id] = []
    users[message.from_user.id].append([])

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton('By info', callback_data='add_by_info'),
        InlineKeyboardButton('By ISBN', callback_data='add_by_isbn'),
    )

    bot.send_message(message.chat.id, 'How you want to add your book?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def proceed_callback(call):
    bot.edit_message_reply_markup(call.message.chat.id, call.message.id)
    if call.data == 'add_by_info':
        add_book_by_info(call.message)
    elif call.data == 'add_by_isbn':
        add_book_by_isbn(call.message)


def add_book_by_isbn(message):
    bot.send_message(message.chat.id, 'Gimme ISBN')
    bot.register_next_step_handler(message, add_book_isbn)


def add_book_isbn(message):
    isbn = message.text
    users[message.from_user.id][-1].append(isbn)

    bot.send_message(message.chat.id, f'Book ISBN: {isbn}')
    bot.send_message(message.chat.id, 'Successfully added!')


def add_book_by_info(message):
    bot.send_message(message.chat.id, 'Gimme book name')
    bot.register_next_step_handler(message, add_book_name)


def add_book_name(message):
    book_name = message.text
    users[message.from_user.id][-1].append(book_name)

    bot.send_message(message.chat.id, f'Book name: {book_name}')
    bot.send_message(message.chat.id, 'Gimme authors list')
    bot.register_next_step_handler(message, add_book_authors)


def add_book_authors(message):
    authors = message.text
    users[message.from_user.id][-1].append(authors)

    bot.send_message(message.chat.id, f'Book authors: {authors}')
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
