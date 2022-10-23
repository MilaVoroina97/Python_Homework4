
import response_randomly as res
import json
import re


def load_file(file):
    with open(file,'r',encoding='utf-8') as responses:
        print(f'Файл {file} был успешно загружен')
        return json.load(responses)


bot_answers = load_file('answer.json')#answers_bot - подгружаем файл с ответами для бота в виде списка словарей 
# print(bot_answers)

def get_response(our_message):#создаем функцию, которая будет распознавать сообщение от пользователя и в зависимости от кол-ва наиболее подходящих слов в вопросе, бот будет давать ответ.
    message =  re.split(r'\s+|[,;?!.-]\s*',our_message.lower())# "очищаем" сообщение пользователя для его удобного анализа
    count_list = []#сюда будем записывать кол-во удачного совпадения с сообщением пользователя и запрограммированного для бота вероятного сообщения пользователя

    for answer in bot_answers:#цикл, который проходит через весь список словарей с запрограммированными ответами для бота и возможными сообщениями от пользователя
        answer_count = 0# переменная для подсчета совпадений сообщения пользователя с запрограммированных для бота набора возможных сообщений от пользователя
        need_count = 0#переменная для подсчета совпадений с обязательными словами
        need_words = answer['need_words']#лист с обязательными словами для совпадения
        

        if need_words:#если слова совпали:
            for word in message:#цикл для поиска распознаваемых ботом слов в сообщении от пользователя
                if word in need_words:#если слово в сообщении от пользователя есть в обязательных словах
                    need_count += 1#плюсуем счетчик
        if need_count == len(need_words):#если все слова из списка обязательных слов для совпадения совпали
            for word in message:#снова проходим по сообщению от пользователя
                if word in answer['user_message']:#если в сообщение от пользователя есть слова из запрограммированных возможных вопросов от пользователя для бота
                    answer_count += 1#плюсуем счетчик
        
        count_list.append(answer_count)
    
    more_match = max(count_list)#находим максмальное число совпадений
    answer_index = count_list.index(more_match)#записываем индекс этого числа в листе

    if our_message == "":
        return 'Please write something.'

    if more_match != 0:#если число совпадений не равно нулю, то возвращаем пользователю ответ с наибольшим число совпаденй 
        return bot_answers[answer_index]['responses']
    
    return res.unknown_answer()#если сообщение не распознано,возвращаем рандомные ответы



while True:
    user_message = input('Вы: ')
    print('Бот: ', get_response(user_message))