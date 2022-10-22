# Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа

import long_responses as long
import re

def probability_of_message(our_message,neccesary_words,if_single_response=False,need_words=[]):#создаем функцию для вычисления вероятности того, что для сообщения от пользователя есть определенное сообщение ответа бота.
    message_certain = 0
    has_required_words = True

    for word in our_message:#пишем цикл, которые будет помогать нам находить слова, запрограммированные в распозноваемые слова для бота
        if word in neccesary_words:#опознаваемые слова ботом, для которых у него уже запрограммирован готовый ответ
            message_certain += 1
    percent = float(message_certain)/float(len(neccesary_words))#вычисляем процент того, сколько слов было распознано ботом для выбора ответа 

    for word in neccesary_words:#создаем цикл для того, чтобы отбросить слова, которые не запрограммированы в вопросы для бота 
        if word not in our_message:
            has_required_words = False
            break
    
    if has_required_words or if_single_response:
        return int(percent*100)#возвращает процент совместимости каждого сообщения пользователя с распозноваемыми словами для бота
    else:
        return 0

def check_messages(input_message):#создаем функцию со вложенной в нее же другой функции для распознования ботом сообщения от пользователя и ответу ему
    highest_prob_list = {}#словарь, где ключом будет ответ бота, а элементами - кол-во совпадений с запрограммировами предложениями для бота от пользователя

    def response(bot_response,list_of_words,if_single_response = False,need_words = []):#вложенная функция, где мы в качестве аргументов берем ответ бота, список слов для распознования ботом, чтобы дать ответ и определяем, может ли ответ быть единственным или же могут быть какие-то ключевые слова для распознования ботом
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = probability_of_message(input_message,list_of_words,if_single_response,need_words)#записываем в словарь ответ бота и процент распознавания слов
    response('Привет',["здравствуйте","добрый день","привествую","доброго дня","привет"],if_single_response=True)
    response('У меня все отлично, как у тебя ?',["как","у","тебя","дела"],need_words='дела')
    response('Спасибо!',["мне","нравится","с","тобой","общаться"],need_words=['нравиться','нравишься'])
    response('Пожалуйста',["спасибо","благодарю"],if_single_response=True)
    response('Общаюсь с тобой',["что","делаешь","чем","занимаешься"],if_single_response=True)
    response("До встречи!",["пока","прощай","до свидания","до встречи"],if_single_response=True)
    response('Меня зовут Бот-Пулсон!',["как","тебя","зовут"],need_words=['зовут'])

    response(long.R_SING,["какая","твоя","любимая","песня"],need_words=["песня"])
    response(long.R_BOOK,["какую","ты","читал","книгу","в","последний","раз"],need_words=["совет"])

    match = max(highest_prob_list,key = highest_prob_list.get)#с помощью максимального количества совпадений между заданной строки для бота и сообщением от пользователя и будет определяться ответ на вопрос
    # print(highest_prob_list)

    return long.unknown_quetion() if highest_prob_list[match] < 1 else match# если совпадений будет меньше одного, то бот выдаст ответ из файла long_responses, где прописаны рандомные ответы на неопознанные сообщения от пользователя, в противном случае бот выдаст ответ в виде ключа словаря с наибольшом процентом совпадения


def get_bot_responses(our_input):#создаем функцию, которая будет принимать на вход вопрос от пользователя
    message = re.split(r'\s+|[,;?!.-]\s*',our_input.lower())#убираем лишние знаки из сообщения и приводим его к нижнему регистру для удобного анализа, а также разделяем каждое слово отдельно
    response = check_messages(message)
    return response


while True: #пока тру, получаем новые ответы от бота
    print('Бот:' + get_bot_responses(input('Вы: ')))