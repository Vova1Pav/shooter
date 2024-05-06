#Создай собственный Шутер!

from pygame import *
from random import randint
import time as tm
mixer.init()
font.init()

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))

display.set_caption('shooter')
background = transform.scale(
    image.load('galaxy.jpg'), 
    (win_width, win_height)
)

mixer.music.load('space.ogg')
mixer.music.play()

lives = 3

font1 = font.SysFont('Calibri', 36)
lost = 0
txt_loose = font1.render(
    'Пропущено: ' + str(lost), 1, (255, 255, 255)
)

font2 = font.SysFont('Calibri', 36)
win = 0
txt_win = font2.render(
    'Поражено: ' + str(win), 1, (255, 255, 255)
)

font3 = font.SysFont('Arial', 36)
txt_winner = font3.render(
    'YOU WIN!', 1, (117, 253, 0)
)

font4 = font.SysFont('Arial', 36)
txt_loser = font4.render(
    'YOU LOOSE!', 1, (255, 0, 0)
)

font5 = font.SysFont('Arial', 36)
lives_txt = font4.render(
    str(lives), 1, (255, 0, 0)
)

font6 = font.SysFont('Arial', 36)
txt_reload = font4.render(
    'Wait, reload...', 1, (145, 130, 181)
)

font7 = font.SysFont('Arial', 36)
txt_reset = font4.render(
    'Press R to restart, press Q to exit, press P to pause', 1, (255, 255, 255)
)


font7 = font.SysFont('Arial', 36)
txt_pause = font4.render(
    'You on pause...', 1, (145, 130, 181)
)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_ps = key.get_pressed()

        if keys_ps[K_LEFT] and self.rect.x >0:
            self.rect.x -= self.speed
        
        if keys_ps[K_RIGHT] and self.rect.x <640:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets_group.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(10, 490)
            self.speed = randint(1, 3)
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

class Asteroids(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(10, 490)
            self.speed = randint(1, 3)

class Button_PNG():
    def __init__(self, btn_image, btn_x, btn_y, w, h):
        self.image = transform.scale(image.load(btn_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = btn_x
        self.rect.y = btn_y
        self.pressed = False

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
pausebtn_png = Button_PNG("pause.png",600,10,45,45)

player = Player('rocket.png', 325, 440, 55, 55, 10)

enemy = Enemy('ufo.png', randint(10, 490), 0, 80, 50, randint(1, 3))
enemy2 = Enemy('ufo.png', randint(10, 490), 0, 80, 50, randint(1, 3))
enemy3 = Enemy('ufo.png', randint(10, 490), 0, 80, 50, randint(1, 3))
enemy4 = Enemy('ufo.png', randint(10, 490), 0, 80, 50, randint(1, 3))
enemy5= Enemy('ufo.png', randint(10, 490), 0, 80, 50, randint(1, 3))
asteroid = Asteroids('asteroid.png', randint(10, 490), 0, 80, 50, 1)
asteroid1 = Asteroids('asteroid.png', randint(10, 490), 0, 80, 50, 1)
asteroid2 = Asteroids('asteroid.png', randint(10, 490), 0, 80, 50, 1)

enemy_group = sprite.Group()
asteroids = sprite.Group()
enemy_group.add(enemy)
enemy_group.add(enemy2)
enemy_group.add(enemy3)
enemy_group.add(enemy4)
enemy_group.add(enemy5)
asteroids.add(asteroid)
asteroids.add(asteroid1)
asteroids.add(asteroid2)


bullets_group = sprite.Group()


clock = time.Clock()
FPS = 90

game = True

num_fire = 0
rel_time = False

finish = False

while game:
    for e in event.get():
        if finish != True or pausebtn_png.pressed != True:
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                if pausebtn_png.collidepoint(x, y):
                    pausebtn_png.pressed = True
                    if finish != True:
                        finish = True
                        pausebtn_png.pressed = False
                    elif finish == True:
                        finish = False


        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire <8 and rel_time == False:
                    player.fire()
                    num_fire += 1
                if num_fire >=8 and rel_time == False:
                    rel_time = True
                    last_time = tm.time()
            if e.key == K_r:
                finish = False
                win = 0
                lost = 0
                lives = 3
                for i in enemy_group:
                    i.kill()
                for i in bullets_group:
                    i.kill()
                for i in asteroids:
                    i.kill()
                for i in range(5):
                    enemy7 = Enemy('ufo.png', randint(10, 490), 0, 80, 50, randint(1, 3))
                    enemy_group.add(enemy7)
                for i in range(3):
                    asteroid4 = Enemy('asteroid.png', randint(10, 490), 0, 80, 50, 1)
                    asteroids.add(asteroid4)

            if e.key == K_p:
                if finish != True:
                    finish = True
                    window.blit(txt_pause, (250, 250))
                elif finish:
                    finish = False

            if e.key == K_q:
                game = False
    if finish == False:
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        enemy_group.draw(window)
        enemy_group.update()
        bullets_group.draw(window)
        bullets_group.update()
        asteroids.draw(window)
        asteroids.update()
        pausebtn_png.reset()
        txt_loose = font1.render(
        'Пропущено: ' + str(lost), 1, (255, 255, 255)
        )
        txt_win = font2.render(
            'Поражено: ' + str(win), 1, (255, 255, 255)
        )
        lives_txt = font4.render(
        str(lives), 1, (255, 0, 0)
        )



        window.blit(txt_win, (10, 40))
        window.blit(txt_loose, (10, 10))
        window.blit(lives_txt, (650, 10))

        if rel_time == True:
            now_time = tm.time()
            if now_time - last_time <= 3:
                txt_reload = font4.render(
                'Wait, reload...', 1, (145, 130, 181)
                )
                window.blit(txt_reload, (325, 450))
                
            else:
                num_fire = 0
                rel_time = False

        collides_2 = sprite.groupcollide(asteroids, bullets_group, False, True)
        collides = sprite.groupcollide(enemy_group, bullets_group, True, True)     
        
        for every in collides:
            win += 1
            enemy6 = Enemy('ufo.png', randint(10, 490), 0, 80, 50, randint(1, 3))
            enemy_group.add(enemy6)
        
        ship_collide = sprite.spritecollide(player, enemy_group, False)
        ship_collide2 = sprite.spritecollide(player, asteroids, False)

        if ship_collide or ship_collide2:
            lives -= 1
            for enem in ship_collide:
                enem.kill()
                enemy6 = Enemy('ufo.png', randint(10, 490), 0, 80, 50, randint(1, 3))
                enemy_group.add(enemy6)
            for asteroi in ship_collide2:
                asteroi.kill()
                asteroid3 = Enemy('asteroid.png', randint(10, 490), 0, 80, 50, 1)
                asteroids.add(asteroid3)



        if win >= 10:
            window.blit(txt_winner, (300, 10))
            finish = True 
            window.blit(txt_reset, (0, 450))
        
        if lost >= 3:
            window.blit(txt_loser, (300, 10))
            finish = True 
            window.blit(txt_reset, (0, 450))

        if lives < 1:
            window.blit(txt_loser, (300, 10))
            finish = True 
            window.blit(txt_reset, (0, 450))


    

    display.update()
    clock.tick(FPS)