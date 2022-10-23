
import random

def unknown_answer():
    random_answer = [
            "Прости, я не понял вопроса..:(",
            "Звучит интересно",
            "Я не понял вопроса, попробуй задать как-то по другому ... пожалуйста:))",
            "....",
            "Вопрос интересный, но я не знаю на него ответ(((((((("
         ]
    
    length = len(random_answer)
    random_index = random.randrange(length)
    return random_answer[random_index]


