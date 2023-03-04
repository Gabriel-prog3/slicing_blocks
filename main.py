import pygame as pg
import random


pg.font.init()
FPS = 60
WIDTH, HEIGHT = 400, 300
WIN = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


def draw_update():
    clock.tick(FPS)
    pg.display.flip()
    WIN.fill((0, 0, 0))


FIRST_SIZE = 300
HEIGHT_BLOCK = 20
VELOCITY = 4
velocity = VELOCITY
score = 1
previus_size = FIRST_SIZE
game_over = False

blocks = [pg.Rect(0, HEIGHT - HEIGHT_BLOCK, FIRST_SIZE, HEIGHT_BLOCK)]


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
        if not game_over:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if score > 1:
                        previus_size += -abs(blocks[-2].x - blocks[-1].x)
                        if blocks[-1].x < blocks[-2].x:
                            blocks[-1].x = blocks[-2].x

                    blocks[-1].w = previus_size
                    first_position = random.choice((0, WIDTH - previus_size))
                    velocity = -VELOCITY if first_position else VELOCITY
                    blocks.append(
                        pg.Rect(
                            first_position,
                            HEIGHT - (score + 1) * HEIGHT_BLOCK,
                            previus_size,
                            HEIGHT_BLOCK,
                        )
                    )
                    if blocks[-1].w > 0:
                        score += 1

    game_over = blocks[-1].y <= 2 * HEIGHT_BLOCK or blocks[-1].w <= 0
    font = pg.font.SysFont(None, 44)
    if game_over:
        img = font.render("game over, score: " + str(score - 1), True, (255, 255, 255))
        WIN.blit(img, (20, 20))
        blocks[-1].w = 0

    else:
        img = font.render("score: " + str(score - 1), True, (255, 255, 255))
        WIN.blit(img, (20, 20))
        blocks[-1].x += velocity

    if blocks[-1].x > WIDTH - previus_size or blocks[-1].x < 0:
        velocity = -velocity

    for block in blocks:
        pg.draw.rect(WIN, (255, 255, 255), block)

    draw_update()
