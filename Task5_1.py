

import response_randomly as res
import json
import re


def load_file(file):
    with open(file) as responses:
        print(f'Файл {file} был успешно загружен')
        return json.load(responses)


bot_answers = load_file('answers_bot.json')
print(bot_answers)

def get_response(our_message):
    message =  re.split(r'\s+|[,;?!.-]\s*',our_message.lower())
    count_list = []

    for answer in bot_answers:
        answer_count = 0
        need_count = 0
        need_words = answer['need_words']

        if need_words:
            for word in message:
                if word in need_words:
                    need_count += 1
        if need_count == len(need_words):
            for word in message:
                if word in answer['user_message']:
                    answer_count += 1
        
        count_list.append(answer_count)
    
    more_match = max(count_list)
    answer_index = count_list.index(more_match)

    if our_message == "":
        return 'Please write something.'

    if more_match != 0:
        return bot_answers[answer_index]['responses']
    
    return res.unknown_answer()



while True:
    user_message = input('Вы: ')
    print('Бот: ', get_response(user_message))