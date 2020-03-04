import unittest
from game_end_checker import GameEndChecker

class TestGameEndChecker(unittest.TestCase):  
  def test_checker_recognises_draw(self):
    board = { 0: ['X', 'O', 'X'], 1: ['O', 'X', 'X'], 2: ['O', 'X', 'O'] }
    game_end_checker = GameEndChecker()
    self.assertEqual(game_end_checker.is_draw(board), True)

  def test_checker_recognises_not_draw(self):
    board = { 0: ['X', 'O', 'X'], 1: [None, 'X', 'X'], 2: ['O', 'X', 'O'] }
    game_end_checker = GameEndChecker()
    self.assertEqual(game_end_checker.is_draw(board), False)

  def test_if_player_X_won_first_row_state_is_won(self):
    board = { 0: ['X', 'X', 'X'], 1: ['O', 'O', None], 2: [None, None, None] }
    game_end_checker = GameEndChecker()
    self.assertEqual(game_end_checker.who_won(board), 'X')

  def test_if_player_O_won_first_row_state_is_won(self):
    board = { 0: ['O', 'O', 'O'], 1: ['X', 'X', None], 2: [None, None, None] }
    game_end_checker = GameEndChecker()
    self.assertEqual(game_end_checker.who_won(board), 'O')

  def test_if_player_X_won_second_row_state_is_won(self):
    board = { 0: ['O', 'O', None], 1: ['X', 'X', 'X'], 2: [None, None, None] }
    game_end_checker = GameEndChecker()
    self.assertEqual(game_end_checker.who_won(board), 'X')