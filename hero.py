import pygame

class Hero:
    def __init__(self, screen):
        '''Инициализация героя - космического корабля'''
        self.image = pygame.load()
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()