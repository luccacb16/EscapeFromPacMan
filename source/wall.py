import pygame

class Wall:
    def __init__(self, size_x, size_y, pos_x, pos_y):
        self.wall_surface = pygame.Surface((size_x, size_y))
        self.wall_rectangle = self.wall_surface.get_rect(bottomleft = (pos_x, pos_y))