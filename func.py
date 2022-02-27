import pygame
from char import *
from constants import *


def write(content, x, y, size, color, screen):
    font = pygame.font.SysFont("Roboto-Medium.ttf", size)
    text = font.render(content, True, color)
    screen.blit(text, text.get_rect(center=(x, y)))


def show_score(x, y, screen):
    write(str(player.score) + " : " +
          str(bot.score), x, y, 100, White, screen)


def pause(fps):
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_SPACE:
                    loop = False
        pygame.display.update()
        fps.tick(60)


def reset():
    player.reset()
    bot.reset()


def checkwin():
    if (player.score == 10):
        SCREEN.fill(Black)
        write("Player wins!", screen_width / 2,
              screen_height / 2 - 100, 150, White, SCREEN)
        write("Press Space to play again", screen_width /
              2, screen_height / 2 + 40, 100, White, SCREEN)
        reset()
        pause(fps)
    elif (bot.score == 10):
        SCREEN.fill(Black)
        write("Bot wins!", screen_width / 2,
              screen_height / 2 - 100, 150, White, SCREEN)
        write("Press Space to play again", screen_width /
              2, screen_height / 2 + 40, 100, White, SCREEN)
        reset()
        pause(fps)
