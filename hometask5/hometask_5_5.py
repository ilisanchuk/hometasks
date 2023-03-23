def total(*args):
    return sum(args)
quantity = int(input('Введите количество элементов в списке: '))
list_of_numbers = [int(input('Введите число: ')) for x in range(quantity)]
print('Список чисел:')
print(*list_of_numbers, sep=', ')
print('Сумма этих чисел:\n', total(*list_of_numbers))