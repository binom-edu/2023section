import pygame

class Pers(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((20, 20))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        all_sprites.add(self)

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.rect.y -= 5
            if self.rect.top <= 0:
                self.rect.top += 20
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 5
        # self.rect.y += 5
        # if self.rect.top >= HEIGHT:
        #     self.rect.bottom = 0


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
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    
    pygame.display.flip()

pygame.quit()