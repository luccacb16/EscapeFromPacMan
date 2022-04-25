import pygame
from randompos import *
from constantes import *
from tad import *
from chaves import *

class Fechaduras:
	def __init__(self, pilha_fechaduras, randompos):

		# Contador
		self.font = pygame.font.Font(None, 35)
		self.fechaduras_text_surface = self.font.render(f'{pilha_fechaduras.getIndexTopo()+1}', False, 'White')
		self.fechaduras_text_rectangle = self.fechaduras_text_surface.get_rect(center = (680, 278))

		# Fechadura VERDE (A)
		self.verde_surface = pygame.image.load('textures/fechaduras/fechadura_verde.png').convert_alpha()
		self.verde_surface = pygame.transform.scale(self.verde_surface, (fechaduras_width, fechaduras_height))
		self.verde_rectangle = self.verde_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[4]]))
		self.verde_index = 'A'

		# Fechadura AMARELA (B)
		self.amarela_surface = pygame.image.load('textures/fechaduras/fechadura_amarela.png').convert_alpha()
		self.amarela_surface = pygame.transform.scale(self.amarela_surface, (fechaduras_width, fechaduras_height))
		self.amarela_rectangle = self.amarela_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[5]]))
		self.amarela_index = 'B'

		# Fechadura ROSA (C)
		self.rosa_surface = pygame.image.load('textures/fechaduras/fechadura_rosa.png').convert_alpha()
		self.rosa_surface = pygame.transform.scale(self.rosa_surface, (fechaduras_width, fechaduras_height))
		self.rosa_rectangle = self.rosa_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[6]]))
		self.rosa_index = 'C'

		# Fechadura VERMELHA (D)
		self.vermelha_surface = pygame.image.load('textures/fechaduras/fechadura_vermelha.png').convert_alpha()
		self.vermelha_surface = pygame.transform.scale(self.vermelha_surface, (fechaduras_width, fechaduras_height))
		self.vermelha_rectangle = self.vermelha_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[7]]))
		self.vermelha_index = 'D'

	def reset(self, randompos):

		# Fechadura VERDE (A)
		self.verde_surface = pygame.image.load('textures/fechaduras/fechadura_verde.png').convert_alpha()
		self.verde_surface = pygame.transform.scale(self.verde_surface, (fechaduras_width, fechaduras_height))
		self.verde_rectangle = self.verde_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[4]]))
		self.verde_index = 'A'

		# Fechadura AMARELA (B)
		self.amarela_surface = pygame.image.load('textures/fechaduras/fechadura_amarela.png').convert_alpha()
		self.amarela_surface = pygame.transform.scale(self.amarela_surface, (fechaduras_width, fechaduras_height))
		self.amarela_rectangle = self.amarela_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[5]]))
		self.amarela_index = 'B'

		# Fechadura ROSA (C)
		self.rosa_surface = pygame.image.load('textures/fechaduras/fechadura_rosa.png').convert_alpha()
		self.rosa_surface = pygame.transform.scale(self.rosa_surface, (fechaduras_width, fechaduras_height))
		self.rosa_rectangle = self.rosa_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[6]]))
		self.rosa_index = 'C'

		# Fechadura VERMELHA (D)
		self.vermelha_surface = pygame.image.load('textures/fechaduras/fechadura_vermelha.png').convert_alpha()
		self.vermelha_surface = pygame.transform.scale(self.vermelha_surface, (fechaduras_width, fechaduras_height))
		self.vermelha_rectangle = self.vermelha_surface.get_rect(center = (randompos.posicoes[randompos.posicoes_index[7]]))
		self.vermelha_index = 'D'

	# Colisão fechaduras
	def colisao_fechaduras(self, pilha_chaves, pilha_fechaduras, fantasma, pacman, chave):

		if pilha_chaves.getIndexTopo() + pilha_fechaduras.getIndexTopo() + 1 >= 3:

			if fantasma.player_rectangle.colliderect(self.verde_rectangle): # Verde
				if pilha_chaves.getTopo() == self.verde_index:
					pilha_chaves.desempilha()
					pilha_fechaduras.empilha('A')
					playSom(som_fechadura) # Som

					chave.verde_rectangle = chave.verde_surface.get_rect(center = (1000, 1000))
					self.verde_rectangle = self.verde_surface.get_rect(center = (1000, 1000))
				else:
					playSom(som_wrong) # Som de errado

			if fantasma.player_rectangle.colliderect(self.amarela_rectangle): # Amarela
				if pilha_chaves.getTopo() == self.amarela_index:
					pilha_chaves.desempilha()
					pilha_fechaduras.empilha('B')
					playSom(som_fechadura) # Som

					chave.amarela_rectangle = chave.amarela_surface.get_rect(center = (1000, 1000))
					self.amarela_rectangle = self.amarela_surface.get_rect(center = (1000, 1000))
				else:
					playSom(som_wrong) # Som de errado

			if fantasma.player_rectangle.colliderect(self.rosa_rectangle): # Rosa
				if pilha_chaves.getTopo() == self.rosa_index:

					pilha_chaves.desempilha()
					pilha_fechaduras.empilha('C')
					playSom(som_fechadura) # Som

					chave.rosa_rectangle = chave.rosa_surface.get_rect(center = (1000, 1000))
					self.rosa_rectangle = self.rosa_surface.get_rect(center = (1000, 1000))
				else:
					playSom(som_wrong) # Som de errado

			if fantasma.player_rectangle.colliderect(self.vermelha_rectangle): # Vermelha
				if pilha_chaves.getTopo() == self.vermelha_index:
					pilha_chaves.desempilha()
					pilha_fechaduras.empilha('D')
					playSom(som_fechadura) # Som

					chave.vermelha_rectangle = chave.vermelha_surface.get_rect(center = (1000, 1000))
					self.vermelha_rectangle = self.vermelha_surface.get_rect(center = (1000, 1000))
				else:
					playSom(som_wrong) # Som de errado

			# Impede o pacman de ficar "guardando caixão"
			if pacman.enemy_rectangle.colliderect(self.verde_rectangle): # Verde
				pacman.enemy_x = 288
				pacman.enemy_y = 127

			if pacman.enemy_rectangle.colliderect(self.amarela_rectangle): # Amarela
				pacman.enemy_x = 288
				pacman.enemy_y = 127

			if pacman.enemy_rectangle.colliderect(self.rosa_rectangle): # Rosa
				pacman.enemy_x = 288
				pacman.enemy_y = 127

			if pacman.enemy_rectangle.colliderect(self.vermelha_rectangle): # Vermelha
				pacman.enemy_x = 288
				pacman.enemy_y = 127

	def contador(self, pilha_fechaduras):
		self.fechaduras_text_surface = self.font.render(f'{pilha_fechaduras.getIndexTopo()+1}', False, 'White')