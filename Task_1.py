""" Напишите программу, которая принимает на вход 
вещественное число и показывает сумму его цифр.

    *Пример:*

    - 6782 -> 23
    - 0.56 -> 11 """

#Вариант1
""" num = input('Введите число ')

def summa(num):                            
    if float(num) < 0:                            
        num = float(num) * (-1)
    number = 0

    for i in str(num): # Превращаем в строку
        if i != '.':
            number += int(i)
    return number

print(f'Сумма чисел равна {summa(num)}') """

#Вариант2
num = abs(float(input('Введите число:'))) 
while num%1 != 0:  
    num *= 10
sum = 0      
while num > 0: 
        sum += num % 10
        num //= 10
print(f'Сумма чисел равна {int(sum)}')
#while round(num) != num:  остаток от деления на на 1 не равен 0