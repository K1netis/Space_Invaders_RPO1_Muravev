import pygame
import sys
from hero import Hero

def start_game():
    '''Основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("Самая лучшая игра")

    hero = Hero(screen)

    flag = True
    move_left = False
    move_right = False
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    move_right = True
                if event.key == pygame.K_a:
                    move_left = True
            if event.type == pygame.KEYUP:
                move_right = False
                move_left = False
        
        if move_right == True and hero.rect.right < 1200:
            hero.rect.centerx += 1
        if move_left == True and hero.rect.left > 0:
            hero.rect.centerx -= 1
        pygame.display.flip()
        screen.fill(0)
        hero.output_hero()

start_game()