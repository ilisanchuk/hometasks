print('КАЛЬКУЛЯТОР')
def calc():
    def choice():
        y = input('Попробовать ещё раз? (y/n): ')
        if y == 'y':
            return calc()
        elif y != 'n':
            return choice()
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    symbol = input('Введите знак + , - , * или /: ')
    if not a.isdigit() or not b.isdigit():
        print('Неверный формат данных!')
        choice()
    else:
        a, b = int(a), int(b)
        if symbol == '+':
            d = a + b
            print(f'Итого: {a} {symbol} {b} = {d}')
            choice()
        elif symbol == '-':
            d = a - b
            print(f'Итого: {a} {symbol} {b} = {d}')
            choice()
        elif symbol == '*':
            d = a * b
            print(f'Итого: {a} {symbol} {b} = {d}')
            choice()
        elif symbol == '/':
            if b == 0:
                print('На ноль делить нельзя!')
                choice()
            else:
                d = a / b
                print(f'Итого: {a} {symbol} {b} = {d}')
                choice()
        else:
            print('Неправильный формат знака.')
            choice()
calc()