
# LIBRARY IMPORTS
import pygame
import playercontroller as pc
import globalvar as gb
import classes as cl
import updatebackground as updatebg
import random


test_list = []
for i in range(1):
    x = random.randrange(800, 1600)
    y = random.randrange(350, 400)
    test_list.append([x, y])

hammer_list = []
for i in range(1):
    x = random.randrange(800, 1600)
    y = random.randrange(350, 400)
    hammer_list.append([x, y])

fail_list = []
for i in range(1):
    x = random.randrange(800, 1600)
    y = random.randrange(350, 400)
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
goose = cl.Goose("imgs/goose.png", 0, 350) # create goose object
draw_goose = pygame.sprite.Group() # create goose sprite group
draw_goose.add(goose) # adding object to group

player = pc.Mario("./engineer.png", 100, 350)
draw_player = pygame.sprite.Group() # create goose sprite group
draw_player.add(player) # adding object to group

# draw_player = pygame.sprite.Group()
# draw_player.add(player)
player_velocity = 0
is_jumping = False


left = updatebg.Background("./imgs/backgrounds/background-1.jpeg", -799)
middle = updatebg.Background("./imgs/backgrounds/background-2.jpeg", 0)
right = updatebg.Background("./imgs/backgrounds/background-3.jpeg")



started = False
screen.blit(pygame.image.load("./imgs/titlescreen.png"), (0, 0))
pygame.display.update()

while not started:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            started = True
        if event.type == pygame.QUIT:
            started = True
            gb.DONE = True

left.printimage(screen)
middle.printimage(screen)
right.printimage(screen)

global gamended
gamended = False

# MAIN GAME LOOP
while not gamended and not gb.DONE:
    # --- Main event loop
    pc.eventcheck()

    # CLOSING THE WINDOW
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.isJump = True


    # SCREEN BACKGROUND
    left = left.scroll(screen)
    middle = middle.scroll(screen)
    right = right.scroll(screen)
    
    
    draw_goose.draw(screen) # draw the goose to the screen
    draw_player.draw(screen)

    # Player
    #player.draw(screen)
    player.jump()

    
    for i in range(len(test_list)):
        test = cl.Test("imgs/test.png", test_list[i][0], test_list[i][1])
        draw_test = pygame.sprite.Group()
        draw_test.add(test)
        draw_test.draw(screen)
        test_list[i][0] -= gb.SPEED 

        test_hit_list = pygame.sprite.spritecollide(player, draw_test, False)

        if test_list[i][0] < -50:
            y = random.randrange(350, 400) 
            test_list[i][1] = y 
            x = random.randrange(800, 1600) 
            test_list[i][0] = x
        if test_hit_list:
            updatebg.endgame(screen)
            gamended = True

    for i in range(len(hammer_list)):
        hammer = cl.Hammer("imgs/hammer.png", hammer_list[i][0], hammer_list[i][1])
        draw_hammer = pygame.sprite.Group()
        draw_hammer.add(hammer)
        draw_hammer.draw(screen)
        hammer_list[i][0] -= gb.SPEED 

        hammer_hit_list = pygame.sprite.spritecollide(player, draw_hammer, False)

        if hammer_list[i][0] < -50:
            y = random.randrange(350, 400)
            hammer_list[i][1] = y 
            x = random.randrange(800, 1600)
            hammer_list[i][0] = x
        if hammer_hit_list:
            updatebg.endgame(screen)
            gamended = True

    for i in range(len(fail_list)):
        fail = cl.Fail("imgs/fail.png", fail_list[i][0], fail_list[i][1])
        draw_fail = pygame.sprite.Group()
        draw_fail.add(fail)
        draw_fail.draw(screen)
        fail_list[i][0] -= gb.SPEED 

        fail_hit_list = pygame.sprite.spritecollide(player, draw_fail, False)

        if fail_list[i][0] < -50: 
            y = random.randrange(350, 400)
            fail_list[i][1] = y 
            x = random.randrange(800, 1600) 
            fail_list[i][0] = x
        if fail_hit_list:
            updatebg.endgame(screen)
            gamended = True


    pygame.display.update()

    # UPDATING THE SCREEN
    pygame.display.flip()

    # LIMIT TO 60 FRAMES/ SEC
    clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# CLOSE WINDOW & QUIT
pygame.quit()