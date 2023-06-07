# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

n = int(input('Введите количество элементов:    '))
array = [randint(-9, 9) for i in range(n)]
min_el = int(input('Введите цифру 1 - 5:    '))
max_el = int(input('Введите цифру 6 - 10:    '))

def find_index(arr, mini, maxi,):
    index = []
    #arr.append(randint(-9, 9))
    for i in range(len(arr)):
        if mini <= arr[i] <= maxi:
            index.append(i)
    return index
    
print(array)
print(find_index(array, min_el, max_el))

