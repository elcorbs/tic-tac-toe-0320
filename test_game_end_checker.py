import unittest
from game_end_checker import GameEndChecker

class TestGameEndChecker(unittest.TestCase):
  def setUp(self):
    self.game_end_checker = GameEndChecker()

  def test_checker_recognises_draw(self):
    board = { 0: ['X', 'O', 'X'], 1: ['O', 'X', 'X'], 2: ['O', 'X', 'O'] }
    self.assertEqual(self.game_end_checker.is_draw(board), True)

  def test_checker_recognises_not_draw(self):
    board = { 0: ['X', 'O', 'X'], 1: [None, 'X', 'X'], 2: ['O', 'X', 'O'] }
    self.assertEqual(self.game_end_checker.is_draw(board), False)

  def test_if_player_X_won_first_row_state_is_won(self):
    board = { 0: ['X', 'X', 'X'], 1: ['O', 'O', None], 2: [None, None, None] }
    self.assertEqual(self.game_end_checker.who_won(board), 'X')

  def test_if_player_O_won_first_row_state_is_won(self):
    board = { 0: ['O', 'O', 'O'], 1: ['X', 'X', None], 2: [None, None, None] }
    self.assertEqual(self.game_end_checker.who_won(board), 'O')

  def test_if_player_X_won_second_row_state_is_won(self):
    board = { 0: ['O', 'O', None], 1: ['X', 'X', 'X'], 2: [None, None, None] }
    self.assertEqual(self.game_end_checker.who_won(board), 'X')

  def test_if_player_O_won_second_row_state_is_won(self):
    board = { 0: ['O', 'O', None], 1: ['O', 'O', 'O'], 2: [None, None, None] }
    self.assertEqual(self.game_end_checker.who_won(board), 'O')

  def test_if_player_X_won_third_row_state_is_won(self):
    board = { 0: ['O', 'O', None], 1: [None, None, None], 2: ['X', 'X', 'X'] }
    self.assertEqual(self.game_end_checker.who_won(board), 'X')
  
  def test_if_player_X_won_first_column_state_is_won(self):
    board = { 0: ['X', 'O', None], 1: ['X', None, None], 2: ['X', 'O', 'O'] }
    self.assertEqual(self.game_end_checker.who_won(board), 'X')

  def test_if_player_X_won_second_column_state_is_won(self):
    board = { 0: ['O', 'X', None], 1: ['O', 'X', None], 2: [None, 'X', 'O'] }
    self.assertEqual(self.game_end_checker.who_won(board), 'X')
  
  def test_if_player_X_won_third_column_state_is_won(self):
    board = { 0: ['O', None, 'X'], 1: ['O', None, 'X'], 2: [None, 'O', 'X'] }
    self.assertEqual(self.game_end_checker.who_won(board), 'X')

  def test_if_player_X_won_backward_diagonal_state_is_won(self):
    board = { 0: ['X', None, 'O'], 1: ['O', 'X', None], 2: [None, 'O', 'X'] }
    self.assertEqual(self.game_end_checker.who_won(board), 'X')

  def test_if_player_X_won_forward_diagonal_state_is_won(self):
    board = { 0: [None, 'O', 'X'], 1: ['O', 'X', None], 2: ['X', None, 'O'] }
    self.assertEqual(self.game_end_checker.who_won(board), 'X')