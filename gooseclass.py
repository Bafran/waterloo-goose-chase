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