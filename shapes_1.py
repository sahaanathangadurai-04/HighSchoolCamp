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
BROWN = (174, 134, 93)
WHITE = (255, 255, 255)

PI = 3.141592653

# Set the height and width of the screen
size = (600, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    screen.fill(WHITE)
    # hair
    pygame.draw.circle(screen, BLACK, [200, 180], 113)
    pygame.draw.circle(screen, BLACK, [250, 280], 40)
    pygame.draw.circle(screen, BLACK, [150, 280], 40)
    pygame.draw.arc(screen, BLACK, [200, 160, 150, 100], 0, PI)  # WORK on for bangs
    # head
    pygame.draw.circle(screen, BROWN, [200, 200], 100)
    pygame.draw.arc(screen, BLACK, [140, 165, 125, 100], PI, 0, 5)
    pygame.draw.ellipse(screen, BLACK, [150, 155, 30, 45])
    pygame.draw.ellipse(screen, BLACK, [220, 155, 30, 45])
    # Body line
    pygame.draw.line(screen, BROWN, [200, 300], [200, 600], 8)
    # arm line right
    pygame.draw.line(screen, BROWN, [200, 350], [300, 450], 8)
    # arm line left
    pygame.draw.line(screen, BROWN, [200, 350], [100, 450], 8)
    # leg line left
    pygame.draw.line(screen, BROWN, [200, 600], [100, 675], 8)
    # leg line right
    pygame.draw.line(screen, BROWN, [200, 600], [300, 675], 8)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()