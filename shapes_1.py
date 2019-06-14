"""
title: shapes_1
author: Sahaana
date: 2019-06-14 10:46
"""

import pygame

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# define colors
BLACK = (0, 0, 0)
TEAL = (110, 163, 161)
BROWN = (222, 184, 135)
WHITE = (255, 255, 255)
ORANGE = (255, 160, 122)

PI = 3.141592653

# Set the height and width of the screen
size = (600, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

ball_pos = 0
ball_change = 1


def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, ORANGE, [70 + x, 460 + ball_pos + y, 40, 40])
    # hair main
    pygame.draw.circle(screen, BLACK, [200 + x, 180 + y], 113)
    # hair buns
    pygame.draw.circle(screen, BLACK, [250 + x, 280 + y], 40)
    pygame.draw.circle(screen, BLACK, [150 + x, 280 + y], 40)
    # head
    pygame.draw.circle(screen, BROWN, [200 + x, 200 + y], 100)
    # the mouth
    pygame.draw.arc(screen, BLACK, [140 + x, 165 + y, 125, 100], PI, 0, 5)
    # Drew the eyes
    pygame.draw.ellipse(screen, BLACK, [150 + x, 155 + y, 30, 45])
    pygame.draw.ellipse(screen, BLACK, [220 + x, 155 + y, 30, 45])
    # Body line
    pygame.draw.line(screen, BROWN, [200 + x, 300 + y], [200 + x, 600 + y], 8)
    # arm line right
    pygame.draw.line(screen, BROWN, [200 + x, 350 + y], [300 + x, 450 + y], 8)
    # arm line left
    pygame.draw.line(screen, BROWN, [200 + x, 350 + y], [100 + x, 450 + y], 8)
    # leg line left
    pygame.draw.line(screen, BROWN, [200 + x, 600 + y], [100 + x, 675 + y], 8)
    # leg line right
    pygame.draw.line(screen, BROWN, [200 + x, 600 + y], [300 + x, 675 + y], 8)


# Loop as long as done == False
while not done:
    ball_pos += ball_change

    if ball_pos > 90:
        ball_change -= 3
    if ball_pos < 100:
        ball_change += 3

    # User did something
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -6
    if keys[pygame.K_RIGHT]:
        x_speed = 6
    if keys[pygame.K_UP]:
        y_speed = -6
    if keys[pygame.K_DOWN]:
        y_speed = 6

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0

    screen.fill(WHITE)

    draw_stick_figure(screen, x_coord, y_coord)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
