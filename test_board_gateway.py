import unittest
from board_gateway import BoardGateway

class TestBoardGateway(unittest.TestCase):
  file_path = './board.json'
  initial_board_data = '{"1": [null, null, null], "2": [null, null, null], "3": [null, null, null]}'
  
  def save_string_to_file(self,board_data):
    with open(self.file_path, 'w') as file:
      file.write(board_data)
  
  def get_file_contents(self):
     with open(self.file_path, 'r') as file:
      return file.read()

  def test_get_board_returns_empty_board(self):
    self.save_string_to_file(self.initial_board_data)

    board = BoardGateway().get_board()
    self.assertEqual(board,{'1': [None, None, None], '2': [None, None, None], '3': [None, None, None]})

  def test_get_board_returns_populated_board(self):
    board_data = '{ "1": ["X", null, null], "2":[null, null, null], "3": [null, null, null] }'
    self.save_string_to_file(board_data)

    board = BoardGateway().get_board()
    self.assertEqual(board,{'1': ['X', None, None], '2': [None, None, None], '3': [None, None, None]})

  def test_place_X_in_position_1_1(self):
    expected_board_data = '{"1": ["X", null, null], "2": [null, null, null], "3": [null, null, null]}'
    self.save_string_to_file(self.initial_board_data)
    
    BoardGateway().place_counter('X',1,1)

    board_data = self.get_file_contents()

    self.assertEqual(expected_board_data,board_data)

  def test_place_X_in_position_2_1(self):
    expected_board_data = '{"1": [null, "X", null], "2": [null, null, null], "3": [null, null, null]}'
    self.save_string_to_file(self.initial_board_data)
    
    BoardGateway().place_counter('X',2,1)

    board_data = self.get_file_contents()

    self.assertEqual(expected_board_data,board_data)

  def test_place_X_in_position_1_2(self):
    expected_board_data = '{"1": [null, null, null], "2": ["X", null, null], "3": [null, null, null]}'
    self.save_string_to_file(self.initial_board_data)
    
    BoardGateway().place_counter('X',1,2)

    board_data = self.get_file_contents()

    self.assertEqual(expected_board_data,board_data)
  
  def test_place_O_in_position_2_2(self):
    expected_board_data = '{"1": [null, null, null], "2": [null, "O", null], "3": [null, null, null]}'
    self.save_string_to_file(self.initial_board_data)
    
    BoardGateway().place_counter('O',2,2)

    board_data = self.get_file_contents()

    self.assertEqual(expected_board_data,board_data)

  def test_empty_board_saves_a_blank_board(self):
    self.save_string_to_file('{"1": [null, null, null], "2": [null, "O", null], "3": [null, null, null]}')
    
    BoardGateway().empty_board()

    board_data = self.get_file_contents()
    self.assertEqual(board_data, self.initial_board_data)
