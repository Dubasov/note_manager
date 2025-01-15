from datetime import datetime
import json
from STAGE_5.utils.validate_input import validate_input
from STAGE_5.utils.validate_date import validate_date
from STAGE_5.interface.display_notes import notes_display
from STAGE_5.interface.search_notes import search_notes
from STAGE_5.utils.validate_status import validate_status
from STAGE_5.utils.generate_unique_id import generate_unique_id
from STAGE_5.config import *

def create_id( add_note_dict):
    add_note_dict['ID'] = generate_unique_id()

def create_name(add_note_dict):
    while True:
        add_note_dict['Имя пользователя'] = input(MESSAGE_NAME_INP)  # получение имени
        if validate_input(add_note_dict['Имя пользователя']):  # проверка ввода
            return add_note_dict
        else:
            print(MESSAGE_ERR_NAME)
            continue

def create_tittles(add_note_dict):
    print(MESSAGE_CR_TIT)

    # add_note_dict['Темы'] = []  # список тем

    title_ticker = 1  # Переменная счётчик введённых заголовков
    while True:
        title = input(f'{MESSAGE_TIT_INP} {title_ticker}: ')  # получение заголовков

        if validate_input(title):  # проверка ввода
            if title.lower() in (item.lower() for item in add_note_dict['Темы']):  # Поиск совпадений
                print(MESSAGE_ERR_TIT_UNIQ)  # найдено совпадение (повтор)
                continue
            else:
                add_note_dict['Темы'].append(title)  # заголовки уникальны (добавление в список)
                title_ticker = title_ticker + 1
        elif title.isspace():  # Если только пробел\ы
            print(MESSAGE_ERR_TIT_SPACE)  # ошибка темы (только пробелы)
            continue
        elif title == '' and len(add_note_dict['Темы']) > 0:  # завершение ввода
            return add_note_dict
        else:
            print(MESSAGE_ERR_TIT_EMPTY)  # ошибка пустого списка

def create_description(add_note_dict):
    while True:
        add_note_dict['Описание'] = input(MESSAGE_DESCR_INP)
        if validate_input(add_note_dict['Описание']):
            return add_note_dict
        else:
            print(MESSAGE_ERR_DESCR_EMPTY)
            continue

def create_status(add_note_dict):
    while True:
        print(MESSAGE_CR_STATUS)
        status_command = input(MESSAGE_COMMAND_INP)  # пользовательский ввод
        if status_command == '1':
            add_note_dict['Статус'] = 'Активна'  # добавление статуса "Активна"
            if validate_status(add_note_dict):
                return add_note_dict
        elif status_command == '2':  # добавление статуса "Отложена"
            add_note_dict['Статус'] = 'Отложена'
            if validate_status(add_note_dict):
                return add_note_dict
        elif status_command == '3':  # добавление статуса "Выполнена"
            add_note_dict['Статус'] = 'Выполнена'
            if validate_status(add_note_dict):
                return add_note_dict
        else:
            print(MESSAGE_COMMAND_ERR)
            continue

def create_now_date(add_note_dict):
    add_note_dict['Создана'] = datetime.strftime(datetime.now(), "%d-%m-%Y")  # текущая дата
    return add_note_dict

def create_issue_date(add_note_dict):
    while True:
        date_input = input(MESSAGE_DATE_INP)
        if validate_date(date_input):
            add_note_dict['Дата завершения'] = validate_date(date_input)
            return add_note_dict
        else:
            print(MESSAGE_ERR_DATE_FORMAT)
            continue

# ФУНКЦИЯ СОЗДАНИЯ
def create_note():
    add_note_dict =     {'ID': '',
                        'Имя пользователя': '',
                        'Темы': [],
                        'Описание': '',
                        'Статус': '',
                        'Создана': '',
                        'Дата завершения': ''}  # Объявление словаря внутри функции

    print(MESSAGE_CR_NOTE)
    create_id(add_note_dict)
    create_name(add_note_dict)   # имя
    create_tittles(add_note_dict) # темы
    create_description(add_note_dict) # описание
    create_status(add_note_dict) # статус
    create_now_date(add_note_dict) # настоящая дата
    create_issue_date(add_note_dict) # дата завершения
    return add_note_dict

# ФУНКЦИЯ РЕДАКТИРОВАНИЯ
def update_note(notes_lst):
    print(MESSAGE_UPD_NOTE)
    searched_notes = []
    for iteration, note in enumerate(notes_lst):
        note_id = iteration + 1
        searched_notes.append(note_id)
        notes_display(note, note_id)

    while True:  # есть ли команда в списке доступных индексов
        print(f'{MESSAGE_UPD_NOTE_NUM_INP}. Доступные значения {searched_notes}')
        try:
            change_note = input(MESSAGE_COMMAND_INP)  # Выбор заметки для обновления
            if int(change_note) in searched_notes:
                add_note_dict = notes_lst[(int(change_note) - 1)]
                break
            else:
                print(MESSAGE_COMMAND_ERR)
                continue
        except ValueError:
            print(MESSAGE_COMMAND_ERR)
            continue

    # МЕНЮ КОМАНД ДЛЯ ВЫБОРА ПОЛЯ ДЛЯ РЕДАКТИРОВАНИЯ
    while True:
        print(MESSAGE_UPD_FLD)
        key_changer = input(MESSAGE_COMMAND_INP)  # Ввод команды

        # ______КОМАНДА 1_________Изменение имени пользователя
        if key_changer == '1':
            create_name(add_note_dict)
            break
        # ______КОМАНДА 2_________Изменение тем
        elif key_changer == '2':
            add_note_dict['Темы'] = []
            create_tittles(add_note_dict)
            break
        # ______КОМАНДА 3_________Изменение описания
        elif key_changer == '3':
            create_description(add_note_dict)
            break
        #______КОМАНДА 4_________ Изменение статуса
        elif key_changer == '4':
            create_status(add_note_dict)
            break
        # ______КОМАНДА 5_________Изменение даты
        elif key_changer == '5':
            create_issue_date(add_note_dict)
            break
        # ______КОМАНДА 6_________Изменение всех полей
        elif key_changer == '6':
            create_name(add_note_dict)
            add_note_dict['Темы'] = []
            create_tittles(add_note_dict)
            create_description(add_note_dict)
            create_status(add_note_dict)
            create_issue_date(add_note_dict)
            break
        else:
            print(MESSAGE_COMMAND_ERR)
            continue
    searched_notes.clear()

# ФУНКЦИЯ УДАЛЕНИЯ
def delete_notes(notes_lst):
    if not len(notes_lst) == 0:
        print(MESSAGE_DEL_NOTE)  #>> раздел удаление заметок
        while True:
            print(MESSAGE_DEL_FLD) #>> выбрать заметку или найти заметку для удаления
            command_delete = input(MESSAGE_COMMAND_INP)  #>> введите команду

            if command_delete == '1':
                searched_notes = []
                for iteration, note in enumerate(notes_lst):
                    note_id = iteration + 1
                    searched_notes.append(note_id)
                    notes_display(note, note_id)
                flag_break = False

                while True:
                    print(c + f'Введите номер заметки для удаления. '
                              f'Доступные значения {searched_notes}')
                    try:
                        note_change_command = int(input(MESSAGE_COMMAND_INP))    #>> введите команду
                        if not note_change_command in searched_notes:
                            print(MESSAGE_COMMAND_ERR)    #>> такой команды не существует
                            continue
                        else:
                            flag_break = True
                            del notes_lst[(note_change_command - 1)]
                            print(lg + f'Заметка {note_change_command} успешно удалена!')
                            break
                    except ValueError:
                        print(MESSAGE_COMMAND_ERR)    #>> такой команды не существует
                if flag_break:
                    searched_notes.clear()
                    break

            elif command_delete == '2':
                flag_break = False
                searched_notes = search_notes(notes_lst)    # функция возвращает список индексов

                if not len(searched_notes) == 0:            # если длина списка индексов не равна 0
                    while True:
                        try:
                            print(c + f'Введите номер заметки для удаления. '
                                      f'Доступные номера:  {searched_notes}')
                            note_change_command = int(input(MESSAGE_COMMAND_INP))    #>> введите команду
                            if int(note_change_command) not in searched_notes:
                                print(MESSAGE_COMMAND_ERR)    #>> такой команды не существует
                                continue
                        except ValueError:
                            print(MESSAGE_COMMAND_ERR)    #>> команда должна быть целым числом
                            continue
                        else:
                            flag_break = True
                            del notes_lst[(note_change_command - 1)]
                            print(lg + f'Заметка {note_change_command} успешно удалена!')
                            break

                    if flag_break:
                        break
                else:   # если длина списка индексов равна 0
                    flag_break = True

                if flag_break:
                    break
            else:
                print(MESSAGE_COMMAND_ERR)    #>> такой команды не существует
                continue
    else:
        print(MESSAGE_LST_EMPTY)   #>> заметки не найдены
    searched_notes.clear()
    return notes_lst

# ФУНКЦИЯ ЧТЕНИЯ ФАЙЛА
def read_json(json_file):
    try:
        with open(f'{json_file}.json', 'r', encoding='utf8') as file:
            notes_lst = json.load(file)
        return notes_lst
    except FileNotFoundError:
        print(MESSAGE_ERR_FILE_NOT_FOUND)  # >> файла не существует
        notes_lst = []
        return notes_lst
    except json.decoder.JSONDecodeError:    # пустой файл
        notes_lst = []
        return notes_lst

# ФУНКЦИЯ ЗАПИСИ
def write_json(notes, json_file):
    try:
        with open(f'{json_file}.json', 'w', encoding='utf8') as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)
    except PermissionError:
        print(MESSAGE_ERR_FILE, json_file)



if '__main__' == __name__:
    notes_lst = [{'Имя пользователя': 'Влад',
                  'Темы': ['Тестовый заголовок 1 в заметке Влада', 'Тестовый заголовок 2 в заметке Влада'],
                  'Описание': 'Тестовое описание-1 в заметке влада',
                  'Статус': 'Отложена',
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

    print(create_note())
    # print(update_note(notes_lst))
    # print(notes_lst)