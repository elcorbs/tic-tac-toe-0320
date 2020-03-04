class TicTacToe():
  def __init__(self, board_gateway):
    self.board_gateway = board_gateway

  def start_game(self):
    self.board_gateway.empty_board()
    return {'board': self.board_gateway.get_board(), 'state': 'new game'}

  def take_turn(self, x, y):
    self.board_gateway.place_counter(x, y)
    board = self.board_gateway.get_board()
    state = 'in play'    
    if self.is_draw(board):
      state = 'draw'
    if self.is_won(board):
      state = 'player ' + board[1][0] + ' won'

    return {'board': board, 'state': state}

  def is_draw(self, board):
    return None not in board[1] + board[2] + board[3]

  def is_won(self, board):
    first_row_won = board[1][0] and board[1][0] == board[1][1] == board[1][2]
    second_row_won = board[2][0] and board[2][0] == board[2][1] == board[2][2]
    return first_row_won or second_row_won

