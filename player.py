from constants import *
from paddle import Paddle


class Player(Paddle):
    player_change = 0
    is_key_up = False
    score = 0

    def __init__(self, x, y, width, height, color, speed=8):
        super().__init__(x, y, width, height, color)
        self.speed = speed

    def reset(self):
        self.y = screen_height / 2 - 100
        self.properties.y = self.y
        self.score = 0
        self.player_change = 0
        self.is_key_up = False

    def move(self):
        if (self.y + self.player_change >= 0) and (self.y + self.player_change + self.height <= screen_height):
            self.properties.y += self.player_change
        elif (self.properties.top > 0) and (self.properties.top < -self.player_change):
            self.properties.y -= self.properties.top
        elif (self.properties.bottom < screen_height) and (screen_height - self.properties.bottom < self.player_change):
            self.properties.y += screen_height - self.properties.bottom
        self.y = self.properties.y
