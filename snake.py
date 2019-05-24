#!/usr/bin/env python3
"""Snake

Usage:
  snake --help
  snake [-w WIDTH] [-h HEIGHT] [-s [-o DATA_DIR]] play
  snake [-w WIDTH] [-h HEIGHT] [-s [-o DATA_DIR]] [-m MODEL] simulate NUM_GAMES

Arguments:
  NUM_GAMES  The number of games to be simulated.
  DATA_DIR   The directory where game states will be saved.
  MODEL      The decision-making model to use. Current values: random, user.

Options:
  -w WIDTH, --width WIDTH     [default: 5]
  -h HEIGHT, --height HEIGHT  [default: 5]
  -s --save  Save gameplay data
  -o DATA_DIR, --output DATA_DIR  [default: ./data]
  -m MODEL, --model MODEL [default: rand]
"""
import sys
import os
import json
import pprint
from docopt import docopt
import Game
from Game import Game as Snake
import models


def create_log_file(data_dir):
  try:
    last_game = sorted(os.listdir(data_dir))[-1]
    game_number = int(last_game.replace("game_", "").replace(".txt", "")) + 1
    file_name = "game_{}.txt".format( str(game_number).zfill(7) )
    return open("{}/{}".format(data_dir, file_name), "w")
  except IndexError:
    return open("{}/game_0000000.txt".format(data_dir), "w")


def simulate(board_width, board_height, model, log=False, display=False):
  snake = Snake(board_width, board_height)
  while True:
    if display:
      print(snake.print())
    
    state = move = model.choose_move(snake.state())

    if log:
      log.write(json.dumps(state))


    result = state["result"]
    if result is Snake.RESULT["lose"]:
      print("You lose.")
      break
    elif result is Snake.RESULT["win"]:
      print("You win!")
      break
  
  if log:
    close(log)




def main():
  args = docopt(__doc__, options_first=True)
  print(args)

  available_models = {
    "user": models.UserWasdModel,
    "random": models.RandomModel
  }

  width = int(args["--width"])
  height = int(args["--height"])
  log = create_log_file() if args["--save"] else None
  if args["play"]:
    simulate(
      width,
      height,
      models.UserWasdModel(),
      log,
      display=True
    )
  elif args["simulate"]:
    for _ in range(int(args["NUM_GAMES"])):
      simulate(
        width,
        height,
        available_models[args["MODEL"]],
        log,
        display=False
      )

if __name__ == "__main__":
  main()
