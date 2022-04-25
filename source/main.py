import pygame
from sys import exit

from player import *
from enemy import *
from map import *
from wall import *
from gamestate import *
from constantes import *
from randompos import *
from chaves import *
from fechaduras import *
from tad import *

# Inicia pygame e janela
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Escape From Pacman')
clock = pygame.time.Clock()

# Gamestate do jogo (onde tudo roda)
gamestate = Gamestate()

# Inicia o mapa e as paredes
map = Map()
map.create_walls()

# Inicia a pilha de chaves e fechaduras
pilha_chaves = Pilha()
pilha_fechaduras = Pilha()

# Inicia as Chaves e Fechaduras
randompos = Randompos() # Randomizador de posições das chaves e fechaduras
chave = Chaves(pilha_chaves, randompos)
fechadura = Fechaduras(pilha_fechaduras, randompos)

# Inicia o Player e inimigo
fantasma = Player()
pacman = Enemy()

# Ícone da janela do jogo
pygame.display.set_icon(fantasma.player_surface)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    if gamestate.game_active:
        tecla = pygame.key.get_pressed()
        gamestate.update(screen, fantasma, pacman, map, chave, fechadura) # Atualiza a tela

        fantasma.movimento() # Movimentação do fantasma
        fantasma.update() # Atualiza o fantasma

        pacman.movimento() # Movimentação do PacMan
        pacman.update() # Atualiza o PacMan
        pacman.animate() # Anima o PacMan

        map.colisao_update(fantasma, pacman, tecla, gamestate) # Colisão com as paredes

        gamestate.is_game_over(fantasma, pacman) # Verifica se o player perdeu
        gamestate.is_portal_open(pilha_fechaduras) # Verifica se o portal está aberto
        gamestate.is_game_won(fantasma, map) # Verifica se o player ganhou
        
        # Colisão com as chaves e fechaduras
        chave.colisao_chaves(pilha_chaves, fantasma, pacman)
        fechadura.colisao_fechaduras(pilha_chaves, pilha_fechaduras, fantasma, pacman, chave)

        # Contador de chaves e fechaduras
        chave.contador(pilha_chaves)
        fechadura.contador(pilha_fechaduras)
   
    else:
        # Tela do Menu
        if(gamestate.MENU):
            gamestate.menu(screen, fantasma, pacman, chave, fechadura, pilha_chaves, pilha_fechaduras, randompos)
            # Menu: Tutorial
            if(gamestate.TUTORIAL):
                gamestate.tutorial(screen)
            # Menu: Créditos
            if(gamestate.CREDITOS):
                gamestate.creditos(screen)
        # Tela de Game Over
        if(gamestate.GAME_OVER):
            gamestate.game_over(screen, fantasma, pacman, tecla, chave, fechadura, pilha_chaves, pilha_fechaduras, randompos)
        # Tela de Game Won
        if(gamestate.GAME_WON):
            gamestate.game_won(screen, fantasma, pacman, tecla, chave, fechadura, pilha_chaves, pilha_fechaduras, randompos)

    pygame.display.update()
    clock.tick(60)