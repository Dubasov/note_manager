#GRADE 1. ЭТАП 1. Задание 5.
#Объявляем словарь
note_dict = {}

#Ввод пользовательских данных
note_dict['Имя пользователя'] = input('Введите имя: ')                                  #username
note_dict['Описание'] = input('Введите описание: ')                                     #content
note_dict['Статус'] = input('Введите статус (Активна / Завершена): ')                   #status
note_dict['Дата создания'] = input('Ввведите дату создания (день-месяц-год): ')         #created_date
note_dict['Дата завершения'] = input('Ввведите дату завершения (день-месяц-год): ')     #issue_date

#Объявление списка заголовков по ключу
note_dict['Заголовки'] = []

#Ввод пользовательских заголовков
for item in range(3):
    title = input(f'Введите заголовок заметки {item + 1}: ')
    note_dict['Заголовки'].append(title)

#Вывод данных словаря при помощи f-strings
print('\nВведены следующие данные:')
for key, value in note_dict.items():
    print(f"{key}: {value}")