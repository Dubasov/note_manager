from STAGE_7.error_handling_ui import handle_error
from STAGE_7.pagination import pagination
from config import *
from datetime import datetime
from STAGE_5.data.file_handling import create_note, delete_notes, update_note


def validate_date(date_input):
    try:
        temp_issue_date = datetime.strptime(date_input, "%d-%m-%Y")
        issue_date = datetime.strftime(temp_issue_date, "%d-%m-%Y")  # дата в строку
        return issue_date
    except ValueError:
        return False


def main_menu(notes_lst):
    while True:
        print(clr_CYA + 'Добавить заметку         - 1\n'
                        'Посмотреть заметки       - 2\n'
                        'Редактировать заметку    - 3\n'
                        'Удалить заметку          - 4\n'
                        'Завершить работу         - 5\n')

        command_menu = input(MESSAGE_COMMAND_INP)

        # ____КОМАНДА 1______Добавление новой заметки
        if command_menu == '1':
            notes_lst.append(create_note())
            continue
        # ____КОМАНДА 2______Показать список заметок
        elif command_menu == '2':
            pagination(notes_lst)
            continue
        # ____КОМАНДА 3______Редактирование заметки
        elif command_menu == '3':
            update_note(notes_lst)
            continue
        # ____КОМАНДА 4______Удаление заметки
        if command_menu == '4':
            delete_notes(notes_lst)
            continue
        # ____КОМАНДА 7______Завершение программы
        elif command_menu == '5':
            break
        else:
            handle_error('command_error')


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
    main_menu(notes_lst)
