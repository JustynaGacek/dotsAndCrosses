from unittest import TestCase
from game import Game


class TestGame(TestCase):

    def test_winning_condition_increment(self):
        test_game = Game()
        test_game.winning_condition_increment(0, 1)
        test_rows = [1, 0, 0]
        test_columns = [1, 0, 0]
        test_diagonals = [1, 0]
        self.assertEqual(test_rows, test_game.rows, "Rows condition is wrong")
        self.assertEqual(test_columns, test_game.columns, "Column condition is wrong")
        self.assertEqual(test_diagonals, test_game.diagonals, "Diagonal conditions are wrong")
        test_game.winning_condition_increment(6, 1)
        test_rows = [1, 0, 1]
        test_columns = [2, 0, 0]
        test_diagonals = [1, 1]
        self.assertEqual(test_rows, test_game.rows, "Rows condition is wrong")
        self.assertEqual(test_columns, test_game.columns, "Column condition is wrong")
        self.assertEqual(test_diagonals, test_game.diagonals, "Diagonal conditions are wrong")
        test_game.winning_condition_increment(5, -1)
        test_rows = [1, -1, 1]
        test_columns = [2, 0, -1]
        test_diagonals = [1, 1]
        self.assertEqual(test_rows, test_game.rows, "Rows condition is wrong")
        self.assertEqual(test_columns, test_game.columns, "Column condition is wrong")
        self.assertEqual(test_diagonals, test_game.diagonals, "Diagonal conditions are wrong")

    def test_check_if_given_field_correct(self):
        game = Game()
        self.assertEqual(game.check_if_given_field_correct(4), True)
        self.assertEqual(game.check_if_given_field_correct(9), False)
        self.assertEqual(game.check_if_given_field_correct(-1), False)

    def test_winning_condition_check(self):
        test_game = Game()
        self.assertTrue(test_game.winning_condition_check())
        test_game.rows = [0, 3, 0]
        self.assertFalse(test_game.winning_condition_check())
        test_game.rows = [0, 0, 0]
        test_game.columns = [-3, 0, 0]
        self.assertFalse(test_game.winning_condition_check())
        test_game.columns = [-4, 1, 2]
        self.assertTrue(test_game.winning_condition_check())
        test_game.diagonals = [-3, -50]
        self.assertFalse(test_game.winning_condition_check())