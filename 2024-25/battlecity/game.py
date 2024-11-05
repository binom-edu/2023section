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
        self.last_update_c = self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
        self.speed = 1
        self.direction = 0
        self.block_move = False
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
            self.last_update_c = now

        if now - self.last_update > self.frame_rate:    
            self.img_num = (self.img_num + 1) % len(self.imgs)
            self.image = pygame.transform.rotate(self.imgs[self.img_num], self.direction * 90)
            self.last_update = now

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


def readcfg():
    '''Чтение настроек'''
    with open('settings.cfg') as fin:
        ans = dict()
        for line in fin:
            key, value = line.split()
            ans[key] = int(value)
    return ans

cfg = readcfg()
img_dir = os.path.join(os.path.dirname(__file__), 'img')

pygame.init()
screen = pygame.display.set_mode((cfg['WIDTH'] * cfg['TILESIZE'], cfg['HEIGHT'] * cfg['TILESIZE']), 0, 32)
pygame.display.set_caption('Battle City 2D')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

player = Player((cfg['WIDTH'] // 2, cfg['HEIGHT'] // 2))

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
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()