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

collision = 0

ball_x = WIDTH / 2
ball_y = HEIGHT - 30
ball_x_direction = 0
ball_y_direction = 0
ball_x_speed = 5
ball_y_speed = 5

brick_width = 99
brick_height = 30
bricks = []
strengths = [[5, 5, 5, 5, 5],
             [4, 4, 4, 4, 4],
             [3, 3, 3, 3, 3],
             [2, 2, 2, 2, 2],
             [1, 1, 1, 1, 1]]
#for testing
#strengths = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

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
create_bricks()

while run:

    screen.fill(gray)
    clock.tick(fps)

    for row in bricks:
        for b in row:
            pygame.draw.rect(screen, b.color, b.rect)

    player = pygame.draw.rect(screen, black, [player_x, HEIGHT - 20, 120, 15])
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

#key press handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_event()
        elif event.type == pygame.KEYDOWN:
            controls(event)
        elif event.type == pygame.KEYUP:
            keyup_event(event)
#ball/player velocity
    ball_x += ball_x_direction * ball_x_speed
    ball_y += ball_y_direction * ball_y_speed
    player_x += player_direction * player_speed
#wall collision handling
    if ball_x <= 10 or ball_x >= WIDTH - 10:
        ball_x_direction *= -1
#out of bounds handling (floor/ceiling)
    if ball_y <= 10 or ball_y >= HEIGHT:
        quit_event()

#player collision handling
    if ball.colliderect(player):
        if not collision % 2 == 0:
            ball_y_direction *= -1
            collision += 1

#brick collision
    bricks_to_remove = []
    for row in bricks:
        for b in row:
            if ball.colliderect(b.rect):
                if collision % 2 == 0:
                    ball_y_direction *= -1
                    collision += 1
                    b.strength -= 1
                    if b.strength == 0:
                        bricks_to_remove.append(b)
#removing bricks once strength depletes
    for b in bricks_to_remove:
        row = next((r for r in bricks if b in r), None)
        if row:
            row.remove(b)

    pygame.display.flip()
pygame.quit()
