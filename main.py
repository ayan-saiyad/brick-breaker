import pygame
import random

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

board = [[5, 5, 5, 5, 5], [4, 4, 4, 4, 4], [3, 3, 3, 3, 3], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1]]

colors = [red, orange, green, blue, purple]

screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font("freesansbold.ttf", 30)

active = False


def drawblocks(blocks):
    board_squares = []
    for i in range(len(blocks)):
        row = []
        for j in range(len(blocks[i])):
            block = pygame.draw.rect(screen, colors[(blocks[i][j]) - 1], [j * 100, i * 40, 98, 38])
            row.append([block, (i, j)])

        board_squares.append(row)

    return board_squares
def handle_quit_event():
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

def handle_keyup_event(event):
    global player_direction
    if event.key == pygame.K_RIGHT:
        player_direction = 0
    if event.key == pygame.K_LEFT:
        player_direction = 0


run = True
while run:

    screen.fill(gray)
    clock.tick(fps)

    squares = drawblocks(board)

    player = pygame.draw.rect(screen, black, [player_x, HEIGHT - 20, 120, 15])
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            handle_quit_event()
        elif event.type == pygame.KEYDOWN:
            controls(event)
        elif event.type == pygame.KEYUP:
            handle_keyup_event(event)

    ball_x += ball_x_direction * ball_x_speed
    ball_y += ball_y_direction * ball_y_speed

    if ball_x <= 10 or ball_x >= WIDTH - 10:
        ball_x_direction *= -1

    for i in range(len(squares)):
        if ball.colliderect(squares[i][0]):
            ball_y_direction *= -1
            board[squares[i][1][0]][squares[i][1][1]] -= 1



    if ball.colliderect(player):
        ball_y_direction *= -1


    player_x += player_direction * player_speed

    pygame.display.flip()
pygame.quit()
