class GameEndChecker():
  def is_draw(self, board):
    return None not in board[0] + board[1] + board[2]

  def who_won(self,board):
    for squares in board.values():
      if self.squares_equal(squares[0], squares[1], squares[2]):
        return squares[0]
    
    for i in range(len(board[0])):
      if self.squares_equal(board[0][i], board[1][i], board[2][i]):
        return board[0][i]

    if self.squares_equal(board[0][0], board[1][1], board[2][2]):
      return board[0][0]

    if self.squares_equal(board[0][2], board[1][1], board[2][0]):
      return board[0][2]
    return None
  
  def squares_equal(self, one, two, three):
    return one and one == two == three