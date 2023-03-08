a = True
while a == True:
    numbers = input('Введите числа через пробел: ')
    list_of_numbers = numbers.split(' ')
    space = list_of_numbers.count('')  # счетчик ненужных пробелов
    if numbers == 'q':
        break
    else:
        for _ in range(space):
            list_of_numbers.remove('') # удаляем ненужные пробелы
        for i in list_of_numbers:
            if not i.isdigit():
                print('Неверный формат данных, попробуйте ещё раз!\n        Для выхода введите q.')
                break
            else:
                list_of_numbers.reverse()
                print('Список чисел в обратном порядке: ', ' '.join(list_of_numbers), '\n       Для выхода введите q.')
                break