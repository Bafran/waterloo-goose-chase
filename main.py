
# LIBRARY IMPORTS
import pygame
import playercontroller as pc
import globalvar as gb
import classes as cl


# PYGAME SET UP
# Initializing pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (gb.WIDTH, gb.HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Waterloo Goose Chase")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# OBJECTS 
goose = cl.Goose("imgs/goose.png", 0, 300) # create goose object
draw_goose = pygame.sprite.Group() # create goose sprite group
draw_goose.add(goose) # adding object to group


player = cl.Player("engineer.png", 450, 200)
draw_player = pygame.sprite.Group()
draw_player.add(player)

hammer = cl.Hammer("imgs/hammer.png", 100, 100) # create hammer object
draw_hammer = pygame.sprite.Group() # create hammer sprite group
draw_hammer.add(hammer) # adding object to group

fail = cl.Fail("imgs/fail.png", 200, 100) # create fail object
draw_fail = pygame.sprite.Group() # create fail sprite group
draw_fail.add(fail) # adding object to group

test = cl.Test("imgs/test.png", 300, 100) # create test object
draw_test = pygame.sprite.Group() # create test sprite group
draw_test.add(test) # adding object to group



# MAIN GAME LOOP
while not gb.DONE:
    # --- Main event loop
    pc.eventcheck()

    # CLOSING THE WINDOW
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # SCREEN BACKGROUND
    screen.fill(gb.BLUE)
    
    draw_goose.draw(screen) # draw the goose to the screen
    draw_player.draw(screen)
    draw_hammer.draw(screen) # draw the hammer to the screen
    draw_fail.draw(screen) # draw the fail to the screen
    draw_test.draw(screen) # draw the test to the screen


    # UPDATING THE SCREEN
    pygame.display.flip()

    # LIMIT TO 60 FRAMES/ SEC
    clock.tick(60)

# CLOSE WINDOW & QUIT
pygame.quit()