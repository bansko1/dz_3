amount_of_elements = input('Введите количество элементов: ')
list_of_elements = []
for i in range(int(amount_of_elements)):
    sentense = f'Введите {i+1} элемент: '
    x = input(sentense)
    list_of_elements.append(int(x))
list_of_elements.sort()
print('Вывод:', list_of_elements)
