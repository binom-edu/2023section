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
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
        all_sprites.add(self)
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.img_num = (self.img_num + 1) % len(self.imgs)
            self.image = self.imgs[self.img_num]
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
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()