import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

# --- Screen size (16:9) ---
screen_width = 640
screen_height = 360  # 640 / 16 * 9 = 360, exact 16:9

# Scale factor relative to the original 864-wide artwork
SCALE = screen_width / 864

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#define font
font = pygame.font.SysFont('Bauhaus 93', int(60 * SCALE))

#define colours
white = (255, 255, 255)

#define game variables
ground_scroll = 0
scroll_speed = max(1, int(4 * SCALE))
flying = False
game_over = False
pipe_gap = int(150 * SCALE)
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

def scale_image(img, w, h):
    return pygame.transform.scale(img, (w, h))

#load images
bg = pygame.image.load('Games/Flappy/img/bg.png').convert()
bg = pygame.transform.scale(bg, (screen_width, screen_height))  # stretch to fill window exactly, once

ground_raw = pygame.image.load('Games/Flappy/img/ground.png').convert_alpha()
gw, gh = ground_raw.get_size()
ground_img = pygame.transform.scale(ground_raw, (int(gw * SCALE), int(gh * SCALE)))

button_raw = pygame.image.load('Games/Flappy/img/restart.png').convert_alpha()
bw, bh = button_raw.get_size()
button_img = pygame.transform.scale(button_raw, (int(bw * SCALE), int(bh * SCALE)))

# ground level: keep ground_img's top aligned to bottom of screen minus its own height,
# so it always sits flush at the bottom of the window regardless of scale
ground_level = screen_height - ground_img.get_height()

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = int(100 * SCALE)
    flappy.rect.y = int(screen_height / 2)
    flappy.vel = 0
    return 0


class Bird(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f"Games/Flappy/img/bird{num}.png").convert_alpha()
            iw, ih = img.get_size()
            img = pygame.transform.scale(img, (int(iw * SCALE), int(ih * SCALE)))
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
        if flying == True:
            #apply gravity
            self.vel += 0.5 * SCALE
            if self.vel > 8 * SCALE:
                self.vel = 8 * SCALE
            if self.rect.bottom < ground_level:
                self.rect.y += int(self.vel)

        if game_over == False:
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10 * SCALE
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            #handle the animation
            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            #rotate the bird
            self.image = pygame.transform.rotate(self.images[self.index], -2 * self.vel)
        else:
            #point the bird downwards
            self.image = pygame.transform.rotate(self.images[self.index], -90)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Games/Flappy/img/pipe.png").convert_alpha()
        iw, ih = img.get_size()
        self.image = pygame.transform.scale(img, (int(iw * SCALE), int(ih * SCALE)))
        self.rect = self.image.get_rect()

        #position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()

flappy = Bird(int(100 * SCALE), int(screen_height / 2))
bird_group.add(flappy)

#create restart button instance
button = Button(screen_width // 2 - button_img.get_width() // 2,
                 screen_height // 2 - button_img.get_height() // 2,
                 button_img)


run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(bg, (0, 0))

    pipe_group.draw(screen)
    bird_group.draw(screen)
    bird_group.update()

    #draw and scroll the ground (two copies side by side so it tiles seamlessly)
    screen.blit(ground_img, (ground_scroll, ground_level))
    screen.blit(ground_img, (ground_scroll + ground_img.get_width(), ground_level))

    #check the score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False

    draw_text(str(score), font, white, int(screen_width / 2), int(20 * SCALE))

    #look for collision
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True
    #once the bird has hit the ground, its game over and no longer flying
    if flappy.rect.bottom >= ground_level:
        game_over = True
        flying = False

    if flying == True and game_over == False:
        #generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(int(-100 * SCALE), int(100 * SCALE))
            btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
            top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        pipe_group.update()

        ground_scroll -= scroll_speed
        if abs(ground_scroll) > ground_img.get_width():
            ground_scroll = 0

    #check for game over and reset
    if game_over == True:
        if button.draw() == True:
            game_over = False
            score = reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()

pygame.quit()