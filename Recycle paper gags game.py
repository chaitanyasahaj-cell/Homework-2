import pygame
import random
from pygame.locals import *
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recycle Project")

def load_image(path, size):
    return pygame.transform.scale(pygame.image.load(path).convert_alpha(), size)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, img, size, x, y):
        super().__init__()
        self.image = load_image(img, size)
        self.rect = self.image.get_rect(topleft=(x, y))

class Bin(Sprite):
    def __init__(self):
        super().__init__("images/bin.png", (50, 70), 400, 300)

# load the background once, not every frame
bg_image = load_image("images/bg.png", (WIDTH, HEIGHT))

object_bin = Bin()
all_sprites = pygame.sprite.Group(object_bin)

recyclable_items = pygame.sprite.Group()   # start empty, add sprites later
plastic = pygame.sprite.Group()

recyclable_images = ["images/bag.png", "images/box.png", "images/pencil.png"]

for i in range(10):
    item = Sprite(
        random.choice(recyclable_images),
        (20, 20),
        random.randint(0, WIDTH - 20),   
        random.randint(0, HEIGHT - 20)
    )
    all_sprites.add(item)
    recyclable_items.add(item)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_image, (0, 0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
