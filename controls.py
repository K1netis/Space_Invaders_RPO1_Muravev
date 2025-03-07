import pygame
import sys
from bullet import Bullet
from enemy import Enemy
import time

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

def update(screen, hero, enemys, bullets, background):
    screen.fill(0)
    screen.blit(background, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    hero.output_hero()
    enemys.draw(screen)
    pygame.display.flip()


def update_bullets(screen, bullets, enemys):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)
    if len(enemys) == 0:
        bullets.empty()
        create_army(screen, enemys)

def update_enemys(screen, stats, enemys, bullets, hero):
    enemys.update()
    if pygame.sprite.spritecollideany(hero, enemys):
        hero_kill(screen, stats, enemys, bullets, hero)
        enemys_check(screen, stats, enemys, bullets, hero)

def create_army(screen, enemys):
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((1200 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((1000 - 400 - 2 * enemy_height) / enemy_height)
    for row_num in range(number_enemy_y):
        for enemy_num in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + enemy_width * enemy_num
            enemy.y = enemy_height + enemy_height * row_num
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.y
            enemys.add(enemy)

def hero_kill(screen, stats, enemys, bullets, hero):
    if stats.hero_hp > 0:
        stats.hero_hp -= 1
        enemys.empty()
        bullets.empty()
        create_army(screen, enemys)
        hero.create_hero_again()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def enemys_check(screen, stats, enemys, bullets, hero):
    screen_rect = screen.get_rect()
    for enemy in enemys.sprites():
        if enemy.rect.bottom > screen.rect.bottom:
            hero_kill(screen, stats, enemys, bullets, hero)
            break