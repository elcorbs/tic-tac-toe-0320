class GameEndChecker():
  def is_draw(self, board):
    return None not in board[0] + board[1] + board[2]
    
  def who_won(self,board):
    first_row_won = board[0][0] and board[0][0] == board[0][1] == board[0][2]
    second_row_won = board[1][0] and board[1][0] == board[1][1] == board[1][2]

    if first_row_won:
      return board[0][0]
    if second_row_won:
      return board[1][0]
    return None