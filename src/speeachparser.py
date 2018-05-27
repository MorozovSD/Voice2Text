import speech_recognition as sr
import soundfile as sf
import re
from googletrans import Translator


class SearchFilter:
    def __init__(self, string_filter=''):
        self.year = find_year(string_filter)
        self.genre = find_genre(string_filter)
        self.country = find_country(string_filter)
        self.rate = find_rate(string_filter)
        self.name = find_name(string_filter)
        self.producer = find_producer(string_filter)


def translate_filter_to_english(russian_filter):
    english_filter = SearchFilter()
    if russian_filter.year is not None:
        english_filter.year = russianFilter.year
    if russian_filter.genre is not None:
        english_filter.genre = translate_to_english(russianFilter.genre)
    if russian_filter.country is not None:
        english_filter.country = translate_to_english(russianFilter.country)
    if russian_filter.rate is not None:
        english_filter.rate = translate_to_english(russianFilter.rate)
    if russian_filter.name is not None:
        english_filter.name = translate_to_english(russianFilter.name)
    if russian_filter.producer is not None:
        english_filter.producer = translate_to_english(russianFilter.producer)
    return english_filter



def parse_parameter(regexp, string_filter):
    search_result = re.search(regexp, string_filter, re.IGNORECASE)
    if search_result is None:
        return None
    else:
        return search_result.groups()[0]


def find_year(string_filter):
    return parse_parameter(r'Год (\d+),?', string_filter)


def find_genre(string_filter):
    return parse_parameter(r'Жанр ([^,]+),?', string_filter)


def find_country(string_filter):
    return parse_parameter(r'Страна ([^,]+),?', string_filter)


def find_rate(string_filter):
    return parse_parameter(r'Рейтинг (\d+),?', string_filter)


def find_name(string_filter):
    return parse_parameter(r'Название ([^,]+),?', string_filter)


def find_producer(string_filter):
    return parse_parameter(r'Продюсер ([^,]+),?', string_filter)


def translate_to_english(word):
    translator = Translator()
    return translator.translate(word, src='ru', dest='en').text


#data, samplerate = sf.read('S:\\123.ogg')
#sf.write('S:\\123.wav', data, samplerate)
r = sr.Recognizer()

#with sr.AudioFile(AUDIO_FILE) as source:
#    audio = r.record(source)
#with sr.Microphone() as source:
    #print("Скажите что-нибудь")
    #audio = r.listen(source)

result = 'жанр комедия, год 1984, страна Россия, рейтинг 8, продюсер Харви вайнштейн'
try:
    #result = r.recognize_google(audio, language="ru-RU")
    russianFilter = SearchFilter(string_filter=result)
    englishFilter = translate_filter_to_english(russianFilter)
    print(result)
    print(englishFilter.year)
    print(englishFilter.genre)
    print(englishFilter.country)
    print(englishFilter.rate)
    print(englishFilter.name)
    print(englishFilter.producer)
except sr.UnknownValueError:
    print("Робот не расслышал фразу")
except sr.RequestError as e:
    print("Ошибка сервиса; {0}".format(e))