import pygame, controls
from hero import Hero
from pygame.sprite import Group
from stats import Stats

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((1200 , 1000))
    background = pygame.image.load("image/background.png")
    pygame.display.set_caption("Самая лучшая игра")

    #объекты классов
    hero = Hero(screen)
    
    bullets = Group()
    enemys = Group()
    stats = Stats()
    controls.create_army(screen,enemys)
    
    flag = True
    while flag:
        controls.events(screen, hero, bullets)
        hero.moving_hero(screen)
        controls.update(screen, hero, enemys, bullets, background)
        controls.update_bullets(screen, bullets, enemys)
        controls.update_enemys(screen, stats, enemys, bullets, hero)
        
start_game()
