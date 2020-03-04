import unittest
from unittest.mock import Mock
from tic_tac_toe import TicTacToe

class TestTicTactoe(unittest.TestCase):

  def setUp(self):
    self.board_gateway_mock = Mock()
    self.tic_tac_toe = TicTacToe(self.board_gateway_mock)

  def mock_return_empty_board(self):
    board = { 1: [None, None, None], 2: [None, None, None], 3: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = board
    return board

  def test_start_game_empties_the_board(self):
    self.tic_tac_toe.start_game()
    self.board_gateway_mock.empty_board.assert_called()

  def test_start_game_returns_the_board_retrieved_from_gateway(self):
    expected_board = self.mock_return_empty_board()
    board = self.tic_tac_toe.start_game()
    self.assertEqual(board, {'board': expected_board, 'state': 'new game'})

  def test_when_turn_taken_a_counter_is_placed(self):
    self.mock_return_empty_board()
    self.tic_tac_toe.take_turn(2, 2)
    self.board_gateway_mock.place_counter.assert_called_with(2, 2)
  
  def test_when_turn_taken_a_different_counter_is_placed(self):
    self.mock_return_empty_board()
    self.tic_tac_toe.take_turn(1, 3)
    self.board_gateway_mock.place_counter.assert_called_with(1, 3)

  def test_when_turn_taken_updated_board_is_returned(self):
    expected_board = { 1: [None, None, None], 2: [None, 'X', None], 3: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = expected_board
    board = self.tic_tac_toe.take_turn(2, 2)
    self.assertEqual(board, {'board': expected_board, 'state': 'in play'})
  
  def test_when_another_turn_taken_updated_board_is_returned(self):
    expected_board = { 1: [None, 'O', None], 2: ['X', None, 'X'], 3: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = expected_board
    board = self.tic_tac_toe.take_turn(2, 2)
    self.assertEqual(board, {'board': expected_board, 'state': 'in play'})

  def test_if_board_full_no_winner_state_is_draw(self):
    expected_board = { 1: ['X', 'O', 'X'], 2: ['O', 'X', 'X'], 3: ['O', 'X', 'O'] }
    self.board_gateway_mock.get_board.return_value = expected_board
    board = self.tic_tac_toe.take_turn(3, 3)
    self.assertEqual(board, {'board': expected_board, 'state': 'draw'})

  def test_if_player_X_won_first_row_state_is_won(self):
    expected_board = { 1: ['X', 'X', 'X'], 2: ['O', 'O', None], 3: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = expected_board
    board = self.tic_tac_toe.take_turn(1, 3)
    self.assertEqual(board, {'board': expected_board, 'state': 'player X won'})

  def test_if_player_O_won_first_row_state_is_won(self):
    expected_board = { 1: ['O', 'O', 'O'], 2: ['X', 'X', None], 3: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = expected_board
    board = self.tic_tac_toe.take_turn(1, 3)
    self.assertEqual(board, {'board': expected_board, 'state': 'player O won'})

  def test_if_player_X_won_second_row_state_is_won(self):
    expected_board = { 1: ['O', 'O', None], 2: ['X', 'X', 'X'], 3: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = expected_board
    board = self.tic_tac_toe.take_turn(2, 3)
    self.assertEqual(board, {'board': expected_board, 'state': 'player X won'})
