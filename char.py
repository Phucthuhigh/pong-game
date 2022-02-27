# Import file and libraries
from player import Player
from ai import AI
from ball import Ball
from constants import *

# Setup the player
player = Player(0, screen_height / 2 - 100, 10, 200, White, 16)
bot = AI(screen_width - 10, screen_height / 2 - 100, 10, 200, White, 10)

# Setup the ball
ball = Ball(screen_width / 2 - 5, screen_height / 2 - 5, 30, White, 12)
