import pygame
from src.constants import PLAYER, SCREEN, COLORS

class Player(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        super().__init__()  
        self.speed = PLAYER["SPEED"]

        self.image = pygame.Surface((PLAYER["WIDTH"], PLAYER["HEIGHT"]))
        self.image.fill(COLORS["WHITE"])
        self.rect = self.image.get_rect(topleft=(x, y))  

    def update(self):  
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN["WIDTH"], SCREEN["HEIGHT"]))
