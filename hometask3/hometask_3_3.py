def change_lst():
    def choice():
        y = input('Попробовать ещё раз? (y/n): ')
        if y == 'y':
            return change_lst()
        elif y != 'n':
            return choice()
    lst = input('Введите строку больше 2 символов: ')
    if len(lst) > 2:
        list_of_symbols = list(lst)
        list_of_symbols[0], list_of_symbols[-1] = list_of_symbols[-1], list_of_symbols[0]
        print('Строка, где поменяли первый и последний символ:\n', ''.join(list_of_symbols))
        choice()
    else:
        print('Введите более двух символов!')
        choice()

change_lst()