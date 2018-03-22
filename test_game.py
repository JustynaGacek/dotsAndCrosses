from unittest import TestCase
from game import Game


class TestGame(TestCase):
    def test_winning_condition_increment(self):
        self.fail()

    def test_check_if_given_field_correct(self):
        game = Game.Game()
        self.assertEqual(game.check_if_given_field_correct(4), True)
        self.assertEqual(game.check_if_given_field_correct(9), False)
        self.assertEqual(game.check_if_given_field_correct(-1), False)
        self.assertRaises(ValueError, game.check_if_given_field_correct, self, 3.33)
        self.assertRaises(ValueError, game.check_if_given_field_correct, self, "aaa")


    def test_first_user_move(self):
        self.fail()

    def test_second_user_move(self):
        self.fail()

    def test_winning_condition_check(self):
        self.fail()

    def test_game(self):
        self.fail()
