import pygame, controls
from hero import Hero
from enemy import Enemy
from pygame.sprite import Group
import os

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((1200, 1000))
    pygame.display.set_caption("Самая лучшая игра")

    #объекты классов
    hero = Hero(screen)
    bullets = Group()
    enemys = Group()
    flag = True
    while flag:
        
        controls.events(screen, hero, bullets)
        screen.blit(pygame.image.load(os.path.join('image/background.png')), (-100,-100))
        # pygame.display.flip()
        hero.moving_hero(screen)
        controls.update(screen, hero, bullets, enemys)
        controls.moving_bullets(screen, bullets)
        controls.create_army(screen)
start_game()