"""
title: pygame_practice
author: Sahaana
date: 2019-06-14 09:48
"""

import pygame

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# define colors
BLACK = (0, 0, 0)
TEAL = (110, 163, 161)

PI = 3.141592653

# Set the height and width of the screen
size = (400, 500)
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

    pygame.draw.circle(screen, TEAL, [200, 200], 160)
    pygame.draw.arc(screen, BLACK, [100, 160, 200, 125], PI, 0, 5)
    pygame.draw.ellipse(screen, BLACK, [120, 130, 50, 60])
    pygame.draw.ellipse(screen, BLACK, [220, 130, 50, 60])

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()