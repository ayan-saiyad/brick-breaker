import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (255, 0, 0)
orange = (255, 128, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)

WIDTH = 500
HEIGHT = 900
player_x = 190
ball_x = WIDTH / 2
ball_y = HEIGHT - 30

board = [[5, 5, 5, 5, 5], [4, 4, 4, 4, 4], [3, 3, 3, 3, 3], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1]]

colors = [red, orange, green, blue, purple]

screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font("freesansbold.ttf", 30)

active = False


def drawblocks(blocks):
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            pygame.draw.rect(screen, colors[(blocks[i][j]) - 1], [j * 100, i * 40, 98, 38])


run = True
while run:

    screen.fill(gray)
    clock.tick(fps)

    drawblocks(board)

    player = pygame.draw.rect(screen, black, [player_x, HEIGHT - 20, 120, 15])
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
