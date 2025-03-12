import pygame
from src.constants import BULLET, SCREEN, COLORS

class Bullet(pygame.sprite.Sprite):  # Herdar de Sprite!
    def __init__(self, x, y):
        super().__init__()  # Inicialização obrigatória
        self.speed = BULLET["SPEED"]

        # Configurar imagem e rect (obrigatório)
        self.image = pygame.Surface((BULLET["WIDTH"], BULLET["HEIGHT"]))
        self.image.fill(COLORS["RED"])
        self.rect = self.image.get_rect(center=(x, y))  # Posiciona no centro

    def update(self):
        self.rect.x += self.speed

        # Remove o projétil quando sair da tela
        if self.rect.left > SCREEN["WIDTH"]:  # Adicione SCREEN às importações
            self.kill()
