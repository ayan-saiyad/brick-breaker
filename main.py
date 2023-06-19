import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

WIDTH = 500
HEIGHT = 900
player_x = 190
ball_x = WIDTH / 2
ball_y = HEIGHT - 30

blocks = [[5, 5, 5, 5, 5], [4, 4, 4, 4, 4], [3, 3, 3, 3, 3], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1]]

screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font("freesansbold.ttf", 30)

run = True
while run:

    screen.fill(gray);
    clock.tick(fps)

    player = pygame.draw.rect(screen, black, [player_x, HEIGHT - 20, 120, 15])
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
