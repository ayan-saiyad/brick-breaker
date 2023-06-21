import pygame

class Brick:
    def __init__(self, x, y, width, height, strength):
        self.rect = pygame.Rect(x, y, width, height)
        self.strength = strength

    def get_strength(self):
        return self.strength
