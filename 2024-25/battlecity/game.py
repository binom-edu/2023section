import pygame, random, os

class Tank(pygame.sprite.Sprite):
    def __init__(self, coords: tuple, type: int):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = []
        self.image = pygame.surface.Surface((cfg['TILESIZE'] * 2, cfg['TILESIZE'] * 2))
        self.image.fill((0, 255, 0))
        self.imgs.append(self.image)
        self.rect = self.image.get_rect()
        self.x, self.y = coords
        self.rect.topleft = (self.x * cfg['TILESIZE'], self.y * cfg['TILESIZE'])
        now = pygame.time.get_ticks()
        self.last_update_c = self.last_update = now
        self.frame_rate = 100
        self.speed = 1
        self.direction = 0
        self.block_move = False
        self.bullets = 1
        self.maxbullets = 1
        self.shoot_delay = 500
        self.last_shoot = now
        all_sprites.add(self)
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update_c > self.speed:
            self.block_move = True
            if self.rect.top > self.y * cfg['TILESIZE']:
                self.rect.top -= 1
            elif self.rect.top < self.y * cfg['TILESIZE']:
                self.rect.top += 1
            elif self.rect.left < self.x * cfg['TILESIZE']:
                self.rect.left += 1
            elif self.rect.left > self.x * cfg['TILESIZE']:
                self.rect.left -= 1
            else:
                self.block_move = False
            for tile in pygame.sprite.spritecollide(self, tiles_fg, False):
                if tile.type == 'g':
                    continue
                if self.direction == 0:
                    self.rect.top = tile.rect.bottom
                elif self.direction == 1:
                    self.rect.left = tile.rect.right
                elif self.direction == 2:
                    self.rect.bottom = tile.rect.top
                else:
                    self.rect.right = tile.rect.left
                self.x = self.rect.left // cfg['TILESIZE']
                self.y = self.rect.top // cfg['TILESIZE']
            self.last_update_c = now

        if now - self.last_update > self.frame_rate:    
            self.img_num = (self.img_num + 1) % len(self.imgs)
            self.image = pygame.transform.rotate(self.imgs[self.img_num], self.direction * 90)
            self.last_update = now

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot >= self.shoot_delay and self.bullets > 0:
            Bullet(self, )
            self.bullets -= 1
            self.last_shoot = now

class Player(Tank):
    def __init__(self, coords: tuple):
        Tank.__init__(self, coords, 0)
        self.imgs = []
        for filename in os.listdir(os.path.join(img_dir, 'whitetank')):
            img = pygame.image.load(os.path.join(img_dir, 'whitetank', filename))
            self.imgs.append(pygame.transform.scale(img, (cfg['TILESIZE'] * 2, cfg['TILESIZE'] * 2)))
        self.image = self.imgs[0]
        self.img_num = 0

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.shoot()
        if not self.block_move:
            if keystate[pygame.K_UP]:
                self.direction = 0
                self.y = max(self.y - 1, 0)
            elif keystate[pygame.K_LEFT]:
                self.direction = 1
                self.x = max(self.x - 1, 0)
            elif keystate[pygame.K_DOWN]:
                self.direction = 2
                self.y = min(self.y + 1, cfg['HEIGHT'] - 2)
            elif keystate[pygame.K_RIGHT]:
                self.direction = 3
                self.x = min(self.x + 1, cfg['WIDTH'] - 2)
        Tank.update(self)

class Tile(pygame.sprite.Sprite):
    def __init__(self, coords: tuple, type: str):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.power = 1
        self.destroyable = True
        if type == 'x':
            self.image = pygame.surface.Surface((cfg['TILESIZE'], cfg['TILESIZE']))
            self.image.fill((200, 40, 40))
            tiles_fg.add(self)
        elif type == 'b':
            self.image = pygame.surface.Surface((cfg['TILESIZE'], cfg['TILESIZE']))
            self.image.fill((200, 200, 200))
            self.power = 2
            tiles_fg.add(self)
        elif type == 'g':
            self.image = pygame.surface.Surface((cfg['TILESIZE'], cfg['TILESIZE']))
            self.image.fill((10, 200, 10))
            self.destroyable = False
            tiles_fg.add(self)
        self.rect = self.image.get_rect()
        x, y = coords
        self.rect.topleft = (x * cfg['TILESIZE'], y * cfg['TILESIZE'])

class Bullet(pygame.sprite.Sprite):
    def __init__(self, owner, speed=5, power=1):
        pygame.sprite.Sprite.__init__(self)
        self.owner = owner
        self.speed = speed
        if owner.direction == 0:
            self.speedx, self.speedy = 0, -speed
        elif owner.direction == 1:
            self.speedx, self.speedy = -speed, 0
        elif owner.direction == 2:
            self.speedx, self.speedy = 0, speed
        else:
            self.speedx, self.speedy = speed, 0
        self.power = power
        self.image = pygame.surface.Surface((6, 6))
        self.rect = pygame.draw.circle(self.image, (255, 255, 255), (3, 3), 3)
        self.rect.center = owner.rect.center
        all_sprites.add(self)
        bullets.add(self)
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if not (0 <= self.rect.x < cfg['WIDTH'] * cfg['TILESIZE'] and 0 <= self.rect.y <= cfg['HEIGHT'] * cfg['TILESIZE']):
            self.owner.bullets = min(self.owner.bullets + 1, self.owner.maxbullets)
            self.kill()
            # del self
        for tile in pygame.sprite.spritecollide(self, tiles_fg, False):
            if tile.destroyable:
                if self.power >= tile.power:
                    tile.kill()
                self.owner.bullets = min(self.owner.bullets + 1, self.owner.maxbullets)
                self.kill()
                # del self



def readcfg():
    '''Чтение настроек'''
    with open('settings.cfg') as fin:
        ans = dict()
        for line in fin:
            key, value = line.split()
            ans[key] = int(value)
    return ans

def loadlevel(n):
    '''Загружаем уровень по номеру'''
    tiles_bg.empty()
    tiles_fg.empty()
    lvl_dir = os.path.join(os.path.dirname(__file__), 'levels')
    filename = os.path.join(lvl_dir, str(n) + '.lvl')
    with open(filename) as fin:
        try:
            for y in range(cfg['HEIGHT']):
                line = fin.readline()
                for x in range(cfg['WIDTH']):
                    if line[x] != ' ':
                        tile = Tile((x, y), line[x])
        except:
            print('Ошибка чтения уровня')
            pygame.quit()

cfg = readcfg()
img_dir = os.path.join(os.path.dirname(__file__), 'img')

pygame.init()
screen = pygame.display.set_mode((cfg['WIDTH'] * cfg['TILESIZE'], cfg['HEIGHT'] * cfg['TILESIZE']), 0, 32)
pygame.display.set_caption('Battle City 2D')
clock = pygame.time.Clock()

tiles_bg = pygame.sprite.Group()
tiles_fg = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player((cfg['WIDTH'] // 2, cfg['HEIGHT'] // 2))
level = 0
loadlevel(level)

gameOn = True
while gameOn:
    clock.tick(cfg['FPS'])
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    # обновления
    all_sprites.update()
    # рендеринг
    screen.fill((0, 0, 0))
    tiles_bg.draw(screen)
    all_sprites.draw(screen)
    tiles_fg.draw(screen)

    pygame.display.flip()

pygame.quit()