from . import BaseModel
import random

class RandomModel(BaseModel):
  def choose_move(self, _):
    return random.choice(
      list(RandomModel.MOVES.values())
    )
