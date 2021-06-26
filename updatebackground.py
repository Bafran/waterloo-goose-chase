import globalvar as gb
import pygame
import os, random

class Background:
    def __init__(self, image_path, x=gb.WIDTH):
        self.image = image_path
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = 0
    
    def printimage(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def scroll(self, screen):
        if self.x <= -gb.WIDTH:
            newimage = random.choice(os.listdir(".\\imgs\\backgrounds")) #change dir name to whatever
            self.x = gb.WIDTH*2
            return Background("./imgs/backgrounds/" + str(newimage), self.x) 
        self.x -= gb.SPEED
        screen.blit(self.image, (self.x, self.y))
        return self