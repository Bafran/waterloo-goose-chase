import globalvar as gb
import pygame

class Background:
    def __init__(self, image_path):
        self.image = image_path
        self.image = pygame.image.load(image_path)
        self.x = 0
        self.y = 0
    
    def printimage(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def scroll(self):
        self.x -= gb.SPEED