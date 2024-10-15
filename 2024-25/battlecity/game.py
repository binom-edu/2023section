import pygame, random

class Tank(pygame.sprite.Sprite):
    def __init__(self, coords: tuple, type: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((cfg['TILESIZE'] * 2, cfg['TILESIZE'] * 2))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.x, self.y = coords
        self.rect.topleft = (self.x * cfg['TILESIZE'], self.y * cfg['TILESIZE'])
        all_sprites.add(self)

class Player(Tank):
    def __init__(self, coords: tuple):
        Tank.__init__(self, coords, 0)


def readcfg():
    '''Чтение настроек'''
    with open('settings.cfg') as fin:
        ans = dict()
        for line in fin:
            key, value = line.split()
            ans[key] = int(value)
    return ans

cfg = readcfg()

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
    # рендеринг
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()