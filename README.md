# snake
Can a computer learn how to play the game Snake?

This is an ongoing project that utilizes various ML models to better a computer's ability to play the game of snake whose reward function seeks to maximize the percentage of board covered.

## setting up your environment
The following will setup an isolated python environment with all the necessary requirements to run this application.
```bash
virtualenv
source bin/activate
pip install -r requirements.txt
```

## snake.py
The best help you can get is to run `./snake.py --help`, but the following will get you off the ground if you just want to play around.
### play as a human
#### starting
```bash
./snake.py play
```

You will be presented with the following:
```
.....
.....
.X.H.
.....
.....

[WASD]: 
```

#### the board
Board symbols mean the following:
* H: the snake's head. Your inputs control where the head moves next.
* O: the snake's body. Do not crash the snake's head into a body piece or you will lose.
* T: the end of the snake.
* X: food you are trying to eat.
* .: empty space

Your objective is to navigate the snake's head onto the space containing food by continually moving into adjacent empty spaces. This process continues until you have either:
1. Filled the entire board with the snake (head + body + tail).
2. Inadvertently navigate the snake's head into its body.

#### inputs
Inputs are as follows:
* W: up
* S: down
* A: left
* D: right

In short, imagine your WASD keys mapping to your keyboard's arrow keys.

### simulate with a model
```bash 
./snake.py [-m MODEL] simulate NUM_GAMES
```

The following models are available:
* **user**: this allows you to play, but you can play `NUM_GAMES` sequentially. 
* **random**: each move is RNG. These games won't last long.
* **knn**: k-nearest neighbors, trained from 100,000 games played using the `random` model. This model is not particularly useful, as it is a classification model (as a opposed to a reinforcement model), but it serves as an example of how to implement a more invovled model.
