# GRADE 1. ЭТАП 3. Задание 3.

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

# Список словарей с предустановленными заметками
notes_lst = [{'Имя пользователя': 'Влад',
              'Темы': ['Тестовый заголовок 1 в заметке Влада', 'Тестовый заголовок 2 в заметке Влада'],
              'Описание': 'Тестовое описание-1 в заметке влада',
              'Создана': '15-12-2024',
              'Дата завершения': '15-12-2024'
              },
             {'Имя пользователя': 'Елена',
              'Темы': ['Тестовый заголовок 1 в заметке Елены'],
              'Описание': 'Тестовое описание-2 в заметке Елены',
              'Создана': '15-12-2024',
              'Дата завершения': '10-01-2025'
              }
             ]


# ФУНКЦИЯ ОТРИСОВКИ ЗАМЕТОК
def display_notes(notes_lst):
    for iteration, note_in_the_dict in enumerate(notes_lst):
        # Отрисовка всей заметки
        print('⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯')
        print(y + f'Заметка {iteration + 1}')  # Счетчик итератора
        for key, value in note_in_the_dict.items():  # Перебор словаря note
            if isinstance(value, list):  # Если type = list
                print('▶ Тема: '.ljust(22, ' '), '; '.join(value))  # список в строку
            else:
                print(f'▶ {key}:'.ljust(22, ' '), f'{value}')

        # Отрисовка дедлайна
        # Получение временной (temp) текущей даты для вычисления объекта timedelta
        temp_created_date = datetime.datetime.now()
        temp_issue_date = datetime.datetime.strptime(note_in_the_dict['Дата завершения'], "%d-%m-%Y")

        if temp_created_date < temp_issue_date:  # Блок сравнения дат
            deadline_var = temp_issue_date - temp_created_date
            print(lg + "↪ Осталось {} дней".format(deadline_var.days))
        elif temp_created_date > temp_issue_date:
            deadline_var = temp_created_date - temp_issue_date
            print(r + "↪ Просрочено на {} дней".format(deadline_var.days))
        else:
            print(r + '↪ Истекает сегодня')


if '__main__' == __name__:
    print(g + '* * ВАС ПРИВЕТСТВУЕТ Ф-ИЯ ОТРИСОВКИ ЗАМЕТКИ 1.3.3 * *')
    display_notes(notes_lst)
