import pygame
from colors import *

class GridPoint:
    def __init__(self, left_x, top_y, grid_size):
        self.rect = pygame.Rect(left_x, top_y, grid_size, grid_size)
        self.type = None
        self.occupied = False

    def set_type(self, type):
        self.type = type
        self.occupied = True

    def clear(self):
        self.type = None
        self.occupied = False

    def draw(self, screen):
        if self.occupied:
            if self.type == "Wall":
                pygame.draw.rect(screen, WHITE, self.rect)
            elif self.type == "Spike":
                x, y, w, h = self.rect.x, self.rect.y, self.rect.width, self.rect.height
                points = [(x + w // 2, y), (x, y + h), (x + w, y + h)]
                pygame.draw.polygon(screen, GRAY, points)
            elif self.type == "Sand":
                pygame.draw.rect(screen, SAND, self.rect)
            elif self.type == "Trampoline":
                pygame.draw.rect(screen, PURPLE, self.rect)
            elif self.type == "Start":
                pygame.draw.rect(screen, GREEN, self.rect)
            elif self.type == "End":
                pygame.draw.rect(screen, RED, self.rect)
