# src/entities/enemy.py
import pygame
import random
from src.constants import ENEMY, SCREEN, COLORS

class Enemy(pygame.sprite.Sprite):   
    
    def __init__(self):
        super().__init__() 
        self.speed = ENEMY["SPEED"]

        
        self.image = pygame.Surface((ENEMY["WIDTH"], ENEMY["HEIGHT"]))
        self.image.fill(COLORS["RED"])
        self.rect = self.image.get_rect(
            midleft=(SCREEN["WIDTH"], random.randint(0, SCREEN["HEIGHT"]))
        )

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0: 
            self.kill()
