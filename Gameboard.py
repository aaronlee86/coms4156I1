import db

class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42

    def makemove(self, col, player):
        if player != self.current_turn:
            return False, "It's not your turn"

        row = 5
        while self.board[row][col] != 0 and row >= 0:
            row -= 1

        if row == -1:
            return False, "This column is filled"

        if self.current_turn == 'p1':
            self.board[row][col] = self.player1
        else:
            self.board[row][col] = self.player2

        if player == 'p1':
            self.current_turn = 'p2'
        else: self.current_turn = 'p1'

        result = self.checkWinning(row, col)
        if len(result):
            if self.player1 == result:
                self.game_result = 'player1'
            else:
                self.game_result = 'player2'

        self.remaining_moves -= 1
        if self.remaining_moves == 0:
            self.game_result = 'draw'

        return True, ""

    def checkWinning(self, r, c):
        if r+3 < len(self.board):
            # check vertical
            if self.board[r][c] == self.board[r+1][c] == self.board[r+2][c] == self.board[r+3][c]:
                return self.board[r][c]

            # check 45
            if c+3 < len(self.board[0]):
                if self.board[r][c] == self.board[r+1][c+1] == self.board[r+2][c+2] == self.board[r+3][c+3]:
                    return self.board[r][c]

            # check 135
            if c-3 >=0:
                if self.board[r][c] == self.board[r+1][c-1] == self.board[r+2][c-2] == self.board[r+3][c-3]:
                    return self.board[r][c]

        if c+3 < len(self.board[0]):
            # check 0
            if self.board[r][c] == self.board[r][c+1] == self.board[r][c+2] == self.board[r][c+3]:
                return self.board[r][c]

        # check 180
        elif c-3 >=0:
            if self.board[r][c] == self.board[r][c-1] == self.board[r][c-2] == self.board[r][c-3]:
                return self.board[r][c]

        return ""
'''
Add Helper functions as needed to handle moves and update board and turns
'''



