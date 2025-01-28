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
        add_note_dict1 = {   "username": '1',
                            "title": [],
                            "content": '',
                            "status": '',
                            "created_date": '',
                            "issue_date": ''}
        add_note_dict = {   "username": '',
                            "title": [],
                            "content": '',
                            "status": '',
                            "created_date": '',
                            "issue_date": ''}
        self.assertEqual(create_name(add_note_dict), add_note_dict1)

    def test_create_tittles(self):
        add_note_dict1 = {   "username": '',
                            "title": ['1'],
                            "content": '',
                            "status": '',
                            "created_date": '',
                            "issue_date": ''}
        add_note_dict = {"Имя пользователя": '',
                          "Темы": [],
                          "Описание": '',
                          "Статус": '',
                          "Создана": '',
                          "Дата завершения": ''}
        self.assertEqual(create_tittles(add_note_dict), add_note_dict1)

    def test_create_description(self):
        add_note_dict1 = {   "username": '1',
                            "title": [],
                            "content": '1',
                            "status": '',
                            "created_date": '',
                            "issue_date": ''}
        add_note_dict = {   "username": '',
                            "title": [],
                            "content": '',
                            "status": '',
                            "created_date": '',
                            "issue_date": ''}
        self.assertEqual(create_description(add_note_dict), add_note_dict1)

    def test_create_status(self):
        add_note_dict1 = {   "username": '',
                            "title": [],
                            "content": '',
                            "status": 'Активна',
                            "created_date": '',
                            "issue_date": ''}
        add_note_dict = {   "username": '',
                            "title": [],
                            "content": '',
                            "status": '',
                            "created_date": '',
                            "issue_date": ''}
        self.assertEqual(create_status(add_note_dict), add_note_dict1)

    def test_create_issue_date(self):
        add_note_dict1 = {   "username": '',
                            "title": [],
                            "content": '',
                            "status": '',
                            "created_date": '',
                            "issue_date": '12-12-2024'}
        add_note_dict = {   "username": '',
                            "title": [],
                            "content": '',
                            "status": '',
                            "created_date": '',
                            "issue_date": ''}
        self.assertEqual(create_issue_date(add_note_dict), add_note_dict1)

    def test_create_now_date(self):
        add_note_dict1 = {   "username": '',
                            "title": [],
                            "content": '',
                            "status": '',
                            "created_date": datetime.strftime(datetime.now(), "%d-%m-%Y"),
                            "issue_date": ''}
        add_note_dict = {   "username": '',
                            "title": [],
                            "content": '',
                            "status": '',
                            "created_date": '',
                            "issue_date": ''}
        self.assertEqual(create_now_date(add_note_dict), add_note_dict1)

    def test_delete_note(self):
        notes_lst1 = []
        notes_lst = [{"username": 'Влад',
                          "title": ['Влад'],
                          "content": 'Влад',
                          "status": 'Активна',
                          "created_date": '12-12-2024',
                          "issue_date": '12-12-2025'}]
        self.assertEqual(delete_notes(notes_lst), notes_lst1)


    def test_search_notes(self):
        searched_notes = [1]
        notes_lst = [{"username": 'Влад',
                          "title": ['Влад'],
                          "content": 'Влад',
                          "status": 'Активна',
                          "created_date": '12-12-2024',
                          "issue_date": '12-12-2025'}]
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


