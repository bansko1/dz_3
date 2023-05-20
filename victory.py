import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
year_truth = ['1799', '1809', '1814', '1821', '1821', '1828', '1860', '1891', '1895', '1905']
name_writers = ['А.С.Пушкина: ', 'Н.В.Гоголя: ', 'М.Ю.Лермонтова: ', 'Ф.М.Достоевского: ',
                'С.А.Некрасова: ', 'Л.Н.Толстого: ', 'А.П.Чехова: ',
                'М.А.Булгакова: ', 'С.А.Есенина: ', 'М.А.Шолохова: ']
while True:
    result = random.sample(numbers, 5)
    answers = []
    for i in result:
        sentense = f'Введите год рождения {name_writers[i - 1]}'
        answer = input(sentense)
        answers.append(answer)
        if answer != year_truth[i - 1]:
            print('Ошибка. Правильный ответ: ', year_truth[i - 1])

    counter = 0
    for i in range(5):  # Проход в цикле по всем писателям
        if answers[i] == year_truth[result[i] - 1]:
            counter += 1

    print('Количество правильных ответов', counter)
    print('Количество ошибок', 5 - counter)
    # print('Процент правильных ответов', counter / 5 * 100)
    # print('Процент неправильных ответов', (5 - counter) / 5 * 100)
    question = input('Хочет ли участник начать игру сначала? (да, нет) ')
    if question == 'нет':
        break
