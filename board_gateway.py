import json
class BoardGateway ():
  file_path = './board.json'
  def get_board(self):
    with open(self.file_path, 'r') as file:
      board_data = file.read()

    return json.loads(board_data)

  def empty_board(self):
    empty_board = '{"0": [null, null, null], "1": [null, null, null], "2": [null, null, null]}'

    with open(self.file_path, 'w') as file:
      file.write(empty_board)
  
  def place_counter(self, player, x, y):
    with open(self.file_path, 'r') as file:
      board_data = json.loads(file.read())

    board_data[str(y-1)][x-1] = player

    with open(self.file_path, 'w') as file:
      file.write(json.dumps(board_data))
