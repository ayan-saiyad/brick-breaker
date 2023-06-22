import pygame


class Brick:

    #colors
    a = (255, 0, 0)
    b = (205, 0, 0)
    c = (155, 0, 0)
    d = (105, 0, 0)
    e = (30, 0, 0)
    colors = [a, b, c, d, e]
    def __init__(self, x, y, width, height, strength):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.strength = strength
        self.color = Brick.colors[self.strength - 1]