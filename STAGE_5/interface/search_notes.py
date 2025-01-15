from STAGE_5.config import *
from STAGE_5.interface.display_notes import notes_display

# ФУНКЦИЯ ПОИСКА ЗАМЕТОК
def search_notes(notes_lst):
    searched_notes = []
    print(MESSAGE_SEARCH_KEY_NOTE)  # >> программа запрашивает ввод ключевого слова и / или...

    # ПОИСК ПО КЛЮЧЕВОЙ
    search_keyword = input(MESSAGE_SEARCH_KEY).lower()  # >> введите ключевую фразу
    if search_keyword == '' or search_keyword.isspace():  # Если пустая или пробелы => поиск по этому модулю выкл.
        search_keyword = None
        print(MESSAGE_SEARCH_KEY_FALSE)  # >> поиск по ключевой фразе выкл
    else:
        print(MESSAGE_SEARCH_KEY_TRUE)  # >> поиск по ключевой фразе вкл

    # ПОИСК ПО СТАТУСУ ЗАМЕТКИ
    print(MESSAGE_SEARCH_STATUS_NOTE)  # >> меню выбора действия для поиска по статусу

    status_search_command = input(MESSAGE_COMMAND_INP)  # >> введите команду

    if status_search_command == '1':  # Командное меню поиска по статусу
        search_status = 'активна'
        print(MESSAGE_SEARCH_STATUS_TRUE)  # >> поиск по статусу вкл
    elif status_search_command == '2':
        search_status = 'отложена'
        print(MESSAGE_SEARCH_STATUS_TRUE)  # >> поиск по статусу вкл
    elif status_search_command == '3':
        search_status = 'выполнена'
        print(MESSAGE_SEARCH_STATUS_TRUE)  # >> поиск по статусу вкл
    else:
        search_status = None  # Если другая команда => поиск по этому модулю выкл.
        print(MESSAGE_SEARCH_STATUS_FALSE)  # >> поиск по статусу выкл

    find = False  # Маркерная переменная результата поиска

    # ЛОГИКА ПОИСКА
    if search_keyword and search_status:  # Если активирован поиск по статусу и ключевому слову
        print(MESSAGE_DISP_RES)  # >> найденные результаты
        for iteration, note in enumerate(notes_lst):  # Перебираем список заметок
            themes_str = ', '.join(note.get('Темы'))  # Меняем данные ключа из списка в строку: (..keyword in str..)

            # Если поисковая фраза и статус в соответствующих ключах
            if search_keyword in note.get('Имя пользователя').lower().replace(', ', ' ').split() and search_status == note.get('Статус').lower():
                note_id = iteration + 1
                searched_notes.append(note_id)
                notes_display(note, note_id)  # отправляем note в ф-ию display
                find = True  # маркер результата поиска ==> True
            elif search_keyword in note.get('Описание').lower().replace(', ', ' ').split() and search_status == note.get('Статус').lower():
                note_id = iteration + 1
                searched_notes.append(note_id)
                notes_display(note, note_id)
                find = True
            elif search_keyword in themes_str.lower().replace(', ', ' ').split() and search_status == note.get('Статус').lower():
                note_id = iteration + 1
                searched_notes.append(note_id)
                notes_display(note, note_id)
                find = True

    # Следующие блоки устроены по такому же принципу
    elif search_keyword:
        print(MESSAGE_DISP_RES)  # >> найденные результаты
        for iteration, note in enumerate(notes_lst):
            themes_str = ', '.join(note.get('Темы'))
            if search_keyword in note.get('Имя пользователя').lower().replace(', ', ' ').split():
                note_id = iteration + 1
                searched_notes.append(note_id)
                notes_display(note, note_id)
                find = True
            elif search_keyword in note.get('Описание').lower().replace(', ', ' ').split():
                note_id = iteration + 1
                searched_notes.append(note_id)
                notes_display(note, note_id)
                find = True
            elif search_keyword in themes_str.lower().replace(', ', ' ').split():
                note_id = iteration + 1
                searched_notes.append(note_id)
                notes_display(note, note_id)
                find = True

    elif search_status:
        print(MESSAGE_DISP_RES)  # >> найденные результаты
        for iteration, note in enumerate(notes_lst):
            if search_status == note.get('Статус').lower():
                note_id = iteration + 1
                searched_notes.append(note_id)
                notes_display(note, note_id)
                find = True

    if not find:  # Если ни один блок условий не сработал, то find == False
        print(MESSAGE_LST_EMPTY)  # >> заметки не найдены
    return searched_notes

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
                  'Статус': 'Выполнена',
                  'Создана': '15-12-2024',
                  'Дата завершения': '10-01-2025'
                  }
                 ]

    print(g + '* * ВАС ПРИВЕТСТВУЕТ Ф-ИЯ ПОИСКА ЗАМЕТОК 1.3.4 * *')

    search_notes(notes_lst)  # Ф-ия поиска
