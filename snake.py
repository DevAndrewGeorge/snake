#!/usr/bin/env python3
"""
"""
import sys
import os
import json
import pprint
import Game
from Game import Game as Snake

def create_log_file():
  try:
    last_game = sorted(os.listdir("./data"))[-1]
    game_number = int(last_game.replace("game_", "").replace(".txt", "")) + 1
    file_name = "game_{}.txt".format( str(game_number).zfill(7) )
    return open("{}/{}".format("data", file_name), "w")
  except IndexError:
    return open("data/game_0000000.txt", "w")
  
def main():
  width = int(sys.argv[1])
  height = int(sys.argv[2])

  snake = Snake(width, height)
  log_file = create_log_file()

  direction = None
  while True:
    print(snake.print())
    move = input()
    if move == "u":
      direction = Snake.UP
    elif move == "d":
      direction = Snake.DOWN
    elif move == "l":
      direction = Snake.LEFT
    elif move == "r":
      direction = Snake.RIGHT

    state = snake.move(direction)

    if state is Snake.RESULT["nothing"]:
      continue

    log_file.write(json.dumps(state))
    result = state["result"]

    if result is Snake.RESULT["lose"]:
      print("You lose.")
      break
    elif result is Snake.RESULT["win"]:
      print("You win!")
      break

  log_file.close()

if __name__ == "__main__":
  main()
