class TicTacToe():
  def __init__(self, board_gateway, game_checker):
    self.board_gateway = board_gateway
    self.game_checker = game_checker

  def start_game(self):
    self.board_gateway.empty_board()
    return {'board': self.board_gateway.get_board(), 'state': 'new game'}

  def take_turn(self, x, y):
    self.board_gateway.place_counter(x, y)
    board = self.board_gateway.get_board()
    state = self.get_state(board)

    return {'board': board, 'state': state}

  def get_state(self, board):
    if self.game_checker.is_draw(board):
      return 'draw'
    winner = self.game_checker.who_won(board)
    if winner:
      return f'player {winner} won'

    return 'in play'
