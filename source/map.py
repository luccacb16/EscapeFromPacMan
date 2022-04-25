import pygame
from player import *
from enemy import *
from wall import *
from gamestate import *

class Map:
    def __init__(self):
        self.map_surface = pygame.image.load('textures/screens/mapa.png').convert()
    
    def create_walls(self):
        self.wall1 = Wall(141,9,217,371)
        self.wall2 = Wall(9,86,217,371)
        self.wall3 = Wall(49,9,217,283)
        self.wall4 = Wall(49,9,310,292)
        self.wall5 = Wall(9,86,350,371)
        self.wall6 = Wall(1,679,10,690)
        self.wall7 = Wall(1,679,566,690)
        self.wall8 = Wall(556,1,10,690)
        self.wall9 = Wall(556,1,10,12)
        self.wall10 = Wall(20,87,278,99)
        self.wall11 = Wall(60,42,52,100)
        self.wall12 = Wall(79,41,155,99)
        self.wall13 = Wall(79,41,340,99)
        self.wall14 = Wall(60,42,464,99)
        self.wall15 = Wall(58,19,53,167)
        self.wall16 = Wall(58,19,464,167)
        self.wall17 = Wall(101,87,10,303)
        self.wall18 = Wall(101,87,10,438)
        self.wall19 = Wall(101,87,464,303)
        self.wall20 = Wall(101,87,464,438)
        self.wall21 = Wall(39,22,10,574)
        self.wall22 = Wall(40,22,525,574)
        self.wall23 = Wall(79,21,155,507)
        self.wall24 = Wall(79,21,340,507)
        self.wall25 = Wall(20,87,154,438)
        self.wall26 = Wall(20,87,401,438)
        self.wall27 = Wall(20,156,154,303)
        self.wall28 = Wall(20,156,401,303)
        self.wall29 = Wall(59,19,176,235)
        self.wall30 = Wall(59,19,340,235)
        self.wall31 = Wall(140,20,217,168)
        self.wall32 = Wall(140,20,217,439)
        self.wall33 = Wall(140,20,217,574)
        self.wall34 = Wall(21,65,278,235)
        self.wall35 = Wall(21,65,277,506)
        self.wall36 = Wall(21,65,277,642)
        self.wall37 = Wall(60,21,52,507)
        self.wall38 = Wall(60,21,462,507)
        self.wall39 = Wall(19,88,93,574)
        self.wall40 = Wall(19,88,463,574)
        self.wall41 = Wall(183,20,52,642)
        self.wall42 = Wall(183,20,339,642)
        self.wall43 = Wall(19,67,155,621)
        self.wall44 = Wall(19,67,401,621)
        self.wall45 = Wall(116,46,232,282)
        self.wall46 = Wall(119,63,228,358)

    def colisao_parede(self, wallx, fantasma, pacman, tecla):
        if fantasma.player_rectangle.colliderect(wallx):
            if tecla[pygame.K_w]:
                fantasma.player_y += vel_player
            if tecla[pygame.K_s]:
                fantasma.player_y -= vel_player
            if tecla[pygame.K_a]:
                fantasma.player_x += vel_player
            if tecla[pygame.K_d]:
                fantasma.player_x -= vel_player
        if pacman.enemy_rectangle.colliderect(wallx): 
            if tecla[pygame.K_UP]:
                pacman.enemy_y += vel_enemy
            if tecla[pygame.K_DOWN]:
                pacman.enemy_y -= vel_enemy
            if tecla[pygame.K_LEFT]:
                pacman.enemy_x += vel_enemy
            if tecla[pygame.K_RIGHT]:
                pacman.enemy_x -= vel_enemy
    
    def colisao_pacman(self, wallx, pacman, tecla):
        if pacman.enemy_rectangle.colliderect(wallx): 
            pacman.enemy_x = 288
            pacman.enemy_y = 127

    def colisao_update(self, fantasma, pacman, tecla, gamestate):
        self.colisao_parede(self.wall1.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall2.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall3.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall4.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall5.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall6.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall7.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall8.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall9.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall10.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall11.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall12.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall13.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall14.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall15.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall16.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall17.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall18.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall19.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall20.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall21.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall22.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall23.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall24.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall25.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall26.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall27.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall28.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall29.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall30.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall31.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall32.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall33.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall34.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall35.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall36.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall37.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall38.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall39.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall40.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall41.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall42.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall43.wall_rectangle, fantasma, pacman, tecla)
        self.colisao_parede(self.wall44.wall_rectangle, fantasma, pacman, tecla)
        if gamestate.portal:
            self.colisao_pacman(self.wall45.wall_rectangle, pacman, tecla)
            self.colisao_pacman(self.wall46.wall_rectangle, pacman, tecla)