class Game(object):
    """ class representing the game of a dots and crosses """

    board = []

    def __init__(self):
        for field in range(9):
            self.board.append(' ')


    def check_if_given_field_correct(self, field):
        if field >= 0 and field <= 8:
            if self.board[field] == ' ':
                print("Your choice was saved.")
                return True
            else:
                print("This field is already occupied. Please choose another free value.")
                return False
        else:
            print("Bad number, use one with 0-8 to make movement.")
            return False


    def first_user_motion(self):
        field = int(input("Now first player play. Give one position using numbers 0-8:   "))
        if self.check_if_given_field_correct(field):
            self.board[field] = "O"
            return True
        else:
            return False

    def second_user_motion(self):
        field = int(input("Now second player play. Give one position using numbers 0-8:   "))
        if self.check_if_given_field_correct(field):
            self.board[field] = "X"
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

    def game(self):
        counter = 0
        print("Now we are starting the game!")
        self.print_board()
        first_player_play = True
        while counter <= 8:
            if first_player_play:
                if self.first_user_motion():
                    first_player_play = False
                    self.print_board()
                    counter += 1
            else:
                if self.second_user_motion():
                    first_player_play = True
                    self.print_board()
                    counter += 1



new_game = Game()
new_game.game()
