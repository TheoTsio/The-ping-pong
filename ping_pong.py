from pygame import *


window = display.set_mode((600, 500))
window.fill((200, 255, 255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed


racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

run = True
clock = time.Clock()

FPS = 60
speed_X = 3
speed_Y = 3
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill((200, 255, 255))
    racket1.reset()
    racket2.reset()
    racket1.update()
    racket2.update2()

    ball.reset()

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_X = speed_X * (-1)

    ball.rect.x += speed_X
    ball.rect.y += speed_Y

    clock.tick(FPS)
    display.update()
