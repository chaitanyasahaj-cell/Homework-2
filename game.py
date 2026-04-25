import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

gun = Actor('gun')
gun.pos = (WIDTH//2, HEIGHT - 10)

apple = Actor('apple')
apple.pos = (randint(50, WIDTH-50), 30)

bullets = []

def draw():
    screen.clear()
    screen.fill("lightblue")

    gun.draw()
    apple.draw()

    for bullet in bullets:
        bullet.draw()

    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("YOU WON!", fontsize=60, color="red", center=(WIDTH/2, HEIGHT/2))


def update():
    global score, game_over

    if game_over:
        return

    if keyboard.left and gun.x > 0:
        gun.x -= 5
    if keyboard.right and gun.x < WIDTH:
        gun.x += 5

    for bullet in bullets[:]:
        bullet.y -= 7

        if bullet.colliderect(apple):
            bullets.remove(bullet)
            score += 1
            apple.pos = (randint(50, WIDTH-50), 30)

        elif bullet.y < 0:
            bullets.remove(bullet)

    if score >= 10:
        game_over = True


def on_key_down(key):
    if key == keys.LCTRL or key == keys.RCTRL:
        if not game_over:
            bullet = Actor('bullet')
            bullet.pos = (gun.x, gun.y - 30)
            bullet.scale = 0.2
            bullets.append(bullet)


pgzrun.go()