import pygame
from constantes import *

class Enemy:
    def __init__(self):
        super().__init__()
        self.enemy_x = 288
        self.enemy_y = 260

        self.sprites = []
        self.is_animating = False
        self.is_animating_left = False
        self.is_animating_right = False
        self.is_animating_up = False
        self.is_animating_down = False
        self.sprites.append(pygame.image.load("textures/pacman/PacMan1Left_350.PNG"))
        self.sprites.append(pygame.image.load("textures/pacman/PacMan2Left_350.PNG"))
        self.sprites.append(pygame.image.load("textures/pacman/PacMan3Left_350.PNG"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.enemy_surface = self.image
        self.enemy_surface = pygame.transform.scale(self.enemy_surface, (enemy_width, enemy_height))
        self.enemy_rectangle = self.enemy_surface.get_rect(center = (self.enemy_x, self.enemy_y))

    def update(self):
        self.enemy_rectangle = self.enemy_surface.get_rect(center = (self.enemy_x, self.enemy_y))

        if self.is_animating == True: 
            self.current_sprite += 0.1  # Velocidade da animação (em frames)  

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        if self.is_animating_left == True:
            self.image = self.sprites[int(self.current_sprite)] 

        if self.is_animating_right == True:
            self.image = pygame.transform.flip(self.sprites[int(self.current_sprite)], True, False)

        if self.is_animating_up == True:
            self.image = pygame.transform.rotate(self.sprites[int(self.current_sprite)], 270)    

        if self.is_animating_down == True:
            self.image = pygame.transform.rotate(self.sprites[int(self.current_sprite)], 90)

        self.enemy_surface = self.image
        self.enemy_surface = pygame.transform.scale(self.enemy_surface, (enemy_width, enemy_height))

    def animate(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_LEFT]:
            self.is_animating = True
            self.is_animating_left = True
            self.is_animating_right = False
            self.is_animating_up = False
            self.is_animating_down = False

        if tecla[pygame.K_RIGHT]:  
            self.is_animating = True 
            self.is_animating_right = True 
            self.is_animating_left = False
            self.is_animating_up = False
            self.is_animating_down = False

        if tecla[pygame.K_UP]:
            self.is_animating = True
            self.is_animating_up = True
            self.is_animating_left = False
            self.is_animating_right = False
            self.is_animating_down = False

        if tecla[pygame.K_DOWN]:
            self.is_animating = True
            self.is_animating_down = True
            self.is_animating_up = False
            self.is_animating_left = False
            self.is_animating_right = False 

    def origem(self):
        self.enemy_x = 288
        self.enemy_y = 260

    def movimento(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_UP]:
            self.enemy_y -= vel_enemy
        if tecla[pygame.K_DOWN]:
            self.enemy_y += vel_enemy
        if tecla[pygame.K_LEFT]:
            self.enemy_x -= vel_enemy
        if tecla[pygame.K_RIGHT]:
            self.enemy_x += vel_enemy