from pagination import *


def validate_date(date_input):
    try:
        temp_issue_date = datetime.strptime(date_input, "%d-%m-%Y")
        issue_date = datetime.strftime(temp_issue_date, "%d-%m-%Y")  # дата в строку
        return issue_date
    except ValueError:
        return False


# ФУНКЦИЯ ПОИСКА ЗАМЕТОК
def filters_notes(notes_lst):
    filtered_notes_lst = []
    while True:
        print(MESSAGE_FILTER)

        filter_command = input(MESSAGE_COMMAND_INP)

        if filter_command == '1':
            search_keyword = input(MESSAGE_SEARCH_KEY).lower()
            if search_keyword.split() != '':  # Если пустая или пробелы => поиск по этому модулю выкл.
                for note in notes_lst:
                    themes_str = ', '.join(note.get('title'))
                    if search_keyword in note.get('username').lower().replace(', ', ' ').split():
                        filtered_notes_lst.append(note)
                        return filtered_notes_lst
                    elif search_keyword in note.get('content').lower().replace(', ', ' ').split():
                        filtered_notes_lst.append(note)
                        return filtered_notes_lst
                    elif search_keyword in themes_str.lower().replace(', ', ' ').split():
                        filtered_notes_lst.append(note)
                        return filtered_notes_lst
                    else:
                        return []
            else:
                handle_error('field_empty')

        elif filter_command == '2':
            # ПОИСК ПО СТАТУСУ ЗАМЕТКИ
            print(MESSAGE_SEARCH_STATUS_NOTE)

            status_search_command = input(MESSAGE_COMMAND_INP)

            if status_search_command == '1':  # Командное меню поиска по статусу
                search_status = 'активна'
            elif status_search_command == '2':
                search_status = 'отложена'
            elif status_search_command == '3':
                search_status = 'выполнена'
            else:
                return []

            return [note for note in notes_lst if note['status'].lower() == search_status]

        # ПОИСК ПО ДАТЕ ЗАМЕТКИ
        elif filter_command == '3':
            print(MESSAGE_DATE_INP)
            date_search_command = input(MESSAGE_COMMAND_INP)
            if validate_date(date_search_command):
                return [note for note in notes_lst if note['created_date'] == date_search_command]
            else:
                return []
        else:
            handle_error('command_error')


if '__main__' == __name__:
    # Список словарей с предустановленными заметками
    notes_lst = [{'username': 'Влад',
                  'title': ['Тестовый заголовок 1 в заметке Влада', 'Тестовый заголовок 2 в заметке Влада'],
                  'content': 'Тестовое описание-1 в заметке влада',
                  'status': 'Отложена',
                  'created_date': '15-12-2024',
                  'issue_date': '15-12-2024'
                  },
                 {'username': 'Елена',
                  'title': ['Тестовый заголовок 1 в заметке Елены'],
                  'content': 'Тестовое описание-2 в заметке Елены',
                  'status': 'Выполнена',
                  'created_date': '15-12-2024',
                  'issue_date': '10-01-2025'
                  }
                 ]

    pagination(filters_notes(notes_lst))
    # Ф-ия поиска
