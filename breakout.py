import pygame
import os
import random


'''Игра Breakout'''


colors = {1: (255, 255, 0), 3: (154, 205, 50), 5: (000, 000, 255)}
pygame.init()
size = width, height = 590, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Brick(pygame.sprite.Sprite):
    def __init__(self, group, coords):
        super().__init__(all_sprites)
        self.strength = random.choice(list(colors.keys()))
        self.color = colors[self.strength]
        self.coords = coords
        self.x1 = coords[0]
        self.y1 = coords[1]
        self.x2 = self.x1 + 50
        self.y2 = self.y1 + 15
        self.add(group)
        #self.add(all_sprites)
        self.image = pygame.Surface((50, 15))
        self.image.fill(self.color)
        self.rect = pygame.Rect((self.x1, self.y1, self.x2, self.y2)) 
        
    #def update(self, demage):
        #self.strength -= demage
        #if self.strength <= 0:
            #brickes.remove(self)
        #else:
            #self.color = colors[self.strength]
            
        
class Board(pygame.sprite.Sprite):
    pass

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, demage):
        super().__init__(all_sprites)
        self.add(all_sprites)
        self.radius = radius
        self.demage = demage
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)
        
    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        #if pygame.sprite.spritecollideany(self, horizontal_borders):
            #self.vy = -self.vy
        #if pygame.sprite.spritecollideany(self, vertical_borders):
            #self.vx = -self.vx
        if pygame.sprite.spritecollideany(self, brickes):
                self.vx = -self.vx 
                self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, paddle_group):
                self.vx = -self.vx 
                self.vy = -self.vy        


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.add(all_sprites)
        self.add(paddle_group)
        self.image = pygame.Surface((100, 20))
        self.image.fill((210, 180, 140)) 
        self.rect = pygame.Rect((245, 570, 345, 590))
        
    def move_right(self):
        if self.rect.topleft[0] + 100 < width:
            self.rect.topright = (self.rect.topright[0] + 5, self.rect.topright[1])
                  
    def move_left(self):
        if self.rect.topleft[0] > 0:
            self.rect.topright = (self.rect.topright[0] - 5, self.rect.topright[1])
        

all_sprites = pygame.sprite.Group()
brickes = pygame.sprite.Group()
paddle_group = pygame.sprite.Group()
brickes.add(all_sprites)
for i in range(0, 594, 54):
    for j in range(0, 200, 25):
        Brick(brickes, (i, j))
paddle = Paddle()

main_ball = Ball(400, 400, 10, 1)
all_sprites.draw(screen)
#brickes.draw(screen)
pygame.display.update()
#clock = pygame.time.Clock()

p_moving_r = False
p_moving_l = False
    

running = True
while running:
    screen.fill((255, 255, 225))
    all_sprites.draw(screen)
    pygame.display.update()    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p_moving_l = True
            if event.key == pygame.K_RIGHT:
                p_moving_r = True
        else:
            p_moving_l = False
            p_moving_r = False
                
    if p_moving_r:
        paddle.move_right()
    if p_moving_l:
        paddle.move_left()
        
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()    
    clock.tick(60)