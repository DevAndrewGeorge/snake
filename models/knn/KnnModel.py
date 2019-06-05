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
    choice = self.model.predict([game_state["state"]])[0]
    for move in KnnModel.MOVES.values():
      coordinates = move.coordinates()
      if coordinates[0] == choice[0] and coordinates[1] == choice[1]:
        return move
    return random.choice(
      list(KnnModel.MOVES.values())
    )
    raise BaseException("failed to make a choice")
