def choice():
    y = input('Попробовать ещё раз? (y/n): ')
    if y == 'y':
        return bigger_than_neighbours()
    elif y == 'n':
        raise SystemExit
    else:
        return choice()
def bigger_than_neighbours():
    numbers = input('Введите числа через пробел: ')
    lst = numbers.split(' ')
    space = lst.count('')
    for _ in range(space):
        lst.remove('')
    for i in lst:
        if not i.isdigit():
            print('Неверный формат данных!')
            choice()
    count = 0
    for i in range(1, len(lst) - 1):
        if lst[i - 1] < lst[i] > lst[i + 1]:
            count += 1
    if count == 0:
        print('Элементов, которые больше своих соседей нет!')
        choice()
    else:
        print('Исходный список: ', ' '.join(lst))
        print('Количество элементов, которые больше своих соседей: ', count)
        choice()

bigger_than_neighbours()