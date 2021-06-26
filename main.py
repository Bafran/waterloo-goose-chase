# LIBRARY IMPORTS
import pygame
import playercontroller as pc
import globalvar as gb

# COLOURS 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# PYGAME SET UP
# Initializing pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (1000, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Waterloo Goose Chase")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()




# MAIN GAME LOOP
while not gb.DONE:
    # --- Main event loop
    pc.eventcheck()

    screen.fill(WHITE)
    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()