import pygame
import globalvar as gb

class Goose(pygame.sprite.Sprite):

    def __init__(self, filename, x, y):
        
        super().__init__()
        
        self.image = pygame.Surface([15, 15])

        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(gb.BLACK) 

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

class Goose(pygame.sprite.Sprite):

    def __init__(self, filename, x, y):
        
        super().__init__()
        
        self.image = pygame.Surface([15, 15])

        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(gb.BLACK) 

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


# HAMMER CLASS
class Hammer(pygame.sprite.Sprite):

    def __init__(self, filename, x, y):
        
        super().__init__()
        
        self.image = pygame.Surface([15, 15])

        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(gb.BLACK) 

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

        self.image.set_colorkey(gb.BLACK) 

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

        self.image.set_colorkey(gb.BLACK) 

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

class Player (pygame.sprite.Sprite):

    def __init__(self, filename, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(gb.BLACK)
        self.rect = self.image.get_rect()

        self.rect.x=x
        self.rect.y=y