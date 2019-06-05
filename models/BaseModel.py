import random
from Game import Game as Snake

class BaseModel:
  MOVES = {
    "W": Snake.MOVES["up"],
    "A": Snake.MOVES["left"],
    "S": Snake.MOVES["down"],
    "D": Snake.MOVES["right"]
  }
  
  def __init__(self):
    pass

  def choose_move(self, state):
    """ Returns a Game.MOVE """
    return None

  def validate_move(self, state, move):
    if move == Snake.MOVES["none"]:
      return False
    elif move == state["move"]:
      return False

  def _random_move(self):
    return random.choice(
      list(BaseModel.MOVES.values())
    )
