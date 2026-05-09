import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

gun = Actor('gun')
gun.pos = (WIDTH // 2, HEIGHT - 30)
gun.scale = 0.025

bullets = []
apples = []

def spawn_apples():
    apples.clear()

    for i in range(5):
        apple = Actor('apple')
        apple.x = randint(50, WIDTH - 50)
        apple.y = randint(-300, -50)
        apple.scale = 0.002
        apples.append(apple)

spawn_apples()

def draw():
    screen.clear()
    screen.fill("white")

    gun.draw()

    for apple in apples:
        apple.draw()

    for bullet in bullets:
        bullet.draw()

    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("white")
        screen.draw.text(
            "YOU WON!",
            fontsize=60,
            color="red",
            center=(WIDTH // 2, HEIGHT // 2)
        )

def update():
    global score, game_over

    if game_over:
        return

    if keyboard.left and gun.x > 20:
        gun.x -= 5

    if keyboard.right and gun.x < WIDTH - 20:
        gun.x += 5

    for apple in apples:
        apple.y += 2

    for bullet in bullets[:]:
        bullet.y -= 7

        for apple in apples[:]:
            if bullet.colliderect(apple):
                if bullet in bullets:
                    bullets.remove(bullet)
                apples.remove(apple)
                score += 1
                break

        if bullet.y < 0:
            if bullet in bullets:
                bullets.remove(bullet)

    if len(apples) == 0:
        spawn_apples()

    if score >= 10:
        game_over = True

def on_key_down(key):
    if key == keys.LCTRL or key == keys.RCTRL:
        if not game_over:
            bullet = Actor('bullet')
            bullet.pos = (gun.x, gun.y - 15)
            bullet.scale = 0.01
            bullets.append(bullet)

pgzrun.go()