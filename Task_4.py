""" Задайте список из N элементов, заполненных числами из
промежутка [-N, N].
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число. """
num = int(input('Введите число '))
lst = [i for i in range(-num, num+1)]
sum = 1
with open('text') as text:
    index = list(map(int, text.readlines()))
for i in range(len(index)):
    sum *= lst[index[i]]
print(lst)
print(sum)