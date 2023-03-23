list_of_numbers = [1, 2, 3]
print('Исходный список из 3х элементов:\n', list_of_numbers)
list_of_numbers = list(map(str, list_of_numbers))
result = []
for i in list_of_numbers:
    for j in list_of_numbers:
        for k in list_of_numbers:
            lists = i + j + k
            if lists.count('1')==1 and lists.count('2')==1 and lists.count('3')==1:
                lists = [int(x) for x in lists]
                result.append(tuple(lists))
print('Все возможные комбинации этого списка:')
print(*result, sep=', ')