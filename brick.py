import pygame
from main import screen

class Brick:

    #colors
    red = (255, 0, 0)
    orange = (255, 128, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    purple = (255, 0, 255)
    colors = [red, orange, green, blue, purple]
    def __init__(self, x, y, width, height, strength):
        self.rect = pygame.Rect(x, y, width, height)
        self.strength = strength
        self.color = Brick.colors[self.strength - 1]

    def get_strength(self):
        return self.strength

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def hit(self):
        self.strength -= 1
        if self.strength == 0:
            return True
        return False