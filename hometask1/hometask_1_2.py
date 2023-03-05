n = int(input('Введите количество чисел в списке: '))
s = [] # список чисел
for i in range(n):
    a = int(input('Введите число: '))
    s.append(a)
for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1
    if count == 1:
        print('Число, которое повторяется один раз: ', i)