from . import BaseModel

class UserWasdModel(BaseModel):
  def choose_move(self, _):
    move = ""
    while move not in UserWasdModel.MOVES:
      move = input("[WASD]: ").upper()
    return UserWasdModel.MOVES[move]
