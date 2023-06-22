import null as null
import pygame
import random

from brick import Brick

pygame.init()

clock = pygame.time.Clock()
fps = 60

WIDTH = 500
HEIGHT = 900

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (255, 0, 0)
orange = (255, 128, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)

player_x = 190
player_direction = 0
player_speed = 6

ball_x = WIDTH / 2
ball_y = HEIGHT - 30
ball_x_direction = 0
ball_y_direction = 0
ball_x_speed = 5
ball_y_speed = 5

brick_width = 99
brick_height = 30
bricks = []
strengths = [[1, 1, 1, 1, 1],
             [2, 2, 2, 2, 2],
             [3, 3, 3, 3, 3],
             [4, 4, 4, 4, 4],
             [5, 5, 5, 5, 5]]

colors = [red, orange, green, blue, purple]

screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font("freesansbold.ttf", 30)

active = False

def create_bricks():
    for i in range(5):
        row = []
        for j in range(5):
            row.append(Brick(i * brick_width + i, j * brick_height + j, brick_width, brick_height, strengths[j][i]))

        bricks.append(row)


def quit_event():
    global run
    run = False

def controls(event):
    global active, ball_y_direction, ball_x_direction, player_direction
    if not active:
        if event.key == pygame.K_SPACE:
            active = True
            ball_y_direction = -1
            ball_x_direction = random.choice([-1, 1])
    else:
        if event.key == pygame.K_RIGHT:
            player_direction = 1
        if event.key == pygame.K_LEFT:
            player_direction = -1

def keyup_event(event):
    global player_direction
    if event.key == pygame.K_RIGHT:
        player_direction = 0
    if event.key == pygame.K_LEFT:
        player_direction = 0

########################################################################################################################
run = True


while run:
    create_bricks()
    screen.fill(gray)
    clock.tick(fps)

    for row in bricks:
        for b in row:
            pygame.draw.rect(screen, b.color, b.rect)

    player = pygame.draw.rect(screen, black, [player_x, HEIGHT - 20, 120, 15])
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_event()
        elif event.type == pygame.KEYDOWN:
            controls(event)
        elif event.type == pygame.KEYUP:
            keyup_event(event)

    ball_x += ball_x_direction * ball_x_speed
    ball_y += ball_y_direction * ball_y_speed

    if ball_x <= 10 or ball_x >= WIDTH - 10:
        ball_x_direction *= -1

    if ball.colliderect(player):
        ball_y_direction *= -1



    player_x += player_direction * player_speed

    pygame.display.flip()
pygame.quit()
