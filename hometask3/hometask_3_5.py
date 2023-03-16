def unique():
    def choice():
        y = input('\t Попробовать ещё раз? (y/n): ')
        if y == 'y':
            return unique()
        elif y == 'n':
            raise SystemExit
        else:
            return choice()
    numbers = input('\t Введите числа через пробел по неубыванию: ')
    lst = numbers.split(' ')
    space = lst.count('')
    for _ in range(space):
        lst.remove('')
    for i in lst:
        if not i.isdigit():
            print('Неверный формат данных!')
            choice()
    lst = list(map(int, lst))
    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            continue
        else:
            print('Внимательней читайте условие!')
            choice()
    count = 1
    for i in range(1, len(lst)):
        if lst[i - 1] != lst[i]:
            count += 1
    print('Исходный список: ', ' '.join(map(str, lst)))
    print('Количество различных элементов: ', count)
    choice()

unique()