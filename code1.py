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

# ПАРАМЕТРЫ ИГРОВОГО БЛОКА
plblock_w = 120
plblock_h = 20
plblock = pygame.Rect(screen_w // 2 - plblock_w // 2, screen_h - plblock_h - 60, plblock_w, plblock_h)
plblock_speed = 6

#ЗАДАЕМ МОМЕНТ ВЫКЛЮЧЕНИЯ ПРОГРАМЫ
while True:
    for e1 in pygame.event.get():
        if e1.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #ЗАДАЕМ ДВИЖЕНИЕ ИГРОВОГО БЛОКА
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and plblock.x > 0:
        plblock.centerx -= plblock_speed
    if key[pygame.K_RIGHT] and plblock.x < screen_w - plblock_w:
        plblock.centerx += plblock_speed


    screen.fill((199, 21, 133))
    pygame.draw.rect(screen, (0, 139, 139), plblock)
    pygame.display.flip()

    clock.tick(60)
