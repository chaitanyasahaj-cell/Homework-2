import pygame
from pygame.locals import *
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recycle Project")

def load_image(path, size):
    return pygame.transform.scale(pygame.image.load(path).convert_alpha(), size)

def draw_bg(image_name):
    image_bg = load_image(image_name,(WIDTH, HEIGHT))
    screen.blit(image_bg,(0,0))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, img, size, x,y):
        super().__init__()
        self.image = load_image(img, size)
        self.rect = self.image.get_rect(topleft = (x,y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw_bg("Sahaj\\Games\\Recycle_Paper_Bag_NEW\\images\\bg.png")
    pygame.display.update()
