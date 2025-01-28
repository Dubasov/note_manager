from STAGE_6.S6_utils import console_resume, notes_display
from STAGE_6.database import *


setup_database()

while True:
    print(MESSAGE_MENU_DB)

    command_menu = input(MESSAGE_COMMAND_INP)

    # ____КОМАНДА 1______Добавление новой заметки
    if command_menu == '1':
        save_note_to_db('nt_mngr_dtbs.db')
        console_resume()
    # ____КОМАНДА 2______Показать список заметок
    elif command_menu == '2':
        searched_notes = []
        for iteration, note in enumerate(load_notes_from_db('nt_mngr_dtbs.db'), start = 1):
            searched_notes.append(iteration)
            notes_display(note, iteration)
        searched_notes.clear()
        console_resume()
    # ____КОМАНДА 3______Редактирование заметки
    elif command_menu == '3':
        update_note_in_db('nt_mngr_dtbs.db',1 )
        console_resume()
    # ____КОМАНДА 4______Удаление заметки
    if command_menu == '4':
        delete_note_from_db('nt_mngr_dtbs.db')
        console_resume()
    # ____КОМАНДА 5______Найти заметку по ключу
    elif command_menu == '5':
        searched_notes = []
        for iteration, note in enumerate(search_notes_by_keyword('nt_mngr_dtbs.db'), start = 1):
            searched_notes.append(iteration)
            notes_display(note, iteration)
        searched_notes.clear()
        console_resume()
    # ____КОМАНДА 6______Найти заметку по статусу
    elif command_menu == '6':
        searched_notes = []
        for iteration, note in enumerate(filter_notes_by_status('nt_mngr_dtbs.db', status=''), start = 1):
            searched_notes.append(iteration)
            notes_display(note, iteration)
        searched_notes.clear()
        console_resume()
    # ____КОМАНДА 7______Завершение программы
    elif command_menu == '7':
        break
    else:
        print(MESSAGE_COMMAND_ERR)  # >> такой команды не существует




