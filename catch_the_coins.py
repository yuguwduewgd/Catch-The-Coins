from ursina import *
import random

app = Ursina()
window.title = "2D Coin Collector"
window.borderless = False
window.color = color.black

# Player (2D cube)
player = Entity(model='quad', color=color.orange, scale=(1,1), position=(0,0,0), collider='box')

# Ground (just for background)
ground = Entity(model='quad', color=color.azure, scale=(20,20), position=(0,0,1))

# Coins
coins = []
for _ in range(10):
    x = random.randint(-9,9)
    y = random.randint(-9,9)
    coin = Entity(model='quad', color=color.yellow, scale=(0.5,0.5), position=(x,y,0), collider='box')
    coins.append(coin)

# Score
score = 0
score_text = Text(text=f"Score: {score}", scale=2, position=(-0.85,0.45), color=color.white)

speed = 0.2

# Orthographic camera (2D top-down)
camera.orthographic = True
camera.position = (0,0,-10)
camera.fov = 20

def update():
    global score

    # Player movement (2D)
    if held_keys['w']:
        player.y += speed
    if held_keys['s']:
        player.y -= speed
    if held_keys['a']:
        player.x -= speed
    if held_keys['d']:
        player.x += speed

    # Check coin collection
    for coin in coins:
        if coin.enabled and player.intersects(coin).hit:
            coin.disable()
            score += 1
            score_text.text = f"Score: {score}"

    # Keep player in bounds
    if abs(player.x) > 10 or abs(player.y) > 10:
        print("Game Over! You went off the screen!")
        application.quit()

app.run()
