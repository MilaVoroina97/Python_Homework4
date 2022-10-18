# задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number

def create_array(n):
    result = []
    for i in range(n):
        result.append(check_digit('Введите, пожалуйста, любое целое число для заполнения массива: '))
    return result

n = check_digit('Введите, пожалуйста, целое число для определения размера массива: ')
list = create_array(n)
print(list)

def unique_numbers_in_list(array):
    array1 = []
    for i in array:
        if i not in array1:
            array1.append(i)
    return array1

print(f'Список уникальных элементов: {unique_numbers_in_list(list)}')