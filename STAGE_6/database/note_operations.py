import sqlite3
from datetime import datetime
from STAGE_6.S6_utils import validate_status, validate_input, validate_date
from STAGE_6.config import *

# CREATE_NOTE__________________________________________________________________________
def save_note_to_db(db_path):
    note_dct = {'username': '',  # шаблон заметки
                'title': [],
                'content': '',
                'status': '',
                'created_date': '',
                'issue_date': ''}
    # ДОБАВЛЕНИЕ ИМЕНИ_______________________________________________________________
    while True:
        note_dct['username'] = input(MESSAGE_NAME_INP)  # пользовательский ввод

        if validate_input(note_dct['username']):  # обновляем значение ключа username
            break
        else:  # False если пробелы / пустой ввод
            print(MESSAGE_FIELD_EMPTY)
            continue
    # ДОБАВЛЕНИЕ ТЕМ_______________________________________________________________
    print(MESSAGE_CR_TIT)

    title_ticker = 1  # счётчик тем

    while True:
        title = input(f'{MESSAGE_TIT_INP} {title_ticker}: ')  # пользовательский ввод

        if validate_input(title):  # только пробелы / пустой ввод?
            if title.lower() in (item.lower() for item in note_dct['title']):  # Нижний регистр и поиск совпадений
                print(MESSAGE_ERR_TIT_UNIQ)
                continue
            else:
                note_dct['title'].append(title)
                title_ticker = title_ticker + 1
        elif title.isspace():  # если только пробелы
            print(MESSAGE_FIELD_EMPTY)
            continue
        elif title == '' and len(note_dct['title']) > 0:  # пустой ввод и ненулевая длина списка ключа
            break
        else:
            print(MESSAGE_ERR_TIT_EMPTY)
    # ДОБАВЛЕНИЕ ОПИСАНИЯ_______________________________________________________________
    while True:
        note_dct['content'] = input(MESSAGE_DESCR_INP)

        if validate_input(note_dct['content']):
            break
        else:
            print(MESSAGE_ERR_DESCR_EMPTY)
            continue
    # ДОБАВЛЕНИЕ СТАТУСА_______________________________________________________________
    while True:
        print(MESSAGE_CR_STATUS)

        status_command = input(MESSAGE_COMMAND_INP)  # пользовательский ввод

        if status_command == '1':
            note_dct['status'] = 'Активна'
            if validate_status(note_dct):
                break
        elif status_command == '2':
            note_dct['status'] = 'Отложена'
            if validate_status(note_dct):
                break
        elif status_command == '3':
            note_dct['status'] = 'Выполнена'
            if validate_status(note_dct):
                break
        else:
            print(MESSAGE_COMMAND_ERR)
            continue
    # ДОБАВЛЕНИЕ ДАТЫ СОЗДАНИЯ_______________________________________________________________
    note_dct['created_date'] = datetime.strftime(datetime.now(), "%d-%m-%Y")
    # ДОБАВЛЕНИЕ ДАТЫ ЗАВЕРШЕНИЯ_______________________________________________________________
    while True:
        date_input = input(MESSAGE_DATE_INP)

        if validate_date(date_input):
            note_dct['issue_date'] = validate_date(date_input)
            break
        else:
            print(MESSAGE_ERR_DATE_FORMAT)
            continue

    # ДОБАВЛЕНИ В БД_______________________________________________________________
    with sqlite3.connect(db_path) as conn:  # подключение к БД \db_path
        sql_add_note_dct = '''INSERT INTO notes (username, title, content, status, created_date, issue_date)
                            VALUES (?, ?, ?, ?, ?, ?);'''
        cursor = conn.cursor()  # создаём объект курсора
        cursor.execute(sql_add_note_dct,
                       (
                           note_dct['username'],
                           str(note_dct['title']),  # список в строку
                           note_dct['content'],
                           note_dct['status'],
                           note_dct['created_date'],
                           note_dct['issue_date']))
        conn.commit()  # сохранение изменений
    return note_dct


# UPDATE_NOTE__________________________________________________________________________
def update_name_in_db(update_dict, db_path, note_id):
    sql_update_name = '''UPDATE notes SET username = ? WHERE id = ?;'''

    print(MESSAGE_UPD_DB_NAME, update_dict['username'])

    while True:
        update_username = input(MESSAGE_NAME_INP)
        if validate_input(update_username):
            update_dict['username'] = update_username
            break
        else:
            print(MESSAGE_ERR_NAME)
            continue

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_update_name, (update_dict['username'], note_id))
        conn.commit()

def update_title_in_db(update_dict, db_path, note_id):
    sql_update_title = '''UPDATE notes SET title = ? WHERE id = ?;'''

    title_ticker = 1  # Счётчик тем

    print(MESSAGE_UPD_DB_TITLE, update_dict['title'])

    update_dict['title'].clear() # очистка списка ключа

    while True:
        title = input(f'{MESSAGE_TIT_INP} {title_ticker}: ')  # получение заголовков

        if validate_input(title):  # только пробелы / пустой ввод?
            if title.lower() in (item.lower() for item in update_dict['title']):  # Нижний регистр и поиск совпадений
                print(MESSAGE_ERR_TIT_UNIQ)
                continue
            else:
                update_dict['title'].append(title)
                title_ticker = title_ticker + 1

        elif title.isspace():  # только пробелы
            print(MESSAGE_ERR_TIT_SPACE)
            continue
        elif title == '' and len(update_dict['title']) > 0:  # пустой ввод и ненулевая длина списка ключа
            break
        else:
            print(MESSAGE_ERR_TIT_EMPTY)

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_update_title, (str(update_dict['title']), note_id))
        conn.commit()

def update_content_in_db(update_dict, db_path, note_id):
    sql_update_content = '''UPDATE notes SET content = ? WHERE id = ?;'''

    print(MESSAGE_UPD_DB_CONTENT, update_dict['content'])

    while True:
        update_content = input(MESSAGE_DESCR_INP)
        if validate_input(update_content):
            update_dict['content'] = update_content
            break
        else:
            print(MESSAGE_ERR_NAME)
            continue

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_update_content, (update_dict['content'], note_id))
        conn.commit()

def update_status_in_db(update_dict, db_path, note_id):
    sql_update_status = '''UPDATE notes SET status = ? WHERE id = ?;'''

    print(MESSAGE_UPD_DB_STATUS, update_dict['status'])

    while True:
        print(MESSAGE_CR_STATUS)
        status_command = input(MESSAGE_COMMAND_INP)
        if status_command == '1':
            update_dict['status'] = 'Активна'
            if validate_status(update_dict):
                break
        elif status_command == '2':
            update_dict['status'] = 'Отложена'
            if validate_status(update_dict):
                break
        elif status_command == '3':
            update_dict['status'] = 'Выполнена'
            if validate_status(update_dict):
                break
        else:
            print(MESSAGE_COMMAND_ERR)
            continue

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_update_status, (update_dict['status'], note_id))
        conn.commit()

def update_issue_date_in_db(update_dict, db_path, note_id):
    sql_update_issue_date = '''UPDATE notes SET issue_date = ? WHERE id = ?;'''

    print(MESSAGE_UPD_DB_ISSUE_DATE, update_dict['issue_date'])

    while True:
        date_input = input(MESSAGE_DATE_INP)
        if validate_date(date_input):
            update_dict['issue_date'] = validate_date(date_input)
            break
        else:
            print(MESSAGE_ERR_DATE_FORMAT)
            continue
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_update_issue_date, (update_dict['issue_date'], note_id))
        conn.commit()

def update_note_in_db(db_path, note_id=1):
    update_dict = {'username': '', 'title': '', 'content': '', 'status': '', 'issue_date': ''}
    sql_note_by_id = '''SELECT * FROM notes WHERE id = ?'''
    sql_del_select_notes = '''SELECT id FROM notes'''
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_del_select_notes)  # получаем все id заметок
        row = cursor.fetchall()

    index_lst = []  # список всех id
    for i in row:  # распаковка списка кортежей полученных id и добавление в список
        for j in i:
            index_lst.append(j)

    if len(index_lst) > 0:  # ненулевое количество заметок в БД
        try:
            while True:
                print(MESSAGE_UPD_NOTES_DB, index_lst)
                print(MESSAGE_ID_DEL_NOTES_DB)
                note_id = int(input(MESSAGE_COMMAND_INP))
                if note_id in index_lst:  # проверка наличия id
                    break
                else:
                    print(MESSAGE_ACCEPT_FALSE)
                    return None
        except ValueError:
            print(MESSAGE_ACCEPT_FALSE)
            return None

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_note_by_id, (note_id,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                update_dict['username'] = row[1]
                update_dict['title'] = eval(row[2])
                update_dict['content'] = row[3]
                update_dict['status'] = row[4]
                update_dict['issue_date'] = row[6]
        else:
            print(MESSAGE_LST_EMPTY)
            return False

    print(MESSAGE_UPD_FLD)
    while True:
        choice_update = input(MESSAGE_COMMAND_INP)
        if choice_update == '1':
            update_name_in_db(update_dict, db_path, note_id)
            break
        elif choice_update == '2':
            update_title_in_db(update_dict, db_path, note_id)
            break
        elif choice_update == '3':
            update_content_in_db(update_dict, db_path, note_id)
            break
        elif choice_update == '4':
            update_status_in_db(update_dict, db_path, note_id)
            break
        elif choice_update == '5':
            update_issue_date_in_db(update_dict, db_path, note_id)
            break
        elif choice_update == '6':
            update_name_in_db(update_dict, db_path, note_id)
            update_title_in_db(update_dict, db_path, note_id)
            update_content_in_db(update_dict, db_path, note_id)
            update_status_in_db(update_dict, db_path, note_id)
            update_issue_date_in_db(update_dict, db_path, note_id)
            break
        else:
            print(MESSAGE_COMMAND_ERR)



# LOAD_NOTE__________________________________________________________________________
def load_notes_from_db(db_path):
    sql_load_notes_lst = "SELECT * FROM notes;"

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_load_notes_lst)
        rows = cursor.fetchall()

        notes_lst = []
        if rows:
            for row in rows:
                notes_lst.append({'id': row[0],
                                    'username': row[1],
                                    'title': eval(row[2]),  # str в list
                                    'content': row[3],
                                    'status': row[4],
                                    'created_date': row[5],
                                    'issue_date': row[6],})
            return notes_lst
        else:
            print(MESSAGE_LST_EMPTY)
            return []



# УДАЛЕНИЕ ЗАМЕТОК_________________________________________________________________________________
def delete_note_from_db(db_path):
        sql_del_select_notes = '''SELECT id FROM notes'''
        sql_del_delete_notes = '''DELETE FROM notes WHERE id = ?;'''
        sql_del_sequence_notes = '''DELETE FROM SQLITE_SEQUENCE WHERE NAME = 'notes';'''

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_del_select_notes)  # получаем все id заметок
            row = cursor.fetchall()

        index_lst = []  # список всех id
        for i in row:       # распаковка списка кортежей полученных id и добавление в список
            for j in i:
                index_lst.append(j)

        if len(index_lst) > 0:  # ненулевое количество заметок в БД
            try:
                while True:
                    print(MESSAGE_DEL_NOTES_DB, index_lst)
                    print(MESSAGE_ID_DEL_NOTES_DB)
                    note_id = int(input(MESSAGE_COMMAND_INP))
                    if note_id in index_lst:    # проверка наличия id
                        break
                    else:
                        print(MESSAGE_ACCEPT_FALSE)
                        return None
            except ValueError:
                print(MESSAGE_ACCEPT_FALSE)
                return None

            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_del_delete_notes, (note_id,))   # удаление по id
                cursor.execute(sql_del_sequence_notes) # обновление ID заметок в БД
                conn.commit()
        else:
            print(MESSAGE_LST_EMPTY)



# ПОИСК ПО КЛЮЧЕВОМУ СЛОВУ_______________________________________________________________________
def search_notes_by_keyword(db_path):
    sql_search_keyword = '''SELECT * FROM notes 
                            WHERE username 
                            LIKE ? OR title LIKE ? OR content LIKE ?;
                         '''
    while True:
        keyword = input(MESSAGE_SEARCH_KEY)
        if validate_input(keyword):
            break
        else:
            print(MESSAGE_FIELD_EMPTY)
            continue

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_search_keyword, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        rows = cursor.fetchall()
        if rows:    # проверка на пустоту
            return [{'id': row[0], 'username': row[1], 'title': row[2], 'content': row[3], 'status': row[4],
                     'created_date': row[5], 'issue_date': row[6]} for row in rows]
        else:
            print(MESSAGE_LST_EMPTY)
            return []


# ПОИСК ПО СТАТУСУ_______________________________________________________________________
def filter_notes_by_status(db_path, status=''):
    sql_search_status = '''SELECT * FROM notes WHERE status LIKE ?;'''
    while True:
        print(MESSAGE_CR_STATUS)
        status_command = input(MESSAGE_COMMAND_INP)
        if status_command == '1':
            status = 'Активна'
            break
        elif status_command == '2':
            status = 'Отложена'
            break
        elif status_command == '3':
            status = 'Выполнена'
            break
        else:
            print(MESSAGE_COMMAND_ERR)
            continue

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_search_status, (f"%{status}%",))
        rows = cursor.fetchall()
        if rows:
            return [{'id': row[0], 'username': row[1], 'title': row[2], 'content': row[3], 'status': row[4],
                     'created_date': row[5], 'issue_date': row[6]} for row in rows]
        else:
            print(MESSAGE_LST_EMPTY)
            return []

if __name__ == "__main__":

    # print(filter_notes_by_status('nt_mngr_dtbs.db', status=''))

    # print(search_notes_by_keyword('nt_mngr_dtbs.db', keyword=''))

    # delete_note_from_db('nt_mngr_dtbs.db', 1)

    # save_note_to_db('nt_mngr_dtbs.db')

    update_note_in_db('nt_mngr_dtbs.db', 1)

    # print(load_notes_from_db('nt_mngr_dtbs.db'))
