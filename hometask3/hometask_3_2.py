def calc_deposit():
    def choice():
        y = input('\t Попробовать ещё раз? (y/n): ')
        if y == 'y':
            return calc_deposit()
        elif y == 'n':
            raise SystemExit
        else:
            return choice()

    deposite = input('Введите первоначальный вклад в рублях: ')
    years = input('Введите планируемое количество лет: ')
    annual_interest = 0.10
    deposite, years = deposite.strip(), years.strip()
    if not deposite.isdigit() or not years.isdigit():
        print('\t Неправильный формат данных!')
        choice()
    else:
        deposite, years = int(deposite), int(years)
    year = years
    initial_deposite = deposite
    while years > 0:
        deposite += deposite * annual_interest
        years -= 1
    print(f'\t Ваш вклад {initial_deposite} рублей через {year} лет под {int(annual_interest * 100)}% годовых будет равен: {round(deposite, 2)} рублей.')
    choice()


calc_deposit()