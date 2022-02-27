import pygame
from constants import *
import random


class Ball:
    __ball_change_x = 0
    __ball_change_y = 0

    def __init__(self, x, y, radius, color, speed=8):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.__ball_change_x = speed
        self.__ball_change_y = speed
        self.properties = pygame.Rect(self.x, self.y, self.radius, self.radius)

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.properties)

    def restart(self):
        self.properties.center = (screen_width / 2, screen_height / 2)
        self.__ball_change_x *= random.choice((1, -1))
        self.__ball_change_y *= random.choice((1, -1))

    def move(self, player, bot):
        if (self.properties.bottom >= screen_height) or (self.properties.top <= 0):
            self.__ball_change_y *= -1
        if self.properties.colliderect(player.properties) or self.properties.colliderect(bot.properties):
            self.__ball_change_x *= -1
        self.properties.x += self.__ball_change_x
        self.x = self.properties.x
        self.properties.y += self.__ball_change_y
        self.y = self.properties.y
        if (self.properties.right > screen_width + 1) or (self.properties.left < -1):
            if (self.properties.right >= screen_width):
                player.score += 1
            elif (self.properties.left <= 0):
                bot.score += 1
            self.restart()
