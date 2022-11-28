import telebot
from random import *
import json
import requests
films = []
API_URL = 'https://7012.deeppavlov.ai/model'

def save():
    with open('films.json','w',encoding='utf-8') as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print('Our films collection was successfully saved in file films.json')

def load():
    global films
    with open('films.json','r',encoding='utf-8') as fh:
        films = json.load(fh)
  


API_TOKEN = '5835810655:AAHADFcvbV_LGtZ2TMxIEl4gq1ys5whAhj8'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id,"Фильмотека была успешно загружена")
    except:
        films.append('Matricha')
        films.append('Solaris')
        films.append('Lord of the rings')
        films.append('Texas')
        films.append('Santa Barbora')
        bot.send_message(message.chat.id,"Фильмотека была успешно загружена по умолчанию")

@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id,"Вот весь список фильмов:")
    bot.send_message(message.chat.id,','.join(films))

@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = " ".join(quest)
    data = {'question_raw':[qq]}
    try:
        res = requests.post(API_URL,json=data,verify=False).json()
        bot.send_message(message.chat.id,res)
    except:
        bot.send_message(message.chat.id,'Что-то я ничего не нашел')
    # bot.send_message(message.chat.id,','.join(films))


bot.polling()