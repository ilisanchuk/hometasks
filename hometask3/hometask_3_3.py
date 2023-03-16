def change_lst():
    def choice():
        y = input('\t Попробовать ещё раз? (y/n): ')
        if y == 'y':
            return change_lst()
        elif y != 'n':
            return choice()

    lst = input('\t Введите строку больше 1 символа: ')
    lst = lst.strip()
    if len(lst) >= 2:
        list_of_symbols = list(lst)
        list_of_symbols[0], list_of_symbols[-1] = list_of_symbols[-1], list_of_symbols[0]
        print('Строка, где поменяли первый и последний символ:', ''.join(list_of_symbols))
        choice()
    else:
        print('Введите более одного символа!')
        choice()

change_lst()