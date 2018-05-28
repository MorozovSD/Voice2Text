# -*- coding: utf-8 -*-
import telebot
from .speech_parser import speech_to_films

token=%TG_TOKEN%
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    print(message.chat.id, ': ', message.text, sep='')
    bot.send_message(message.chat.id, 'Что значит "%s"?' % message.text)

@bot.message_handler(content_types=['voice'])
def handle_docs_audio(message):
    print(message.chat.id, ': voice message')
    file_info = bot.get_file(message.voice.file_id)
    bot.send_message(message.chat.id, 'Держи:\n' + speech_to_films(file_info, token))

if __name__ == '__main__':
    print("START")
    bot.polling(none_stop=True)