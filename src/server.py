# -*- coding: utf-8 -*-
import telebot

token=%TG_TOKEN%
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    print(message.chat.id, ': ', message.text, sep='')
    bot.send_message(message.chat.id, 'Что значит "%s"?' % message.text)

@bot.message_handler(content_types=['voice'])
def handle_docs_audio(message):
    print(message.chat.id, ': voice message')
    bot.send_message(message.chat.id, 'Сейчас это слишком сложно для меня')

if __name__ == '__main__':
    print("START")
    bot.polling(none_stop=True)