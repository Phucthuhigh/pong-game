import pygame
from pygame.locals import *
from char import *
from func import pause
from constants import *


def game_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if (event.key == K_s) or (event.key == K_DOWN):
                player.player_change += player.speed
                player.is_key_up = False
            elif (event.key == K_w) or (event.key == K_UP):
                player.player_change -= player.speed
                player.is_key_up = False
            elif event.key == K_SPACE:
                pause(fps)
        if event.type == KEYUP:
            if (event.key == K_s) or (event.key == K_DOWN) or (event.key == K_w) or (event.key == K_UP):
                player.is_key_up = True
