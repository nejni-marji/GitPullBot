#!/usr/bin/env python3
import telegram as tg
import telegram.ext as tg_ext

def start(bot, update):
	bot.send_message(update.message.chat.id, 'Started!')

def main(dp):
	dp.add_handler(tg_ext.CommandHandler('start', start))
