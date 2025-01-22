import unittest
from STAGE_6.database.note_operations import *
from STAGE_6.database.setup_database import *

setup_database()


class TestNoteManager(unittest.TestCase):

    def test_save_and_load_notes_from_db(self):
        notes_save = save_note_to_db('nt_mngr_dtbs.db')
        notes_load = load_notes_from_db('nt_mngr_dtbs.db')
        for item in notes_load:
            del item['id']
        self.assertEqual(notes_save, notes_load[0])



