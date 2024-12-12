#GRADE 1. ЭТАП 1. Задание 4.
#ВВОД ПОЛЬЗОВАТЕЛЬСКИХ ДАННЫХ
username = input('Введите имя: ')
content = input('Введите описание: ')
status = input('Введите статус (Активна / Завершена): ')
created_date = input('Ввведите дату создания (день-месяц-год): ')
issue_date = input('Ввведите дату завершения (день-месяц-год): ')

#ОБЪЯВЛЕНИЕ СПИСКА
titles_lst = []

#ВВОД ЗАГОЛОВКОВ ПО СРЕДСТВАМ ЦИКЛА
for item in range(3):
    title = input(f'Введите заголовок заметки {item + 1}: ')
    titles_lst.append(title)

#ВЫВОД ПОЛЬЗОВАТЕЛЬСКИХ ДАННЫХ
print('\nВведены следующие данные:')
print('Имя пользователя: ', username)
print('Название: ', titles_lst)
print('Описание: ', content)
print('Статус: ', status)
print('Дата создания: ', created_date[0:5])
print('Дата завершения: ', issue_date[0:5])
