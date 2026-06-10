import pygame

import os
current_folder = os.path.dirname(os.path.abspath(__file__))

pygame.init()
pygame.display.set_caption('Rocket in Space')

# Set the height and width of the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# Define the Player sprite
# Player starts at (0,0) by default
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.image.load("character.png").convert_alpha()
        self.image = pygame.image.load(os.path.join(current_folder, "character.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
            

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

#end of the class

#make a group os all the sprites
sprites = pygame.sprite.Group()

def startgame():
    player = Player()
    sprites.add(player)

    #start the game loop
    while True:
    #Look at every event
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
               # if it is quit the game
                pygame.quit()
                exit(0)
        #Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        # Add background image
        #screen.blit(pygame.image.load("background.png"), (0,0))
        screen.blit(pygame.image.load(os.path.join("background.png")), (0,0))

        #draw the sprites
        sprites.draw(screen)

        pygame.display.update()

startgame()