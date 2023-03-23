from itertools import permutations
list_of_numbers = [1, 2, 3]
print('Исходный список:\n', list_of_numbers)
list_of_numbers = list(map(str, list_of_numbers))
result = []
for i in permutations(list_of_numbers):
    option = list(''.join(i))
    lists = [int(x) for x in option]
    result.append(tuple(lists))
print('Все возможные комбинации этого списка:')
print(*result, sep=', ')