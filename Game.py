import numpy
from Position import Position

class GameOverException(BaseException):
  pass

class InvalidMovException(BaseException):
  pass

class Game:
  PIECES = {
    "food": -1,
    "clear": 0,
    "wall": 1,
    "snake": 10,
    "head": 11,
    "tail": 12
  }

  SNAKE = {
    "head": 0,
    "tail": -1
  }

  MOVES = {
    "left": Position(-1, 0),
    "right": Position(1,0),
    "up": Position(0, -1),
    "down": Position(0, 1)
  }
  

  RESULT = {
    "lose": -1,
    "nothing": 0,
    "move": 1,
    "eat": 10,
    "win": 20
  }


  def __init__(self, width, height):
    # 
    self.width = width
    self.height = height

    # configuring board
    self.board = numpy.zeros(shape=(self.width, self.height), dtype=int)
    self.snake = (self._find_random(Game.PIECES["clear"]),)
    self._mark_head( self.snake[Game.SNAKE["head"]] )
    self.food = self._find_random(Game.PIECES["clear"])
    self._mark_food( self.food )
  
  def _validate_move(self, new_head):
    # You are disllowed form reversing direction
    try:
      if new_head == self.snake[1]:
        return False
    except IndexError:
      pass
    return True

  def _evaulate_move(self, new_head):
    x = new_head.width()
    y = new_head.height()

    # out of bounds
    if x < 0 or x >= self.width or y < 0 or y >= self.height:
      return Game.PIECES["wall"]

    # collided with self
    elif self.board[x][y] == Game.PIECES["snake"]:
      return Game.PIECES["snake"]
   
    return Game.PIECES["clear"]

  def _note(self, start, direction, result):
    return {
      "start": start,
      "finish": self.state(),
      "direction": [direction.width(), direction.height()],
      "result": result
    }

  def state(self):
    head = self.snake[Game.SNAKE["head"]]
    tail = self.snake[Game.SNAKE["tail"]]
    return {
      "width": self.width,
      "height": self.height,
      "state": self.board.flatten().tolist(),
      "snake": [[piece.width(), piece.height()] for piece in self.snake],
      "head": [head.width(), head.height()],
      "tail": [tail.width(), tail.height()],
      "food": [self.food.width(), self.food.height()]
    }

  def move(self, direction):
    #
    result = Game.RESULT["nothing"]
    start_state = self.state()

    # noting potentially changing board positions
    old_head = self.snake[Game.SNAKE["head"]]
    old_tail = self.snake[Game.SNAKE["tail"]]
    new_head = self.snake[Game.SNAKE["head"]] + direction
    
    # do nothing if impossible move performed
    if not self._validate_move(new_head):
      return Game.RESULT["nothing"]

    # checking if game has been lost
    if self._evaulate_move(new_head) is not Game.PIECES["clear"]:
      result = Game.RESULT["lose"]
  
    # check if food was eaten
    full = False
    if new_head == self.food:
      result = Game.RESULT["eat"]
      full = True
    elif result is not Game.RESULT["lose"]:
      result = Game.RESULT["move"]

    # updating snake
    self.snake = (new_head,) + (self.snake if full else self.snake[:Game.SNAKE["tail"]])

    # updating board
    self._mark_clear(old_head)
    self._mark_clear(old_tail)
    if len(self.snake) > 1:
      self._mark_snake(old_head)
      self._mark_tail(self.snake[Game.SNAKE["tail"]])
    if self._evaulate_move(new_head) is not Game.PIECES["wall"]:
      self._mark_head(new_head)

    # checking if game has been won
    if len(self.snake) == self.width * self.height and result is not Game.RESULT["lose"]:
      result = Game.RESULT["win"]
    
    # generating new food
    if full and result is not Game.RESULT["win"]:
      self.food = self._find_random(Game.PIECES["clear"])
      self._mark_food(self.food)
    
    
    return self._note(start_state, direction, result)

  def print(self):
    text = ""
    for row in range(self.height):
      for col in range(self.width):
        mark = self.board[col][row]
        c = None
        if mark == Game.PIECES["snake"]:
          c = "O"
        elif mark == Game.PIECES["food"]:
          c = "X"
        elif mark == Game.PIECES["clear"]:
          c = "."
        elif mark == Game.PIECES["head"]:
          c = "H"
        elif mark == Game.PIECES["tail"]:
          c = "T"
        text = text + c
      text = text + "\n"
    return text

  def _find_random(self, marking):
    while True:
      x = numpy.random.randint(0, self.width)
      y = numpy.random.randint(0, self.height)

      if marking is None or self.board[x][y] == marking:
        return Position(x, y)

  def _mark(self, position, marking):
    self.board[position.width()][position.height()] = marking
  
  def _mark_clear(self, position):
    self._mark(position, Game.PIECES["clear"])
  
  def _mark_food(self, position):
    self._mark(position, Game.PIECES["food"])
  
  def _mark_snake(self, position):
    self._mark(position, Game.PIECES["snake"])

  def _mark_head(self, position):
    self._mark(position, Game.PIECES["head"])

  def _mark_tail(self, position):
    self._mark(position, Game.PIECES["tail"])
