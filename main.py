import pygame

pygame.font.init()
FPS = 60
WIDTH, HEIGHT = 700, 584
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


clock = pygame.time.Clock()


def draw_update():
    clock.tick(FPS)
    pygame.display.flip()
    WIN.fill((0, 0, 0))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    draw_update()
