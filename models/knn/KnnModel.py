import os
import joblib
from sklearn.neighbors import KNeighborsClassifier
import numpy
import random
from .. import BaseModel

class KnnModel(BaseModel):
  def __init__(self):
    self.model = joblib.load("{}/knn.model".format(os.path.dirname(__file__)))

  def choose_move(self, game_state):
    choice = list(self.model.predict([game_state["state"]])[0])

    if self.validate_move(game_state, choice):
      for move in KnnModel.MOVES.values():
        if choice == move:
          return move
    else:
      return self._random_move()
