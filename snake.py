#!/usr/bin/env python3
import sys
import Game
from Game import Game as Snake

def main():
  width = int(sys.argv[1])
  height = int(sys.argv[2])
  snake = Snake(width, height)

  while True:
    try:
      print(snake.print())
      move = input()
      direction = None
      if move == "u":
        direction = Snake.UP
      elif move == "d":
        direction = Snake.DOWN
      elif move == "l":
        direction = Snake.LEFT
      elif move == "r":
        direction = Snake.RIGHT
      snake.move(direction)
    except Game.InvalidMovException:
      print("Invalid move.")
    except Game.GameOverException:
      print("Game over!")
      return
  pass

if __name__ == "__main__":
  main()
