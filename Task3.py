# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
# степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
def create_koeff(k):
    list = []
    for i in range(k + 1):
        list.append(randint(1,100))
    print(list)
    return list 

def create_equation(array):
    equation = ''
    size = len(array)
    if size < 1:
        equation = 'x = 0'
    else:
        for i in range(size): 
            if i != size - 1 and i != size - 2 and array[i] != 0:
                equation += f'{array[i]}x**{size - i -1}'
                if array[i + 1] != 0:
                    equation += ' + '
            elif i == size - 2 and array[i] != 0: 
                equation += f'{array[i]}x'
                if array[i + 1] != 0:
                    equation += ' + '
            elif i == size - 1 and array[i] != 0: 
                equation += f'{array[i]} = 0'
            elif i == size - 1 and array[i] == 0:
                equation += ' =0'
    return equation

def write_in_file(result):
    with open('file.txt','w') as data:
        data.write(result)

def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number

k = check_digit('Введите натуральную степень k для уравнения: ')
write_in_file(create_equation(create_koeff(k)))


            




