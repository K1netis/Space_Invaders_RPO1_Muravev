import pygame
import sys
from bullet import Bullet


def events(screen, hero, bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    hero.move_right = True
                if event.key == pygame.K_a:
                    hero.move_left = True
                if event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, hero)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    hero.move_right = False
                if event.key == pygame.K_a:
                    hero.move_left = False
def update(screen, hero, bullets, enemy):
    screen.fill(0)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    enemy.output_enemy()
    hero.output_hero()
    pygame.display.flip()

def moving_bullets(screen, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)