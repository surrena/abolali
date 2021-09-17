from pyrogram import Client, filters



@Client.on_message(filters.command('start'))
def start(client, message):
	message.reply_text('Hello there...')