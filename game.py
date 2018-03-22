import math


class Game(object):
    """ class representing the game of a dots and crosses """

    board = []
    rows = [0, 0, 0]
    columns = [0, 0, 0]
    diagonals = [0, 0]
    winning_flag = 0

    def __init__(self):
        for field in range(9):
            self.board.append(' ')

    def winning_condition_increment(self, field, increment_value):
        self.rows[math.floor(field / 3)] += increment_value
        self.columns[field % 3] += increment_value
        if field in {0, 4, 8}:
            self.diagonals[0] += increment_value
        if field in {2, 4, 6}:
            self.diagonals[1] += increment_value

    def check_if_given_field_correct(self, field):
        if isinstance(field, int):
            if field != '' and 0 <= field <= 8:
                if self.board[field] == ' ':
                    print("Your choice was saved.")
                    return True
                else:
                    print("This field is already occupied. Please choose another free value.")
                    return False
            else:
                print("Bad number, use a number from range 0-8 to make a move. For reference:")
                Game.mock_board()
                return False
        else:
            print("Bad value, you have to use integer. Use a number from range 0-8 to make a move. For reference:")
            Game.mock_board()
            return False

    def first_user_move(self):
        field = input("First player's move. Choose a spot using numbers 0-8:   ")
        if self.check_if_given_field_correct(field):
            field = int(field)
            self.board[field] = "O"
            self.winning_condition_increment(field, -1)
            return True
        else:
            return False

    def second_user_move(self):
        field = input("Second player's move. Choose a spot using numbers 0-8:   ")
        if self.check_if_given_field_correct(field):
            field = int(field)
            self.board[field] = "X"
            self.winning_condition_increment(field, 1)
            return True
        else:
            return False

    def print_board(self):
        for field in range(9):
            if field%3 == 0:
                print("\n-----------")
            print(" %c " % self.board[field], end = '')
            if (field+1)%3 != 0:
                print("|", end = '')
        print("\n-----------")

    @staticmethod
    def mock_board():
        print("How to play:\n", "Choose where do you want to play your dot or cross,\n",
              "by typing a number corresponding to the field below")
        for field in range(9):
            if field%3 == 0:
                print("\n-----------")
            print(" " + str(field) + " ", end = '')
            if (field+1)%3 != 0:
                print("|", end = '')
        print("\n-----------")

    def winning_condition_check(self):
        if -3 in self.rows or -3 in self.columns or -3 in self.diagonals :
            print("Player one(O) won!")
            self.winning_flag = 1
            return False
        if 3 in self.rows or 3 in self.columns or 3 in self.diagonals:
            print("Player two(X) won!")
            self.winning_flag = 1
            return False
        return True

    def game(self):
        counter = 0
        Game.mock_board()
        print("New game started!")
        self.print_board()
        first_player_play = True
        while self.winning_condition_check() and counter != 9:
            if first_player_play:
                if self.first_user_move():
                    first_player_play = False
                    self.print_board()
                    counter += 1
            else:
                if self.second_user_move():
                    first_player_play = True
                    self.print_board()
                    counter += 1
        if not self.winning_flag:
            print("It's a draw!")
        print("Thanks for playing!")


new_game = Game()
new_game.game()
