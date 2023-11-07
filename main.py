import pygame, controls
from hero import Hero
from enemy import Enemy
from pygame.sprite import Group

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((1200, 1000))
    pygame.display.set_caption("Самая лучшая игра")

    #объекты классов
    hero = Hero(screen)
    enemy = Enemy(screen)
    bullets = Group()
    
    flag = True
    while flag:
        
        controls.events(screen, hero, bullets)

        # pygame.display.flip()
        hero.moving_hero(screen)
        controls.update(screen, hero, bullets, enemy)
        controls.moving_bullets(screen, bullets)
start_game()