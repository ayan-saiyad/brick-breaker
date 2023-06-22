import pygame


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
        self.x = x
        self.y = y
        self.strength = strength
        self.color = Brick.colors[self.strength - 1]