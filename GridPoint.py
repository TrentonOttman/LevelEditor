import pygame

class GridPoint:
    def __init__(self, left_x, top_y, grid_size):
        self.rect = pygame.Rect(left_x, top_y, grid_size, grid_size)
        self.type = None
        self.occupied = False

    def set_type(self, type):
        pass

    def clear(self):
        pass

    def draw(self, screen):
        pass