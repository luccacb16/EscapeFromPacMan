import pygame

from constantes import *

class Player:
    def __init__(self):
        super().__init__()
        self.player_x = 285
        self.player_y = 396

        self.sprites = []
        self.sprites.append(pygame.image.load("textures/player/Ghost1_350.PNG"))
        self.sprites.append(pygame.image.load("textures/player/Ghost2_350.PNG"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.player_surface = self.image
        self.player_surface = pygame.transform.scale(self.player_surface, (player_width, player_height))
        self.player_rectangle = self.player_surface.get_rect(center = (self.player_x, self.player_y))

    def update(self):
        self.player_rectangle = self.player_surface.get_rect(center = (self.player_x, self.player_y))
        self.current_sprite += 0.1  # Velocidade da animação (em frames)

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
        self.player_surface = self.image    
        self.player_surface = pygame.transform.scale(self.player_surface, (player_width, player_height))

    def origem(self):
        self.player_x = 285
        self.player_y = 396
   
    def movimento(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_w]:
            self.player_y -= vel_player
        if tecla[pygame.K_s]:
            self.player_y += vel_player
        if tecla[pygame.K_a]:
            self.player_x -= vel_player
        if tecla[pygame.K_d]:
            self.player_x += vel_player