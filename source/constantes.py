import pygame

# Tamanho das chaves
chaves_k = 1.65
chaves_k2 = 2.4

chaves_width = 7 * chaves_k
chaves_height = 13 * chaves_k

chaves_width_inv = 7 * chaves_k2
chaves_height_inv = 13 * chaves_k2

# Tamanho das fechaduras
fechaduras_k = 1.25
fechaduras_width = 13 * fechaduras_k
fechaduras_height = 19 * fechaduras_k

# Constantes do player
vel_player = 5

player_k = 2.1
player_width = 10 * player_k
player_height = 10 * player_k

# Constantes do inimigo
vel_enemy = 4.25

enemy_k = 2.1
enemy_width = 10 * enemy_k
enemy_height = 10 * enemy_k

# Sons
pygame.mixer.init() # Inicializa o mixer

som_chave = pygame.mixer.Sound('sounds/pegando_chaves.wav') # 1
som_fechadura = pygame.mixer.Sound('sounds/fechadura.wav') # 2 
som_wrong = pygame.mixer.Sound('sounds/wrong_sound.wav') # 3

def playSom(escolha):
	escolha.play()