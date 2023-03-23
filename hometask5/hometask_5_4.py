from random import sample
left = int(input('Введите минимальное число в списке: '))
right = int(input('Введите максимальное число в списке: '))
quantity = int(input('Введите количество различных элементов, которое хотите получить из данного списка: '))
lists = list(range(left, right))
lists = [x for x in sample(lists, quantity)]
print(f'Список из {quantity} случайных элементов в диапазоне от {left} до {right}:\n', *lists)