
# LIBRARY IMPORTS
import pygame
import playercontroller as pc
import globalvar as gb


# VARIABLES
done = False


# COLOURS 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (157, 210, 235)



# PYGAME SET UP
# Initializing pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (1000, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Waterloo Goose Chase")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# CLASSES

# GOOSE CLASS
class Goose(pygame.sprite.Sprite):

    def __init__(self, filename, x, y):
        
        super().__init__()
        
        self.image = pygame.Surface([15, 15])

        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(BLACK) 

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


# HAMMER CLASS
class Hammer(pygame.sprite.Sprite):

    def __init__(self, filename, x, y):
        
        super().__init__()
        
        self.image = pygame.Surface([15, 15])

        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(BLACK) 

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    # Movement method
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    # Update method
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y


# FAIL CLASS
class Fail(pygame.sprite.Sprite):

    def __init__(self, filename, x, y):
        
        super().__init__()
        
        self.image = pygame.Surface([15, 15])

        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(BLACK) 

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    # Movement method
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    # Update method
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y




# TEST CLASS
class Test(pygame.sprite.Sprite):

    def __init__(self, filename, x, y):
        
        super().__init__()
        
        self.image = pygame.Surface([15, 15])

        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(BLACK) 

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    # Movement method
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    # Update method
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y



# OBJECTS 

goose = Goose("imgs/goose.png", 0, 600) # create goose object
draw_goose = pygame.sprite.Group() # create goose sprite group
draw_goose.add(goose) # adding object to group

hammer = Hammer("imgs/hammer.png", 100, 100) # create hammer object
draw_hammer = pygame.sprite.Group() # create hammer sprite group
draw_hammer.add(hammer) # adding object to group

fail = Fail("imgs/fail.png", 200, 100) # create fail object
draw_fail = pygame.sprite.Group() # create fail sprite group
draw_fail.add(fail) # adding object to group

test = Test("imgs/test.png", 300, 100) # create test object
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
    screen.fill(BLUE)
    
    
    draw_goose.draw(screen) # draw the goose to the screen
    draw_hammer.draw(screen) # draw the hammer to the screen
    draw_fail.draw(screen) # draw the fail to the screen
    draw_test.draw(screen) # draw the test to the screen


    # UPDATING THE SCREEN
    pygame.display.flip()

    # LIMIT TO 60 FRAMES/ SEC
    clock.tick(60)

# CLOSE WINDOW & QUIT
pygame.quit()