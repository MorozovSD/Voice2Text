# -*- coding: utf-8 -*-
import telebot
from speech_parser import get_filter
from sparql_request import get_ids
from imdb_requests import get_films

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

    filter = get_filter(message.chat.id, file_info, token)
    if filter['result'] == 'error':
        bot.send_message(message.chat.id, filter['message'])
    else:
        bot.send_message(message.chat.id, 'Идет поиск по вашему запросу')
        ids, b, c = get_ids(filter['filter'])
        print('ids:', ids)
        films = get_films(ids)
        print(films)
        result = ''
        for i in range(len(films)):
            result += str(i+1) + ') ' + films[i]['title'] + '\n'
            if films[i].get('description'):
                result += films[i].get('description') + '\n'
            result += '\n'
        if not result:
            result = 'По вашему запросу ничего не найдено'
        bot.send_message(message.chat.id, result)


if __name__ == '__main__':
    print("START")
    bot.polling(none_stop=True)