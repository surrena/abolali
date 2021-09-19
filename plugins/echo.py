from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command('start'))
def start(client, message):
    chat_id = message.chat.id
    client.send_message(
        chat_id,
        "please choose",
        reply_markup=ReplyKeyboardMarkup(
            [
                ["download  from YT", "download from PH"],  # First row
                ["Communication with admin"]  # second row
            ],
            resize_keyboard=True
        )
    )
