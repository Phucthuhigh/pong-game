from player import Player
from constants import *


class AI(Player):
    def __init__(self, x, y, width, height, color, speed=8):
        super().__init__(x, y, width, height, color, speed)

    def move(self, ball):
        if ball.y > self.y:
            self.player_change = self.speed
        elif ball.y < self.y:
            self.player_change = -self.speed
        else:
            self.player_change = 0
        if (self.y + self.player_change >= 0) and (self.y + self.player_change + self.height <= screen_height):
            self.properties.y += self.player_change
        elif (self.properties.top > 0) and (self.properties.top < -self.player_change):
            self.properties.y -= self.properties.top
        elif (self.properties.bottom < screen_height) and (screen_height - self.properties.bottom < self.player_change):
            self.properties.y += screen_height - self.properties.bottom
        self.y = self.properties.y
