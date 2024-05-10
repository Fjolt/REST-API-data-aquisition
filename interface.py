import pygame
from typing import Dict, List

# Button class
class Button:
    def __init__(self, text, position):
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.color = (0, 255, 0)
        self.hover_color = (0, 200, 0)
        self.position = position
        self.width, self.height = 400, 50
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.is_hovered = False

    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
