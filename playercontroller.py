import pygame
import globalvar as gb

def eventcheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gb.DONE = True
