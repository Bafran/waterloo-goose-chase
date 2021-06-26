
# LIBRARY IMPORTS
import pygame
import playercontroller as pc
import globalvar as gb
import classes as cl
import random


test_list = []
for i in range(1):
    x = random.randrange(800, 1600)
    y = random.randrange(300, 350)
    test_list.append([x, y])

hammer_list = []
for i in range(1):
    x = random.randrange(800, 1600)
    y = random.randrange(300, 350)
    hammer_list.append([x, y])

fail_list = []
for i in range(1):
    x = random.randrange(800, 1600)
    y = random.randrange(300, 350)
    fail_list.append([x, y])



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

    
    for i in range(len(test_list)):
        test = cl.Test("imgs/test.png", test_list[i][0], test_list[i][1])
        draw_test = pygame.sprite.Group()
        draw_test.add(test)
        draw_test.draw(screen)
        test_list[i][0] -= 2 

        if test_list[i][0] < -50: 
            y = random.randrange(300, 350) 
            test_list[i][1] = y 
            x = random.randrange(800, 1600) 
            test_list[i][0] = x

    for i in range(len(hammer_list)):
        hammer = cl.Hammer("imgs/hammer.png", hammer_list[i][0], hammer_list[i][1])
        draw_hammer = pygame.sprite.Group()
        draw_hammer.add(hammer)
        draw_hammer.draw(screen)
        hammer_list[i][0] -= 2 

        if hammer_list[i][0] < -50: 
            y = random.randrange(300, 350)
            hammer_list[i][1] = y 
            x = random.randrange(800, 1600)
            hammer_list[i][0] = x

    for i in range(len(fail_list)):
        fail = cl.Fail("imgs/fail.png", fail_list[i][0], fail_list[i][1])
        draw_fail = pygame.sprite.Group()
        draw_fail.add(fail)
        draw_fail.draw(screen)
        fail_list[i][0] -= 2 

        if fail_list[i][0] < -50: 
            y = random.randrange(300, 350)
            fail_list[i][1] = y 
            x = random.randrange(800, 1600) 
            fail_list[i][0] = x


    # UPDATING THE SCREEN
    pygame.display.flip()

    # LIMIT TO 60 FRAMES/ SEC
    clock.tick(60)

# CLOSE WINDOW & QUIT
pygame.quit()