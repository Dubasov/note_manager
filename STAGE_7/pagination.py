from datetime import datetime
from config import *
from error_handling_ui import handle_error


def display_notes_with_colors(note, value):
    """Отображение статуса заметки в цвете (совместимо с display_notes STAGE_7)"""
    if note.get('status') == 'Активна':
        print(f'▶ Статус: '.ljust(22, ' '), clr_BLU + f'{value}')
    elif note.get('status') == 'Выполнена':
        print(f'▶ Статус: '.ljust(22, ' '), clr_LIGHGRE + f'{value}')
    elif note.get('status') == 'Отложена':
        print(f'▶ Статус: '.ljust(22, ' '), clr_RED + f'{value}')


def display_notes(notes_lst, page, notes_per_page):
    """Функция отображения заметок с пагинацией (совместимо с pagination STAGE_7)"""
    start = (page - 1) * notes_per_page  # Стартовый индекс заметки
    end = start + notes_per_page  # Последний индекс заметки
    page_notes = notes_lst[start:end]  # Диапазон на странице

    for iteration, note in enumerate(page_notes, start + 1):
        print(clr_YEL + f'Заметка: {iteration}')
        print(MESSAGE_DISP_SEP)
        for key, value in note.items():  # Перебор словаря note
            if key == 'ID':
                pass
            elif key == 'username':
                print(f'▶ Имя пользователя: '.ljust(22, ' '), f'{value}')
            elif key == 'content':
                print(f'▶ Описание: '.ljust(22, ' '), f'{value}')
            elif key == 'title':
                print('▶ Тема: '.ljust(22, ' '), '; '.join(value))  # список в строку
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


def pagination(notes_lst):
    """Функция пагинации заметок (совместимо с display_notes STAGE_7)"""
    page = 1
    notes_per_page = 2  # количество заметок на страницу
    if len(notes_lst) > 0:
        command_page_next = ['n', 'т']
        command_page_back = ['b', 'и']
        total_pages = (len(notes_lst) + notes_per_page - 1) // notes_per_page
        while True:
            display_notes(notes_lst, page, notes_per_page)

            # Меню пагинации
            print(Fore.LIGHTBLUE_EX + f'\n| Страница {page} из {total_pages} |')
            print(MESSAGE_PAGINATION)
            command_page = input(MESSAGE_COMMAND_INP).lower()

            if command_page in command_page_next and page < total_pages:
                page += 1
                continue
            elif command_page in command_page_back and 1 < page < total_pages:
                page -= 1
                continue
            elif command_page == 'q' or command_page == 'й':
                break
            else:
                handle_error('command_error')
    else:
        handle_error('empty_list')


if __name__ == '__main__':
    notes_lst = [{'username': '1',
                  'title': ['1', '1'],
                  'content': '1',
                  'status': 'Отложена',
                  'create_date': '15-12-2024',
                  'issue_date': '15-12-2024'
                  },
                 {'username': '2',
                  'title': ['2'],
                  'content': '2',
                  'status': 'Выполнена',
                  'create_date': '15-12-2024',
                  'issue_date': '10-01-2025'
                  },
                 {'username': '3',
                  'title': ['3'],
                  'content': '3',
                  'status': 'Активна',
                  'create_date': '15-12-2024',
                  'issue_date': '10-01-2025'
                  },
                 {'username': '4',
                  'title': ['4', '4'],
                  'content': '4',
                  'status': 'Отложена',
                  'create_date': '15-12-2024',
                  'issue_date': '15-12-2024'
                  },
                 {'username': '5',
                  'title': ['5'],
                  'content': '5',
                  'status': 'Выполнена',
                  'create_date': '15-12-2024',
                  'issue_date': '10-01-2025'
                  },
                 {'username': '6',
                  'title': ['6'],
                  'content': '6',
                  'status': 'Активна',
                  'create_date': '15-12-2024',
                  'issue_date': '10-01-2025'
                  }
                 ]

    pagination(notes_lst)
