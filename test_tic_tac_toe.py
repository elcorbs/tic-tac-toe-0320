import unittest
from unittest.mock import Mock
from tic_tac_toe import TicTacToe
from game_end_checker import GameEndChecker

class TestTicTactoe(unittest.TestCase):

  def setUp(self):
    self.board_gateway_mock = Mock()
    self.game_end_checker_mock = Mock()
    self.tic_tac_toe = TicTacToe(self.board_gateway_mock, self.game_end_checker_mock)

  def mock_return_empty_board(self):
    board = { 0: [None, None, None], 1: [None, None, None], 2: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = board
    return board

  def mock_game_end_checker_returns_in_play(self):
    self.game_end_checker_mock.is_draw.return_value = False
    self.game_end_checker_mock.who_won.return_value = None

  def mock_game_end_checker_returns_draw(self):
    self.game_end_checker_mock.is_draw.return_value = True
    self.game_end_checker_mock.who_won.return_value = None

  def mock_game_end_checker_who_won_to_return(self, player):
    self.game_end_checker_mock.is_draw.return_value = False
    self.game_end_checker_mock.who_won.return_value = player

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
    expected_board = { 0: [None, None, None], 1: [None, 'X', None], 2: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = expected_board
    self.mock_game_end_checker_returns_in_play()
    board = self.tic_tac_toe.take_turn(2, 2)
    self.assertEqual(board, {'board': expected_board, 'state': 'in play'})
  
  def test_when_another_turn_taken_updated_board_is_returned(self):
    expected_board = { 0: [None, 'O', None], 1: ['X', None, 'X'], 2: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = expected_board
    self.mock_game_end_checker_returns_in_play()
    board = self.tic_tac_toe.take_turn(2, 2)
    self.assertEqual(board, {'board': expected_board, 'state': 'in play'})

  def test_checks_if_there_is_a_draw(self):
    expected_board = { 0: ['X', 'O', 'X'], 1: ['O', 'X', 'X'], 2: ['O', 'X', 'O'] }
    self.board_gateway_mock.get_board.return_value = expected_board
    self.tic_tac_toe.take_turn(3, 3)
    self.game_end_checker_mock.is_draw.assert_called_with(expected_board)

  def test_a_draw_returns_draw_state(self):
    expected_board = self.mock_return_empty_board()
    self.mock_game_end_checker_returns_draw()
    board = self.tic_tac_toe.take_turn(3, 3)
    self.assertEqual(board, {'board': expected_board, 'state': 'draw'})

  def test_if_player_X_won_first_row_state_is_won(self):
    expected_board = { 0: ['X', 'X', 'X'], 1: ['O', 'O', None], 2: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = expected_board
    self.mock_game_end_checker_who_won_to_return('X')
    board = self.tic_tac_toe.take_turn(1, 3)
    self.assertEqual(board, {'board': expected_board, 'state': 'player X won'})

  def test_if_player_O_won_first_row_state_is_won(self):
    expected_board = { 0: ['O', 'O', 'O'], 1: ['X', 'X', None], 2: [None, None, None] }
    self.board_gateway_mock.get_board.return_value = expected_board
    self.mock_game_end_checker_who_won_to_return('O')
    board = self.tic_tac_toe.take_turn(1, 3)
    self.assertEqual(board, {'board': expected_board, 'state': 'player O won'})
