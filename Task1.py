# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number

N = check_digit('Введите, пожалуйста, любое целое число: ')

def primfactors(n):
    i = 2
    result = []
    while i <= n:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 1
    return result

print(f'Список простых множителей числа {N} : {primfactors(N)}')

