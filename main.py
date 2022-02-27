# Import file and libraries
import pygame
from pygame.locals import *
from constants import *
from char import *
from events import game_events
from func import *

# Initialize pygame
pygame.init()

# Set game window
pygame.display.set_caption("Pong game")
bg_color = Black


# Run the game loop
while True:
    # Fill background
    SCREEN.fill(bg_color)

    # Check for events
    game_events()

    # Move the player
    player.move()
    if player.is_key_up:
        player.player_change = 0

    # Move the bot
    bot.move(ball)

    # Move the ball
    ball.move(player, bot)

    # Draw objects
    player.draw(SCREEN)
    bot.draw(SCREEN)
    ball.draw(SCREEN)

    # Show score
    show_score(screen_width / 2, 50, SCREEN)

    # Check for win
    checkwin()

    # Update the screen
    pygame.display.update()
    pygame.display.flip()
    fps.tick(60)
