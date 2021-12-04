import unittest
import db
import sqlite3


class Test_TestGameboard(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect('sqlite_db')

    def tearDown(self):
        self.conn.close()

    def test_init(self):
        # test init_db method
        db.clear()
        db.init_db()
        db.init_db()
        c = self.conn.cursor()
        # get the count of tables with the name
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' "
                  "AND name='GAME'")

        # if the count is 1, then table exists
        self.assertEqual(c.fetchone()[0], 1)

        db.clear()

    def test_clear(self):
        # test init_clear method
        db.init_db()
        db.clear()
        c = self.conn.cursor()
        # get the count of tables with the name
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' "
                  "AND name='GAME'")

        # if the count is 1, then table exists
        self.assertEqual(c.fetchone()[0], 0)

    def test_add_move(self):
        # test add_move
        db.clear()
        db.init_db()
        db.add_move(("", "", "", "", 112, 123))
        db.add_move(("", "", "", "", "", 12))
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM GAME WHERE remaining_moves = 12')
        self.assertEqual(cur.fetchone()[5], 12)

        db.clear()

    def test_get_move(self):
        # test add_move
        db.clear()
        db.init_db()
        self.assertEqual(db.getMove(), None)

        db.add_move(("1", "1", "1", "1", "1", 30))
        self.assertEqual(db.getMove()[5], 30)

        db.add_move(("1", "1", "2", "1", "1", 29))
        self.assertEqual(db.getMove()[5], 29)

        db.clear()
