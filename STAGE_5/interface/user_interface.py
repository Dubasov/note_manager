from STAGE_5.interface.search_notes import search_notes, notes_display
from STAGE_5.data.file_handling import update_note, create_note, delete_notes, write_json
from STAGE_5.utils.console_resume import console_resume
from STAGE_5.config import *

def interface(notes_lst):
    print(MESSAGE_HELLO)  # >>вас приветствует менеджер заметок

    # ___________ОСНОВНОЙ ЦИКЛ ПРОГРАММЫ____________
    while True:

        print(MESSAGE_MENU)  # >> командное меню

        command_add = input(MESSAGE_COMMAND_INP)  # >>введите команду

        # ____КОМАНДА 1______Добавление новой заметки
        if command_add == '1':
            notes_lst.append(create_note())  # Ф-ия добавления
            write_json(notes_lst, 'data_file')
            console_resume()  # Ф-ия паузы

        # ____КОМАНДА 2______Показать список заметок
        elif command_add == '2':
            searched_notes = []
            for iteration, note in enumerate(notes_lst):
                note_id = iteration + 1
                searched_notes.append(note_id)
                notes_display(note, note_id)
            searched_notes.clear()
            console_resume()  # Ф-ия паузы

        # ____КОМАНДА 3______Редактирование заметки
        elif command_add == '3':
            update_note(notes_lst)  # Ф-ия обновления
            write_json(notes_lst, 'data_file')
            console_resume()  # Ф-ия паузы

        # ____КОМАНДА 4______Удаление заметки
        if command_add == '4':
            delete_notes(notes_lst)
            write_json(notes_lst, 'data_file')
            console_resume()  # Ф-ия паузы

        # ____КОМАНДА 5______Найти заметку
        elif command_add == '5':
            search_notes(notes_lst)  # Ф-ия поиска
            console_resume()  # Ф-ия паузы

        elif command_add == '6':
            write_json(notes_lst, 'data_file')
            print(MESSAGE_SAVE_NOTES)
            break

        else:
            print(MESSAGE_COMMAND_ERR)  # >> такой команды не существует
            continue

    return notes_lst


if '__main__' == __name__:
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
                  'Статус': 'Активна',
                  'Создана': '15-12-2024',
                  'Дата завершения': '10-01-2025'
                  },
                 {'Имя пользователя': 'Павел',
                  'Темы': ['Тестовый заголовок 3 в заметке Павла'],
                  'Описание': 'Тестовое описание-3 в заметке Павла',
                  'Статус': 'Отложена',
                  'Создана': '15-12-2024',
                  'Дата завершения': '02-01-2025'
                  },
                 {'Имя пользователя': 'Зульфия',
                  'Темы': ['Тестовый заголовок 4 в заметки Зульфии'],
                  'Описание': 'Тестовое описание-4 в заметке Зульфии',
                  'Статус': 'Выполнена',
                  'Создана': '15-12-2024',
                  'Дата завершения': '01-01-1996'
                  }
                 ]
