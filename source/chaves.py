import pygame
from randompos import *
from constantes import *
from tad import *
from player import *

class Chaves:
	def __init__(self, pilha_chaves, randompos):

		# Inventário e contador
		self.inventario_x = 635
		self.inventario_y = [191, 141, 91, 41]

		self.font = pygame.font.Font(None, 35)
		self.chaves_text_surface = self.font.render(f'{pilha_chaves.getIndexTopo()+1}', False, 'White')
		self.chaves_text_rectangle = self.chaves_text_surface.get_rect(center = (680, 244))

		# Chave VERDE (A)
		self.verde_surface = pygame.image.load('textures/chaves/chave_verde.png').convert_alpha()
		self.verde_surface = pygame.transform.scale(self.verde_surface, (chaves_width, chaves_height))
		self.verde_rectangle = self.verde_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[0]]))
		self.verde_index = 'A'

		# Chave AMARELA (B)
		self.amarela_surface = pygame.image.load('textures/chaves/chave_amarela.png').convert_alpha()
		self.amarela_surface = pygame.transform.scale(self.amarela_surface, (chaves_width, chaves_height))
		self.amarela_rectangle = self.amarela_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[1]]))
		self.amarela_index = 'B'

		# Chave ROSA (C)
		self.rosa_surface = pygame.image.load('textures/chaves/chave_rosa.png').convert_alpha()
		self.rosa_surface = pygame.transform.scale(self.rosa_surface, (chaves_width, chaves_height))
		self.rosa_rectangle = self.rosa_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[2]]))
		self.rosa_index = 'C'

		# Chave VERMELHA (D)
		self.vermelha_surface = pygame.image.load('textures/chaves/chave_vermelha.png').convert_alpha()
		self.vermelha_surface = pygame.transform.scale(self.vermelha_surface, (chaves_width, chaves_height))
		self.vermelha_rectangle = self.vermelha_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[3]]))
		self.vermelha_index = 'D'

		# Manda chave pro inventário
	def setInv(self, pilha_chaves):
		qtdChaves = pilha_chaves.getIndexTopo()
		index = pilha_chaves.getTopo()

		playSom(som_chave) # Som

		if index == 'A':
			self.verde_rectangle = self.verde_surface.get_rect(center = (self.inventario_x, self.inventario_y[qtdChaves]))
			self.verde_surface = pygame.transform.scale(self.verde_surface, (chaves_width_inv, chaves_height_inv))
            
		if index == 'B':
			self.amarela_rectangle = self.amarela_surface.get_rect(center = (self.inventario_x, self.inventario_y[qtdChaves]))
			self.amarela_surface = pygame.transform.scale(self.amarela_surface, (chaves_width_inv, chaves_height_inv))
            
		if index == 'C':
			self.rosa_rectangle = self.rosa_surface.get_rect(center = (self.inventario_x, self.inventario_y[qtdChaves]))
			self.rosa_surface = pygame.transform.scale(self.rosa_surface, (chaves_width_inv, chaves_height_inv))

		if index == 'D':
			self.vermelha_rectangle = self.vermelha_surface.get_rect(center = (self.inventario_x, self.inventario_y[qtdChaves]))
			self.vermelha_surface = pygame.transform.scale(self.vermelha_surface, (chaves_width_inv, chaves_height_inv))

	def colisao_chaves(self, pilha_chaves, fantasma, pacman):
		# Colisão com as chaves
		if fantasma.player_rectangle.colliderect(self.verde_rectangle): # Verde
			pilha_chaves.empilha(self.verde_index)
			self.setInv(pilha_chaves)

		if fantasma.player_rectangle.colliderect(self.amarela_rectangle): # Amarela
			pilha_chaves.empilha(self.amarela_index)
			self.setInv(pilha_chaves)

		if fantasma.player_rectangle.colliderect(self.rosa_rectangle): # Rosa
			pilha_chaves.empilha(self.rosa_index)
			self.setInv(pilha_chaves)

		if fantasma.player_rectangle.colliderect(self.vermelha_rectangle): # Vermelha
			pilha_chaves.empilha(self.vermelha_index)
			self.setInv(pilha_chaves)

		# Impede o pacman de ficar "guardando caixão"
		if pacman.enemy_rectangle.colliderect(self.verde_rectangle): # Verde
			pacman.enemy_x = 256
			pacman.enemy_y = 260

		if pacman.enemy_rectangle.colliderect(self.amarela_rectangle): # Amarela
			pacman.enemy_x = 256
			pacman.enemy_y = 260

		if pacman.enemy_rectangle.colliderect(self.rosa_rectangle): # Rosa
			pacman.enemy_x = 256
			pacman.enemy_y = 260

		if pacman.enemy_rectangle.colliderect(self.vermelha_rectangle): # Vermelha
			pacman.enemy_x = 256
			pacman.enemy_y = 260

	def reset(self, randompos):

		# Inventário
		self.inventario_x = 635
		self.inventario_y = [191, 141, 91, 41]

		# Chave VERDE (A)
		self.verde_surface = pygame.image.load('textures/chaves/chave_verde.png').convert_alpha()
		self.verde_surface = pygame.transform.scale(self.verde_surface, (chaves_width, chaves_height))
		self.verde_rectangle = self.verde_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[0]]))
		self.verde_index = 'A'

		# Chave AMARELA (B)
		self.amarela_surface = pygame.image.load('textures/chaves/chave_amarela.png').convert_alpha()
		self.amarela_surface = pygame.transform.scale(self.amarela_surface, (chaves_width, chaves_height))
		self.amarela_rectangle = self.amarela_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[1]]))
		self.amarela_index = 'B'

		# Chave ROSA (C)
		self.rosa_surface = pygame.image.load('textures/chaves/chave_rosa.png').convert_alpha()
		self.rosa_surface = pygame.transform.scale(self.rosa_surface, (chaves_width, chaves_height))
		self.rosa_rectangle = self.rosa_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[2]]))
		self.rosa_index = 'C'

		# Chave VERMELHA (D)
		self.vermelha_surface = pygame.image.load('textures/chaves/chave_vermelha.png').convert_alpha()
		self.vermelha_surface = pygame.transform.scale(self.vermelha_surface, (chaves_width, chaves_height))
		self.vermelha_rectangle = self.vermelha_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[3]]))
		self.vermelha_index = 'D'
		
	def contador(self, pilha_chaves):
		self.chaves_text_surface = self.font.render(f'{pilha_chaves.getIndexTopo()+1}', False, 'White')