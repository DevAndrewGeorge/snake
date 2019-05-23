import numpy
from Position import Position

class GameOverException(BaseException):
  pass

class InvalidMovException(BaseException):
  pass

class Game:
  SNAKE = 1
  FOOD = -1
  CLEAR = 0
  WALL = 2

  HEAD = 0
  TAIL = -1

  LEFT = Position(-1, 0)
  RIGHT = Position(1,0)
  UP = Position(0, -1)
  DOWN = Position(0, 1)

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
    self.snake = (self._find_random(Game.CLEAR),)
    self._mark_snake( self.snake[Game.HEAD] )
    self.food = self._find_random(Game.CLEAR)
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
      return Game.WALL

    # collided with self
    elif self.board[x][y] == Game.SNAKE and new_head != self.snake[Game.TAIL]:
      return Game.SNAKE
   
    return Game.CLEAR

  def _note(self, start, direction, result):
    return {
      "start": start,
      "finish": self._state(),
      "direction": [direction.width(), direction.height()],
      "result": result
    }

  def _state(self):
    return {
      "width": self.width,
      "height": self.height,
      "state": self.board.flatten().tolist(),
      "snake": [[piece.width(), piece.height()] for piece in self.snake],
      "food": [self.food.width(), self.food.height()]
    }

  def move(self, direction):
    #
    result = Game.RESULT["nothing"]
    start_state = self._state()

    # noting potentially changing board positions
    new_head = self.snake[Game.HEAD] + direction
    old_tail = self.snake[Game.TAIL]

    # do nothing if impossible move performed
    if not self._validate_move(new_head):
      return Game.RESULT["nothing"]

    # checking if game has been lost
    if self._evaulate_move(new_head) is not Game.CLEAR:
      result = Game.RESULT["lose"]
  
    # check if food was eaten
    full = False
    if new_head == self.food:
      result = Game.RESULT["eat"]
      full = True
    elif result is not Game.RESULT["lose"]:
      result = Game.RESULT["move"]

    # updating snake
    self.snake = (new_head,) + (self.snake if full else self.snake[:Game.TAIL])

    # updating board
    if not full:
      self._mark_clear(old_tail)
  
    if self._evaulate_move(new_head) is not Game.WALL:
      self._mark_snake(new_head)

    # checking if game has been won
    if len(self.snake) == self.width * self.height and result is not Game.RESULT["lose"]:
      result = Game.RESULT["win"]
    
    # generating new food
    if full and result is not Game.RESULT["win"]:
      self.food = self._find_random(Game.CLEAR)
      self._mark_food(self.food)
    
    
    return self._note(start_state, direction, result)

  def print(self):
    text = ""
    for row in range(self.height):
      for col in range(self.width):
        mark = self.board[col][row]
        if mark == Game.SNAKE:
          text = text + "O"
        elif mark == Game.FOOD:
          text = text + "x"
        elif mark == Game.CLEAR:
          text = text + "."
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
    self._mark(position, Game.CLEAR)
  
  def _mark_food(self, position):
    self._mark(position, Game.FOOD)
  
  def _mark_snake(self, position):
    self._mark(position, Game.SNAKE)
