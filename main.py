import pygame
import random
import math

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
player_width = 120
player_direction = 0
player_speed = 6

collision_occurred = False
collision_timer = 0
last_collision_time = pygame.time.get_ticks()

ball_x = WIDTH / 2
ball_y = HEIGHT - 30
ball_x_direction = 0
ball_y_direction = 0
ball_x_speed = 5
ball_y_speed = 5
ball_speed = 5

brick_width = 99
brick_height = 30
bricks = []
#strengths = [[3, 3, 3, 3, 3], [2, 2, 2, 2, 2],[2, 2, 2, 2, 2],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1]]
#for testing
strengths = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
#strengths = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]

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

    player = pygame.draw.rect(screen, black, [player_x, HEIGHT - 20, player_width, 15])
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
    player_x = max(0, min(WIDTH - player_width, player_x))
#wall collision handling
    if ball_x <= 10 or ball_x >= WIDTH - 10:
        ball_x_direction *= -1
#out of bounds handling (floor/ceiling)
    if ball_y <= 10:
        ball_y_direction *= -1
    if ball_y >= HEIGHT:
        quit_event()


#player collision handling
    if ball.colliderect(player):

        if not collision_occurred or pygame.time.get_ticks() - collision_timer >= 1000:
            # Where the ball hit the paddle, relative to its center (-1 = left edge, 1 = right edge)
            offset = (ball_x - player.centerx) / (player.width / 2)
            offset = max(-1, min(1, offset))

            # Angle from vertical scales with how far from center the ball hit
            max_bounce_angle = 75
            angle_of_incidence = offset * max_bounce_angle

            # Recompute the velocity from the bounce angle; direction carries the sign
            ball_x_speed = abs(math.sin(math.radians(angle_of_incidence)) * ball_speed)
            ball_y_speed = abs(math.cos(math.radians(angle_of_incidence)) * ball_speed)

            ball_x_direction = 1 if offset >= 0 else -1
            ball_y_direction = -1
            collision_occurred = True
            collision_timer = pygame.time.get_ticks()


#brick collision (resolve at most one brick per frame)
    hit_brick = None
    for row in bricks:
        for b in row:
            if ball.colliderect(b.rect):
                hit_brick = b
                break
        if hit_brick:
            break

    if hit_brick:
        # Figure out which side of the brick was hit from how much the ball overlaps each axis
        overlap_x = min(ball.right, hit_brick.rect.right) - max(ball.left, hit_brick.rect.left)
        overlap_y = min(ball.bottom, hit_brick.rect.bottom) - max(ball.top, hit_brick.rect.top)
        if overlap_x < overlap_y:
            ball_x_direction *= -1
        else:
            ball_y_direction *= -1

        hit_brick.strength -= 1
        hit_brick.hit()
        if hit_brick.strength == 0:
            row = next((r for r in bricks if hit_brick in r), None)
            if row:
                row.remove(hit_brick)

    pygame.display.flip()
pygame.quit()
