# задача 4 необязательная. Найдите корни квадратного уравнения, уравнение вводит через строку пользователь. например, 6*x^2+5*x+6=0 . 
# Само собой, уравнение может и не иметь решения. Предусмотреть все варианты, сделать обработку исключений.

# def input_equation():

#     print("Если коэффициент равен 0 или 1, пожалуйста, также введите этот коэффициент при вводе уравнения")
#     equation = input('Введите, пожалуйста,каждый элемент уравнения вида 6 * x ^ 2 + 1 * x + 0 = 0 ЧЕРЕЗ ПРОБЕЛ отдельно: ')
#     buff = equation.split()
#     list = []
#     for i in range(len(buff)):
#         if len(buff) != 13:
#             print('Возможно Вы ввели не все уравнение целиком, необходимо ввести уравнение через ПРОБЕЛ каждый элемент в виде 6 * x ^ 2 + 1 * x + 0 = 0')
#             break
#         else:
#             list.append(buff[i])
#     return list

def input_equation(s):
    symbols = ['x','*','^','+','=',' ',',','.']
    for i in symbols:
        s = s.replace(i,' ')
    s1 = s.replace('2',' ', 1) 
    
    return list(map(int,s1.split( )))
    

import math

def equation_roots(equation):

    a = float(equation[0])
    b = float(equation[1])
    c = float(equation[2])
    print(a,b,c)
    
    if a != 0:
    
        if  b !=0 and c != 0:
            d = b*b - 4*a*c
            print("D=", d)
        
            if d < 0:
                print("Нет корней")
        
            elif d == 0:
                print("1 Корень")
                x = -b / (2*a)
                print("x=", x)
    
            else:
                print("2 Корня")
                x1 = (-b + math.sqrt(d)) / (2*a)
                x2 = (-b - math.sqrt(d)) / (2*a)
                print("x1=", x1, "x2=", x2)
            
        elif b == 0 and c == 0:
            print("Неполное кв. ур")
            print("Корень x=" , 0)
        
        elif b == 0:
            print("Неполное кв. ур")
            if -c / a < 0:
                print("Нет корней")
            else:
                print("2 Корня")
                x1 = math.sqrt(-c / a)
                x2 = -x1
                print("x1=", x1, "x2=", x2)
        else:
            print("Неполное кв. ур")
            print("2 Корня")
            x1 = 0
            x2 = -b / a
            print("x1=", x1, "x2=", x2)
    
    else:
        print("Нужно вводить a > 0, иначе это не кв. ур-е !")

try:
    print('Перед вводом уравнения обратите,пожалуйста, внимание,что если коэффициенты у Вас равны 0 или 1, то их также необходимо прописать, например:-1x^2+0x+2=0')
    equation = input('Введите, пожалуйста, уравнение в виде: 6*x^2+5*x+6=0 для вычисления корней квадратного уравнения: ')
    equal = input_equation(equation)
    equation_roots(equal)
except:
    print('Возможно Вы ввели уравнение не так, как показано в образце, пожалуйста, введите уравнение заново в формате: 6*x^2+5*x+6=0')
        
    


        
    

    








