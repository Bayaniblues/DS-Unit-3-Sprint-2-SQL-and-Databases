import unittest
import sqlite3
import buddymove_holiday


class TestThis(unittest.TestCase):
    def test_chinook(self):
        print(buddymove_holiday.chinook_db)

    def test_new(self):
        print(buddymove_holiday.new_db)

    def total_chars(self):
        print(buddymove_holiday.total_chars())



if __name__ == '__main__':
    unittest.main()