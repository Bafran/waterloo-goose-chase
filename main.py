
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



# OBJECTS 

goose = Goose("imgs/goose.png", 0, 600) # create goose object
draw_goose = pygame.sprite.Group() # create goose sprite group
draw_goose.add(goose) # adding object to group





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



    # UPDATING THE SCREEN
    pygame.display.flip()

    # LIMIT TO 60 FRAMES/ SEC
    clock.tick(60)

# CLOSE WINDOW & QUIT
pygame.quit()