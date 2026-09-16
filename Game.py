import pygame
from pygame.locals import *
pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Recycle Project")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
