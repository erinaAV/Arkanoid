import pygame
import sys
import random


'''Игра Breakout
ПРАВИЛА:
  -для победы необходимо разбить все кирпичи
  -кирпичи обладают разной прочностью (в зависимости от цвета)
  -отбивайте шарик ракеткой
  -управление клавишами навигации
  -вы проиграли, если шарик упал вниз за пределы поля
  '''


colors = {1: (255, 255, 0), 2: (154, 205, 50), 3: (000, 000, 255)}
pygame.init()
size = width, height = 590, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
im_sprite = pygame.sprite.Group()

# фоновая музыка
pygame.mixer.music.load('m1.mp3')
pygame.mixer.music.play(-1, 0.0)


# выход из игры
def terminate():
    pygame.quit()
    sys.exit()
    
    
# загрузка изображений 
def load_image(name, colorkey=None):
    print(name)
    try:
        image = pygame.image.load(name)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

    
# заставка
def screen_saver():
    global all_sprites, im_sprite
    
    text = ['B', 'R', 'E', 'A', 'K', 'O', 'U', 'T'] 
    screen.fill((0, 0, 250))
    
    background_im = load_image('sky.jpg')
    background = pygame.sprite.Sprite(im_sprite)
    background.image = background_im
    background.rect = background.image.get_rect()
    background.rect.topleft = (0, -600)
    bg_move = True
    
    font = pygame.font.Font(None, 30)
    i = 0
    p = 30
    ct = 20
    text_coord = 20
    pygame.display.update()    
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                
        # выезжающий фон
        if background.rect.topleft == (0, 0):
            start_game()
        if bg_move:
            background.rect.move_ip(0, 10)
        clock.tick(ct)
        im_sprite.draw(screen)
        pygame.display.update()
    background.kill()
    start_game()    
    
    
# проверка и экран при победе
def win():
    f = False
    for i in brickes:
        f = True
    if not f:
        text = ['ПОБЕДА! :)', '', 'Нажмите пробел, если хотите',
                'начать заново']
        
        screen.fill((255, 250, 250))
        font = pygame.font.Font(None, 30)
        text_coord = 150   
        for line in text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
            pygame.display.update() 
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:            
                        game()
                        return                
        
   
# процесс игры 
def game():
    global all_sprites, brickes, paddle_group, paddle, main_ball, balls
    
    all_sprites = pygame.sprite.Group()
    brickes = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    
    brickes.add(all_sprites)
    
    # создаем и рисуем спрайты
    for i in range(0, 594, 54):
        for j in range(0, 250, 25):
            Brick(brickes, (i, j))
    paddle = Paddle()
    
    main_ball = Ball(295, 500, 10, 1)
    all_sprites.draw(screen)
    brickes.draw(screen)
    pygame.display.update()
    
    p_moving_r = False
    p_moving_l = False
    
    running = True
    while True:
        screen.fill((255, 250, 250))
        all_sprites.draw(screen)
        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
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
        win() 
        clock.tick(60)
    

# экран начала игры 
def start_game():
    text = ['ПРАВИЛА ИГРЫ:', 'Для победы необходимо разбить стену,',
            'состоящую из блоков,', 'отражая ракеткой шарик.',
            'Вы проиграли, если шарик улетел вниз.', ' ',
            'Нажмите пробел, чтобы начать игру.']
    
    screen.fill((255, 250, 250))
    font = pygame.font.Font(None, 30)
    text_coord = 150   
    for line in text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        pygame.display.update() 
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:            
                    game()
                    return
            

# экран при проигрыше         
def losing():
    text = ['ВЫ ПРОИГРАЛИ :c', '', 'Нажмите пробел, если хотите',
            'начать заново']
    
    screen.fill((255, 250, 250))
    font = pygame.font.Font(None, 30)
    text_coord = 150   
    for line in text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        pygame.display.update() 
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:            
                    game()
                    return            
            

# кирпичики
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
        self.add(all_sprites)
        self.image = pygame.Surface((50, 15))
        self.image.fill(self.color)
        self.rect = pygame.Rect(self.x1, self.y1, 50, 15) 
        
    def update(self):
        if pygame.sprite.spritecollideany(self, balls):
            self.strength -= 1           
        if self.strength <= 0:
            brickes.remove(self)
            self.image.fill((255, 250, 250))
        else:
            self.color = colors[self.strength]
            self.image.fill(self.color)
            

# шарик
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, demage):
        super().__init__(all_sprites)     
        self.add(all_sprites)
        self.add(balls)
        self.radius = radius
        self.demage = demage
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.x = self.rect.topright[0]
        self.y = self.rect.topright[1]          
        self.vx = 1
        self.vy = 3
        
    def update(self):          
        self.rect = self.rect.move(self.vx, self.vy)
        self.x = self.rect.topright[0]
        self.y = self.rect.topright[1]        
            
        # столкновение с кирпичиками
        if pygame.sprite.spritecollideany(self, brickes):
            self.vx = self.vx 
            self.vy = -self.vy
            
        # столкновение с доской
        if pygame.sprite.spritecollideany(self, paddle_group):
            self.vx = self.vx 
            self.vy = -self.vy
            
        # столкновение с границами игрового поля
        if self.y > height:
            losing()        
        if not (self.radius <= self.x <= width):
            self.vx = -self.vx
        if self.y <= 0:
            self.vy = -self.vy


# ракетка
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.add(all_sprites)
        self.add(paddle_group)
        self.image = pygame.Surface((100, 20))
        self.image.fill((210, 180, 140)) 
        self.rect = pygame.Rect((245, 570, 100, 20))
        
    def move_right(self):
        if self.rect.topleft[0] + 100 < width:
            self.rect.move_ip(5, 0)
                  
    def move_left(self):
        if self.rect.topleft[0] > 0:
            self.rect.move_ip(-5, 0)
    
    
screen_saver()
