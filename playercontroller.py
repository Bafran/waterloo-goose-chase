import pygame
import globalvar as gb

ani = 4
tx, ty = 5, 5

def eventcheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gb.DONE = True

class Player (pygame.sprite.Sprite):

    def __init__(self, filename, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(gb.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def jump(self, velocity):
        velocity = -100
        return velocity
    
    def update(self, velocity):
        self.rect.y += velocity
        if self.rect.y > 400:
            self.rect.y = 399
            velocity = 1
        return velocity

class Mario():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # isJump and jumpCount should be attributes of Mario.
        self.isJump = False
        self.jumpCount = 10

    def draw(self, screen, image):
        screen.blit(pygame.image.load(image), (self.x, self.y))

    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 3
                if self.jumpCount < 0:
                    neg = -3
                self.y -= self.jumpCount**2 * 0.1 * neg
                self.jumpCount -= 0.5
            else:
                self.isJump = False
                self.jumpCount = 10