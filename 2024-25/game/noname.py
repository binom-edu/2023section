import pygame

class Pers(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((20, 20))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        all_sprites.add(self)


FPS = 30
WIDTH = 400
HEIGHT = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Без имени 1')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

pers = Pers()


gameOn = True
while gameOn:
    clock.tick(FPS)
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    # обновление
    all_sprites.update()
    # рендеринг
    all_sprites.draw(screen)
    
    pygame.display.flip()

pygame.quit()