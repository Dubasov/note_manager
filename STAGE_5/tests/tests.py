import unittest
from STAGE_5.data.file_handling import *
from datetime import datetime

class TestNoteManager(unittest.TestCase):
    def test_write_and_read_notes(self):
        notes = [{'username': 'Test', 'title': 'Test Note'}]
        write_json(notes, 'test.json')
        notes_lst = read_json('test.json')
        self.assertEqual(notes, notes_lst)

    def test_create_name(self):
        add_note_dict1 = {   "Имя пользователя": '1',
                            "Темы": [],
                            "Описание": '',
                            "Статус": '',
                            "Создана": '',
                            "Дата завершения": ''}
        add_note_dict = {"Имя пользователя": '',
                          "Темы": [],
                          "Описание": '',
                          "Статус": '',
                          "Создана": '',
                          "Дата завершения": ''}
        self.assertEqual(create_name(add_note_dict), add_note_dict1)

    def test_create_tittles(self):
        add_note_dict1 = {   "Имя пользователя": '',
                            "Темы": ['1'],
                            "Описание": '',
                            "Статус": '',
                            "Создана": '',
                            "Дата завершения": ''}
        add_note_dict = {"Имя пользователя": '',
                          "Темы": [],
                          "Описание": '',
                          "Статус": '',
                          "Создана": '',
                          "Дата завершения": ''}
        self.assertEqual(create_tittles(add_note_dict), add_note_dict1)

    def test_create_description(self):
        add_note_dict1 = {   "Имя пользователя": '',
                            "Темы": [],
                            "Описание": '1',
                            "Статус": '',
                            "Создана": '',
                            "Дата завершения": ''}
        add_note_dict = {"Имя пользователя": '',
                          "Темы": [],
                          "Описание": '',
                          "Статус": '',
                          "Создана": '',
                          "Дата завершения": ''}
        self.assertEqual(create_description(add_note_dict), add_note_dict1)

    def test_create_status(self):
        add_note_dict1 = {   "Имя пользователя": '',
                            "Темы": [],
                            "Описание": '',
                            "Статус": 'Активна',
                            "Создана": '',
                            "Дата завершения": ''}
        add_note_dict = {"Имя пользователя": '',
                          "Темы": [],
                          "Описание": '',
                          "Статус": '',
                          "Создана": '',
                          "Дата завершения": ''}
        self.assertEqual(create_status(add_note_dict), add_note_dict1)

    def test_create_issue_date(self):
        add_note_dict1 = {   "Имя пользователя": '',
                            "Темы": [],
                            "Описание": '',
                            "Статус": '',
                            "Создана": '',
                            "Дата завершения": '12-12-2024'}
        add_note_dict = {"Имя пользователя": '',
                          "Темы": [],
                          "Описание": '',
                          "Статус": '',
                          "Создана": '',
                          "Дата завершения": ''}
        self.assertEqual(create_issue_date(add_note_dict), add_note_dict1)

    def test_create_now_date(self):
        add_note_dict1 = {   "Имя пользователя": '',
                            "Темы": [],
                            "Описание": '',
                            "Статус": '',
                            "Создана": datetime.strftime(datetime.now(), "%d-%m-%Y"),
                            "Дата завершения": ''}
        add_note_dict = {"Имя пользователя": '',
                          "Темы": [],
                          "Описание": '',
                          "Статус": '',
                          "Создана": '',
                          "Дата завершения": ''}
        self.assertEqual(create_now_date(add_note_dict), add_note_dict1)

    def test_delete_note(self):
        notes_lst1 = []
        notes_lst = [{"Имя пользователя": 'Влад',
                          "Темы": ['Влад'],
                          "Описание": 'Влад',
                          "Статус": 'Активна',
                          "Создана": '12-12-2024',
                          "Дата завершения": '12-12-2025'}]
        self.assertEqual(delete_notes(notes_lst), notes_lst1)


    def test_search_notes(self):
        searched_notes = [1]
        notes_lst = [{"Имя пользователя": 'Влад',
                          "Темы": ['Влад'],
                          "Описание": 'Влад',
                          "Статус": 'Активна',
                          "Создана": '12-12-2024',
                          "Дата завершения": '12-12-2025'}]
        self.assertEqual(search_notes(notes_lst), searched_notes)


    def validate_date(self):
        date = '12-12-2024'
        res = validate_date(date)
        self.assertEqual(validate_date(date), res)

    def validate_status(self):
        status = 'Активна'
        res = validate_status(status)
        self.assertEqual(validate_date(status), res)


if __name__ == '__main__':
    unittest.main()


