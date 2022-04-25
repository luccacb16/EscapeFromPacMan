import pygame
from player import *
from enemy import *
from map import *
from constantes import *
from chaves import *
from fechaduras import *
from tad import *
import os

class Gamestate:
    def __init__(self):
        self.game_active = False
        self.menu_surface = pygame.image.load('textures/screens/menu.png').convert()
        self.como_jogar_surface = pygame.image.load('textures/screens/tutorial.png').convert()
        self.creditar_surface = pygame.image.load('textures/screens/creditos.png').convert()
        self.game_over_surface = pygame.image.load('textures/screens/game_over.png').convert()
        self.game_won_surface = pygame.image.load('textures/screens/game_won.png').convert()
        self.MENU = 1
        self.TUTORIAL = 0
        self.CREDITOS = 0
        self.GAME_OVER = 0
        self.GAME_WON = 0
        self.portal = 0
        self.portal_vel = 1
        self.portal_width = 5 * self.portal_vel
        self.portal_height = 5 * self.portal_vel

        self.bg_music()

    # Menus
    def menu(self, screen, fantasma, pacman, chave, fechadura, pilha_chaves, pilha_fechaduras, randompos):
        screen.blit(self.menu_surface, (0,0))
        self.mouse_pos = pygame.mouse.get_pos()
        self.iniciar_surface = pygame.Surface((269, 95))
        self.iniciar_rectangle = self.iniciar_surface.get_rect(bottomleft = (215, 357))

        if(self.iniciar_rectangle.collidepoint(self.mouse_pos) and self.TUTORIAL == 0 and self.CREDITOS == 0):
            if(pygame.mouse.get_pressed()[0]):
                self.game_active = True
                fantasma.origem()
                fantasma.update()
                pacman.origem()
                pacman.update()
                
                chave.reset(randompos)
                fechadura.reset(randompos)
                pilha_chaves.reset()
                pilha_fechaduras.reset()

                self.portal = 0
                self.MENU = 0
                self.GAME_OVER = 0
                self.GAME_WON = 0

                self.bg_music()

        self.tutorial_surface = pygame.Surface((269, 95))
        self.tutorial_rectangle = self.tutorial_surface.get_rect(bottomleft = (215, 485))
        if(self.tutorial_rectangle.collidepoint(self.mouse_pos) and self.CREDITOS == 0):
            if(pygame.mouse.get_pressed()[0]):
                self.TUTORIAL = 1
                self.tutorial(screen)
                
        self.creditos_surface = pygame.Surface((269, 95))
        self.creditos_rectangle = self.creditos_surface.get_rect(bottomleft = (215, 612))
        if(self.creditos_rectangle.collidepoint(self.mouse_pos) and self.TUTORIAL == 0):
            if(pygame.mouse.get_pressed()[0]):
                self.CREDITOS = 1
                self.creditos(screen)

    def tutorial(self, screen):
        screen.blit(self.como_jogar_surface, (0,0))
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_ESCAPE]:
            self.TUTORIAL = 0

    def creditos(self, screen):
        screen.blit(self.creditar_surface, (0,0))
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_ESCAPE]:
            self.CREDITOS = 0

    # Musica de fundo
    def bg_music(self):

        if self.MENU:
            pygame.mixer.music.load('sounds/menu_music.mp3')
        elif self.game_active:
            pygame.mixer.music.load('sounds/musica_tema_mp3.mp3')
        elif self.GAME_OVER:
            pygame.mixer.music.load('sounds/game_over_music.mp3')
        elif self.GAME_WON:
            pygame.mixer.music.load('sounds/game_won_music.mp3')

        pygame.mixer.music.play(-1)


    def update(self, screen, fantasma, pacman, map, chave, fechadura):
        # Desenha o mapa, player e inimigo
        screen.blit(map.map_surface, (0, 0))
        screen.blit(fantasma.player_surface, fantasma.player_rectangle)
        screen.blit(pacman.enemy_surface, pacman.enemy_rectangle)

        # Desenha as CHAVES
        screen.blit(chave.verde_surface, chave.verde_rectangle) # Verde
        screen.blit(chave.amarela_surface, chave.amarela_rectangle) # Amarela
        screen.blit(chave.rosa_surface, chave.rosa_rectangle) # Rosa
        screen.blit(chave.vermelha_surface, chave.vermelha_rectangle) # Vermelha

        # Desenha as FECHADURAS
        screen.blit(fechadura.verde_surface, fechadura.verde_rectangle) # Verde
        screen.blit(fechadura.amarela_surface, fechadura.amarela_rectangle) # Amarela
        screen.blit(fechadura.rosa_surface, fechadura.rosa_rectangle) # Rosa
        screen.blit(fechadura.vermelha_surface, fechadura.vermelha_rectangle) # Vermelha

        # Desenha os CONTADORES
        screen.blit(chave.chaves_text_surface, chave.chaves_text_rectangle) # Chaves
        screen.blit(fechadura.fechaduras_text_surface, fechadura.fechaduras_text_rectangle) # Fechaduras

        # Desenha o portal
        if self.portal:
            screen.blit(self.portal_surface, self.portal_rectangle)

    def game_reset(self, fantasma, pacman, chave, fechadura, pilha_chaves, pilha_fechaduras, randompos):
        self.game_active = True
        fantasma.origem()
        fantasma.update()
        pacman.origem()
        pacman.update()

        # Reset das chaves e fechaduras
        randompos.reset()
        chave.reset(randompos)
        fechadura.reset(randompos)
        pilha_chaves.reset()
        pilha_fechaduras.reset()

        self.MENU = 0
        self.GAME_OVER = 0
        self.GAME_WON = 0

        self.portal = 0
        self.portal_vel = 1

        self.bg_music()
        
    def is_game_over(self, fantasma, pacman):
        if fantasma.player_rectangle.colliderect(pacman.enemy_rectangle):
            self.game_active = False
            self.GAME_OVER = 1
            self.bg_music()

    def game_over(self, screen, fantasma, pacman, tecla, chave, fechadura, pilha_chaves, pilha_fechaduras, randompos):
        screen.blit(self.game_over_surface, (0,0))

        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_SPACE]:
            self.game_reset(fantasma, pacman, chave, fechadura, pilha_chaves, pilha_fechaduras, randompos)

    def is_portal_open(self, pilha_fechaduras):
        if (pilha_fechaduras.getIndexTopo() + 1 == 4):
            self.portal = 1
            self.portal_open()

            self.portal_rectangle = self.portal_surface.get_rect(center = (289, 325))

            if self.portal_vel < 14:
                self.portal_vel += 1

            self.portal_width = 5 * self.portal_vel
            self.portal_height = 5 * self.portal_vel

            self.portal_surface = pygame.transform.scale(self.portal_surface, (self.portal_width, self.portal_height))

    def portal_open(self):
        self.portal_surface = pygame.image.load("textures/portal/portal.png")
        self.portal_surface = pygame.transform.scale(self.portal_surface, (self.portal_width, self.portal_height))
        self.portal_rectangle = self.portal_surface.get_rect(center = (289, 325))  
              
    
    def is_game_won(self, fantasma, map):
        if self.portal:
            if fantasma.player_rectangle.colliderect(self.portal_rectangle):
                self.game_active = False
                self.GAME_WON = 1
                self.bg_music()
    
    def game_won(self, screen, fantasma, pacman, tecla, chave, fechadura, pilha_chaves, pilha_fechaduras, randompos):
        screen.blit(self.game_won_surface, (0,0))

        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_SPACE]:
            self.game_reset(fantasma, pacman, chave, fechadura, pilha_chaves, pilha_fechaduras, randompos)
        
        if tecla[pygame.K_ESCAPE]:
            pygame.quit()