import pygame
from src.constants import SCREEN, COLORS, ENEMY
from src.entities import *
from settings import FPS

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN["WIDTH"], SCREEN["HEIGHT"]))
        pygame.display.set_caption("PyZombie")
        self.clock = pygame.time.Clock()

        
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

      
        self.player = Player(100, 300)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.bullets = pygame.sprite.Group()



        self.spawn_timer = ENEMY["SPAWN_TIME"]
        
        pygame.time.set_timer(self.spawn_timer, 1000)

        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.fire_bullet()

            if event.type == self.spawn_timer:
                self.spawn_enemy()



    def fire_bullet(self):
        new_bullet = Bullet(self.player.rect.centerx, self.player.rect.centery)
        self.bullets.add(new_bullet)
        self.all_sprites.add(new_bullet)

    def spawn_enemy(self):
        new_enemy = Enemy()
        self.all_sprites.add(new_enemy)
        self.enemies.add(new_enemy)

    def update(self):
        self.all_sprites.update()
        pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

        if pygame.sprite.spritecollide(self.player, self.enemies, dokill=True):
            print("Game Over!")
            self.running = False

    def draw(self):
        self.screen.fill(COLORS["BLACK"])
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
