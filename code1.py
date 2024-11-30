import random
import pygame
import sys

pygame.init()

# ПАРАМЕТРЫ ЭКРАНА
screen_w = 600
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Arcanoid')

clock = pygame.time.Clock()
# image = pygame.image.load("image1.jpg")
# image = pygame.transform.scale(image, (screen_w, screen_h))

# ПАРАМЕТРЫ ИГРОВОГО БЛОКА
plblock_w = 150
plblock_h = 30
plblock = pygame.Rect(screen_w // 2 - plblock_w // 2, screen_h - plblock_h - 60, plblock_w, plblock_h)
plblock_speed = 8

# ПАРАМЕТРЫ МЯЧИКА
ball_r = 40
ball = pygame.Rect(screen_w // 2 - ball_r // 2, screen_h - ball_r - plblock_h - 60, ball_r, ball_r)
ball_speed = 4
dir_st = 1  # НАПРАВЛЕНИЕ ДВИЖЕНИЯ
dir_op = -1  # ИЗМЕНЕНИЕ НАПРАВЛЕНИЯ ДВИЖЕНИЯ

# ЗАДАЕМ МОМЕНТ ВЫКЛЮЧЕНИЯ ПРОГРАМЫ
while True:
    for e1 in pygame.event.get():
        if e1.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ЗАДАЕМ ДВИЖЕНИЕ ИГРОВОГО БЛОКА
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and plblock.x > 0:
        plblock.centerx -= plblock_speed
    if key[pygame.K_RIGHT] and plblock.x < screen_w - plblock_w:
        plblock.centerx += plblock_speed

    # ЗАДАЕМ ДВИЖЕНИЕ ШАРИКА
    ball.x += ball_speed * dir_st
    ball.y += ball_speed * dir_op
    if screen_w - ball_r < ball.x:
        dir_st = - dir_st
    if screen_h - ball_r < ball.y:
        dir_op = - dir_op

    # ОПРЕДЕЛЯЕМ СТОЛКНОВЕНИЕ С ПЛАТФОРМОЙ
    if ball.colliderect(plblock) and dir_op > 0:
        dir_op = - dir_op

    # screen.blit(image, (0,0))
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (139, 0, 0), plblock)
    pygame.draw.rect(screen, (178, 34, 34), ball)
    pygame.display.flip()

    clock.tick(60)
