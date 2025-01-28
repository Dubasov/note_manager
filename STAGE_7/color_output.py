from datetime import datetime  # Работа с датами
from config import *
from pagination import pagination
init(autoreset=True)  # Авто сброс покраски строчек


def display_notes_with_colors(note, value):
    """Цветной вывод статуса заметки"""
    if note.get('status') == 'Активна':
        print(f'▶ Статус: '.ljust(22, ' '), clr_BLU + f'{value}')
    elif note.get('status') == 'Выполнена':
        print(f'▶ Статус: '.ljust(22, ' '), clr_LIGHGRE + f'{value}')
    elif note.get('status') == 'Отложена':
        print(f'▶ Статус: '.ljust(22, ' '), clr_RED + f'{value}')


def display_notes_s7_demonstrate(note, note_id):
    print(MESSAGE_DISP_SEP)  # >> ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
    print(clr_YEL + f'Заметка: {note_id}')
    for key, value in note.items():  # Перебор словаря note
        if isinstance(value, list):  # Если type = list
            print('▶ Тема: '.ljust(22, ' '), '; '.join(value))  # список в строку
        else:
            if key == 'ID':
                pass
            elif key == 'username':
                print(f'▶ Имя пользователя: '.ljust(22, ' '), f'{value}')
            elif key == 'content':
                print(f'▶ Описание: '.ljust(22, ' '), f'{value}')
            elif key == 'status':
                display_notes_with_colors(note, value)
            elif key == 'created_date':
                print(f'▶ Создана: '.ljust(22, ' '), f'{value}')
            elif key == 'issue_date':
                print(f'▶ Дата завершения: '.ljust(22, ' '), f'{value}')

    # ДЕДЛАЙН
    temp_created_date = datetime.now()
    temp_issue_date = datetime.strptime(note['issue_date'], "%d-%m-%Y")

    if temp_created_date < temp_issue_date:  # Блок сравнения дат
        if note.get('status') != 'Выполнена':
            deadline_var = temp_issue_date - temp_created_date
            print(MESSAGE_DISP_BEF.format(deadline_var.days))  # >> Осталось {} дней
    elif temp_created_date > temp_issue_date:
        if note.get('status') != 'Выполнена':
            deadline_var = temp_created_date - temp_issue_date
            print(MESSAGE_DISP_AFT.format(deadline_var.days))  # >> Просрочено на {} дней
    else:
        if note.get('status') != 'Выполнена':
            print(MESSAGE_DISP_TOD)  # >> Истекает сегодня




if '__main__' == __name__:
    # Список словарей с предустановленными заметками
    notes_lst = [{'username': 'Влад',
                  'title': ['Тестовый заголовок 1 в заметке Влада', 'Тестовый заголовок 2 в заметке Влада'],
                  'content': 'Тестовое описание-1 в заметке влада',
                  'status': 'Отложена',
                  'create_date': '15-12-2024',
                  'issue_date': '15-12-2024'
                  },
                 {'username': 'Елена',
                  'title': ['Тестовый заголовок 1 в заметке Елены'],
                  'content': 'Тестовое описание-2 в заметке Елены',
                  'status': 'Выполнена',
                  'create_date': '15-12-2024',
                  'issue_date': '10-01-2025'
                  },
                 {'username': 'Павел',
                  'title': ['Тестовый заголовок 3 в заметке Павла'],
                  'content': 'Тестовое описание-2 в заметке Павла',
                  'status': 'Активна',
                  'create_date': '15-12-2024',
                  'issue_date': '10-01-2025'
                  },
                 {'username': 'we',
                  'title': ['Тестовый заголовок 1 в заметке Влада', 'Тестовый заголовок 2 в заметке Влада'],
                  'content': 'Тестовое описание-1 в заметке влада',
                  'status': 'Отложена',
                  'create_date': '15-12-2024',
                  'issue_date': '15-12-2024'
                  },
                 {'username': 'wqe',
                  'title': ['Тестовый заголовок 1 в заметке Елены'],
                  'content': 'Тестовое описание-2 в заметке Елены',
                  'status': 'Выполнена',
                  'create_date': '15-12-2024',
                  'issue_date': '10-01-2025'
                  },
                 {'username': 'wqeqwe',
                  'title': ['Тестовый заголовок 3 в заметке Павла'],
                  'content': 'Тестовое описание-2 в заметке Павла',
                  'status': 'Активна',
                  'create_date': '15-12-2024',
                  'issue_date': '10-01-2025'
                  }
                 ]

    searched_notes = []
    for iteration, note in enumerate(pagination(notes_lst)):
        note_id = iteration + 1
        searched_notes.append(note_id)


        display_notes_s7_demonstrate(note, note_id)