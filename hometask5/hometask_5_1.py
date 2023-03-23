
list_of_words = [n.strip() for n in input('Введите слова через запятую:\n').split(',')]
print('Отсортированый список по алфавиту:')
print(*sorted(list_of_words), sep=', ')
