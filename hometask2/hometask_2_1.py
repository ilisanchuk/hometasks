months = {1: 'Январь, 31 дней', 2: 'Февраль, 28 дней', 3: 'Март, 31 дней', 4: 'Апрель, 30 дней', 5: 'Май, 31 дней', 6: 'Июнь, 30 дней', 7: 'Июль, 31 дней', 8: 'Август, 31 дней', 9: 'Сентябрь, 30 дней', 10: 'Октябрь, 31 дней', 11: 'Ноябрь, 30 дней', 12: 'Декабрь, 31 дней'}
a = True
while a == True:
    n = input('Введите порядковый номер месяца от 1 до 12: ')
    if n.isdigit():
        n = int(n)
        if 0 < n < 13:
            print(months[n], '      Для выхода введите q.', sep='\n')
        else:
            print('На Земле только 12 месяцев, попробуйте ещё раз!', '      Для выхода введите q.', sep='\n')
    elif n == 'q':
        break
    else:
        print('Неправильный ввод данных, попробуйте ещё раз!', '        Для выхода введите q.', sep='\n')