import unittest
from Gameboard import Gameboard


class Test_TestGameboard(unittest.TestCase):
    def setUp(self):
        self.board = Gameboard()

    def tearDown(self):
        self.board = None

    def test_correct_color(self):
        # checks the color is correct for both sides
        self.assertEqual(self.board.setPlayer1(""), False)
        self.assertEqual(self.board.setPlayer1("blue"), False)
        self.assertEqual(self.board.setPlayer1(None), False)
        self.assertEqual(self.board.setPlayer2(), False)

        self.assertEqual(self.board.setPlayer1("yellow"), True)
        self.assertEqual(self.board.player1, "yellow")
        self.assertEqual(self.board.setPlayer2(), True)
        self.assertEqual(self.board.player2, "red")

        self.assertEqual(self.board.setPlayer1("red"), True)
        self.assertEqual(self.board.player1, "red")
        self.assertEqual(self.board.setPlayer2(), True)
        self.assertEqual(self.board.player2, "yellow")

    def test_correct_move(self):
        # Checks if there is a winning move in horizontal direction
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.assertEqual(self.board.makemove(0, 'p1'), (True, ""))
        self.assertEqual(self.board.board[5][0], 'red')

        self.assertEqual(self.board.makemove(1, 'p2'), (True, ""))
        self.assertEqual(self.board.board[5][1], 'yellow')

        self.assertEqual(self.board.makemove(2, 'p1'), (True, ""))
        self.assertEqual(self.board.board[5][2], 'red')

        self.assertEqual(self.board.makemove(3, 'p2'), (True, ""))
        self.assertEqual(self.board.board[5][3], 'yellow')

        self.assertEqual(self.board.makemove(4, 'p1'), (True, ""))
        self.assertEqual(self.board.board[5][4], 'red')

        self.assertEqual(self.board.makemove(5, 'p2'), (True, ""))
        self.assertEqual(self.board.board[5][5], 'yellow')

    def test_invalid_move_not_turn(self):
        # Invalid move - not current player's turn
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.assertEqual(self.board.makemove(0, 'p2'),
                         (False, "It's not your turn"))

        self.assertEqual(self.board.makemove(0, 'p1'), (True, ""))
        self.assertEqual(self.board.makemove(0, 'p1'),
                         (False, "It's not your turn"))

        self.assertEqual(self.board.makemove(0, 'p2'), (True, ""))
        self.assertEqual(self.board.makemove(0, 'p2'),
                         (False, "It's not your turn"))

    def test_invalid_move_winner_already(self):
        # Invalid move - winner already declared
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.board.makemove(0, 'p1')
        self.board.makemove(0, 'p2')
        self.board.makemove(1, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(2, 'p2')

        self.assertEqual(self.board.makemove(3, 'p1'), (True, ""))

        self.assertEqual(self.board.makemove(3, 'p2'),
                         (False, "The game was over"))
        self.assertEqual(self.board.makemove(3, 'p1'),
                         (False, "The game was over"))

    def test_invalid_move_draw(self):
        # Invalid move - draw (tie)
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        # row 5
        self.board.makemove(0, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(4, 'p1')
        self.board.makemove(5, 'p2')
        self.board.makemove(6, 'p1')

        # row 4
        self.board.makemove(0, 'p2')
        self.board.makemove(1, 'p1')
        self.board.makemove(2, 'p2')
        self.board.makemove(3, 'p1')
        self.board.makemove(4, 'p2')
        self.board.makemove(5, 'p1')
        self.board.makemove(6, 'p2')

        # row 3
        self.board.makemove(1, 'p1')
        self.board.makemove(0, 'p2')
        self.board.makemove(3, 'p1')
        self.board.makemove(4, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(5, 'p2')
        self.board.makemove(6, 'p1')

        # row 2
        self.board.makemove(1, 'p2')
        self.board.makemove(0, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(4, 'p1')
        self.board.makemove(5, 'p2')
        self.board.makemove(6, 'p1')
        self.board.makemove(2, 'p2')

        # row 1
        self.board.makemove(0, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(4, 'p1')
        self.board.makemove(6, 'p2')
        self.board.makemove(5, 'p1')

        # row 0
        self.board.makemove(1, 'p2')
        self.board.makemove(0, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(5, 'p2')
        self.board.makemove(4, 'p1')
        self.board.makemove(6, 'p2')

        self.assertEqual(self.board.game_result, "draw")
        self.assertEqual(self.board.makemove(6, 'p2'),
                         (False, "The game was over"))
        self.assertEqual(self.board.makemove(6, 'p2'),
                         (False, "The game was over"))

    def test_invalid_move_column_filled(self):
        # Invalid move - current column is filled
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.board.makemove(0, 'p1')
        self.board.makemove(0, 'p2')
        self.board.makemove(0, 'p1')
        self.board.makemove(0, 'p2')
        self.board.makemove(0, 'p1')
        self.board.makemove(0, 'p2')
        self.assertEqual(self.board.makemove(0, 'p1'),
                         (False, "This column is filled"))

    def test_win_horizontal_0(self):
        # Happy path for winning move in horizontal from left to right
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.board.makemove(0, 'p1')
        self.board.makemove(0, 'p2')
        self.board.makemove(1, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(2, 'p2')

        self.assertEqual(self.board.makemove(3, 'p1'), (True, ""))
        self.assertEqual(self.board.game_result, "player1")

    def test_win_horizontal_180(self):
        # Happy path for winning move in horizontal from right to left
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.board.makemove(6, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(3, 'p1')
        self.board.makemove(2, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(1, 'p1')
        self.board.makemove(0, 'p2')

        self.assertEqual(self.board.game_result, "player2")

    def test_win_vertical(self):
        # Happy path for winning move in vertical
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.board.makemove(0, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(0, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(0, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(0, 'p1')

        self.assertEqual(self.board.game_result, "player1")

    def test_win_diagonal_225(self):
        # Happy path for winning move in diagonal 225 degrees
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.board.makemove(0, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(3, 'p1')
        self.board.makemove(2, 'p2')
        self.board.makemove(1, 'p1')
        self.board.makemove(0, 'p2')
        self.board.makemove(0, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(3, 'p1')

        self.assertEqual(self.board.game_result, "player1")

    def test_win_diagonal_315(self):
        # Happy path for winning move in diagonal 315 degrees
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.board.makemove(0, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(3, 'p1')
        self.board.makemove(2, 'p2')
        self.board.makemove(1, 'p1')
        self.board.makemove(0, 'p2')
        self.board.makemove(0, 'p1')
        self.board.makemove(1, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(1, 'p1')
        self.board.makemove(0, 'p2')

        self.assertEqual(self.board.game_result, "player2")

    def test_win_diagonal_45(self):
        # Happy path for winning move in diagonal 45 degrees
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(4, 'p1')
        self.board.makemove(2, 'p2')
        self.board.makemove(3, 'p1')
        self.board.makemove(4, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(4, 'p1')
        self.board.makemove(2, 'p2')
        self.board.makemove(3, 'p1')
        self.board.makemove(4, 'p2')
        self.board.makemove(0, 'p1')
        self.board.makemove(1, 'p2')

        self.assertEqual(self.board.game_result, "player2")

    def test_win_diagonal_135(self):
        # Happy path for winning move in diagonal 45 degrees
        self.board.setPlayer1("red")
        self.board.setPlayer2()

        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(4, 'p1')
        self.board.makemove(2, 'p2')
        self.board.makemove(3, 'p1')
        self.board.makemove(4, 'p2')
        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')
        self.board.makemove(4, 'p1')
        self.board.makemove(2, 'p2')
        self.board.makemove(3, 'p1')
        self.board.makemove(4, 'p2')
        self.board.makemove(3, 'p1')
        self.board.makemove(5, 'p2')

        self.assertEqual(self.board.game_result, "player2")

    def test_get_status(self):
        # test getStatus method
        self.board.setPlayer1("yellow")
        self.board.setPlayer2()
        self.board.makemove(2, 'p1')
        self.board.makemove(3, 'p2')

        status = self.board.getStatus()
        self.assertEqual(status[0], "p1")
        self.assertEqual(status[1], "0,0,0,0,0,0,0;"
                                    "0,0,0,0,0,0,0;"
                                    "0,0,0,0,0,0,0;"
                                    "0,0,0,0,0,0,0;"
                                    "0,0,0,0,0,0,0;"
                                    "0,0,yellow,red,0,0,0")
        self.assertEqual(status[2], "")
        self.assertEqual(status[3], "yellow")
        self.assertEqual(status[4], "red")
        self.assertEqual(status[5], 40)

    def test_set_status(self):
        # test setStatus method
        self.board.setStatus(("p1", "0,0,0,0,0,0,0;"
                                    "0,0,0,0,0,0,0;"
                                    "0,0,0,0,0,0,0;"
                                    "0,0,0,0,0,0,0;"
                                    "0,0,0,0,0,0,0;"
                                    "0,0,yellow,red,0,0,0",
                                    "", "yellow", "red", 40))

        self.assertEqual(self.board.current_turn, "p1")
        self.assertEqual(self.board.game_result, "")
        self.assertEqual(self.board.player1, "yellow")
        self.assertEqual(self.board.player2, "red")
        self.assertEqual(self.board.remaining_moves, 40)
