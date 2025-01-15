# GRADE 1. ЭТАП 3. Задание 4.

import datetime  # Работа с датами
from colorama import init, Fore  # Библиотека для раскрашивания консоли

init(autoreset=True)  # Авто сброс покраски строчек

# Укрощение colorama цветов
r = Fore.RED
m = Fore.MAGENTA
c = Fore.CYAN
g = Fore.GREEN
lg = Fore.LIGHTGREEN_EX
y = Fore.YELLOW


# ФУНКЦИЯ ОТРИСОВКИ ЗАМЕТОК ПРИ ПОИСКЕ
def search_display(note):
    print(lg + '\nНАЙДЕННЫЕ РЕЗУЛЬТАТЫ')
    print('⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯')
    for key, value in note.items():  # Перебор словаря note
        if isinstance(value, list):  # Если type = list
            print('▶ Тема: '.ljust(22, ' '), '; '.join(value))  # список в строку
        else:
            print(f'▶ {key}:'.ljust(22, ' '), f'{value}')

    # Получение временной (temp) текущей даты для вычисления объекта timedelta
    temp_created_date = datetime.datetime.now()
    temp_issue_date = datetime.datetime.strptime(note['Дата завершения'], "%d-%m-%Y")
    if temp_created_date < temp_issue_date:  # Блок сравнения дат
        deadline_var = temp_issue_date - temp_created_date
        print(lg + "↪ Осталось {} дней".format(deadline_var.days))
    elif temp_created_date > temp_issue_date:
        deadline_var = temp_created_date - temp_issue_date
        print(r + "↪ Просрочено на {} дней".format(deadline_var.days))
    else:
        print(r + '↪ Истекает сегодня')


# ФУНКЦИЯ ПОИСКА ЗАМЕТОК
def search_notes(notes_lst, search_keyword=None, search_status=None):
    find = False  # Маркерная переменная результата поиска

    if search_keyword and search_status:  # Если активирован поиск по статусу и ключевому слову
        for iteration, note in enumerate(notes_lst):  # Перебираем список заметок
            themes_str = ', '.join(note.get('Темы'))  # Меняем данные ключа из списка в строку: (..keyword in str..)
            # Если поисковая фраза и статус в соответствующих ключах
            if search_keyword in note.get('Имя пользователя') and search_status == note.get('Статус').lower():
                search_display(note)  # отправляем note в ф-ию display
                find = True  # маркер результата поиска ==> True
            elif search_keyword in note.get('Описание').lower() and search_status == note.get('Статус').lower():
                search_display(note)
                find = True
            elif search_keyword in themes_str and search_status == note.get('Статус').lower():
                search_display(note)
                find = True
    # Следующие блоки устроены по такому же принципу
    elif search_keyword:
        for iteration, note in enumerate(notes_lst):
            themes_str = ', '.join(note.get('Темы'))
            if search_keyword in note.get('Имя пользователя'):
                search_display(note)
                find = True
            elif search_keyword in note.get('Описание').lower():
                search_display(note)
                find = True
            elif search_keyword in themes_str:
                search_display(note)
                find = True

    elif search_status:
        for iteration, note in enumerate(notes_lst):
            if search_status == note.get('Статус').lower():
                search_display(note)
                find = True

    if not find:  # Если ни один блок условий не сработал, то find == False
        print(y + '\nЗАМЕТКИ НЕ НАЙДЕНЫ')


if '__main__' == __name__:

    # Список словарей с предустановленными заметками
    notes_lst = [{'Имя пользователя': 'Влад',
                  'Темы': ['Тестовый заголовок 1 в заметке Влада', 'Тестовый заголовок 2 в заметке Влада'],
                  'Описание': 'Тестовое описание-1 в заметке влада',
                  'Статус': 'Активна',
                  'Создана': '15-12-2024',
                  'Дата завершения': '15-12-2024'
                  },
                 {'Имя пользователя': 'Елена',
                  'Темы': ['Тестовый заголовок 1 в заметке Елены'],
                  'Описание': 'Тестовое описание-2 в заметке Елены',
                  'Статус': 'Отложена',
                  'Создана': '15-12-2024',
                  'Дата завершения': '10-01-2025'
                  }
                 ]

    print(g + '* * ВАС ПРИВЕТСТВУЕТ Ф-ИЯ ПОИСКА ЗАМЕТОК 1.3.4 * *')

    print(c + '\nПрограмма запрашивает ввод ключевого слова и / или статуса.\n'
              'Для отключения модуля поиска — пустой ввод')

    # ПОИСК ПО КЛЮЧЕВОЙ ФРАЗЕ
    search_keyword = input(m + '\nВведите ключевую фразу: ').lower()

    # Если пустая или пробелы => поиск по этому модулю выкл.
    if search_keyword == '' or search_keyword.isspace():
        search_keyword = None
        print(r + '\nПоиск по ключевой фразе выключен')
    else:
        print(g + '\nПоиск по ключевой фразе активирован')

    # ПОИСК ПО СТАТУСУ ЗАМЕТКИ
    print(c + '\nВыберите статус для поиска: '
              '\n○ Активна          — 1; '
              '\n○ Отложена         — 2; '
              '\n○ Выполнена        — 3; '
              '\n○ Ввести статус    — 4.')

    status_search_command = input(m + '\nВведите команду: ')

    # Командное меню поиска по статусу
    if status_search_command == '1':
        search_status = 'активна'
        print(g + '\nПоиск по статусу активирован')

    elif status_search_command == '2':
        search_status = 'отложена'
        print(g + '\nПоиск по статусу активирован')

    elif status_search_command == '3':
        search_status = 'выполнена'
        print(g + '\nПоиск по статусу активирован')

    elif status_search_command == '4':
        search_status = input(m + '\nВведите статус для поиска: ').lower()

        # Если пустая или пробелы => поиск по этому модулю выкл.
        if search_status == '' or search_status.isspace():
            search_status = None
            print(r + '\nПоиск по статусу выключен')

        else:
            print(g + '\nПоиск по статусу активирован')
    else:
        # Если другая команда => поиск по этому модулю выкл.
        search_status = None
        print(r + '\nПоиск по статусу выключен')

    search_notes(notes_lst, search_keyword, search_status)  # Ф-ия поиска
