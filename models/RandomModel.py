from . import BaseModel
import random

class RandomModel(BaseModel):
  def choose_move(self, _):
    return self._random_move()
