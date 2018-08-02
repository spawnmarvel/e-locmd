import unittest
from app.e_lo_db import db_handler

class TestDB(unittest.TestCase):

    def setUp(self):
        db_handler.init_db_book()

    def test_insert_book(self):
        title = "Hobbes.txt"
        note = "Hobbes has some txt"
        rv = db_handler.insert_book(title, note)
        rv1 = "Db txt saved"
        self.assertEqual(rv, rv1)


    def test_select_book(self):
        tmp = db_handler.select_book("Hobbes.txt")
        book = tmp[1]
        self.assertEqual(book, "Hobbes.txt")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
