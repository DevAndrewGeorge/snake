class Position:
  def __init__(self, x, y):
    self._x = x
    self._y = y

  def width(self):
    return self._x

  def height(self):
    return self._y

  def coordinates(self):
    return (self.width(), self.height())
  
  def __eq__(self, other):
    return self._x == other._x and self._y == other._y

  def __add__(self, other):
    x = self._x + other._x
    y = self._y + other._y
    return Position(x, y)
