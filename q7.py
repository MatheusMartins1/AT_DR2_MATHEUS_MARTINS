#Questao 7
# 7. Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta), 
# toda vez que a tecla espaço for pressionada ou o botão direito for clicado.
import pygame
from pygame.locals import *
from escrever import escreve_texto
import random

pygame.init()
largura_tela, altura_tela = 600, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO, AZUL, AMARELO = (255, 0, 0), (0,0,255),(255, 151, 26)
tela.fill(PRETO)
largura_quadrado,altura_quadrado = 40,40

x,y= largura_tela/2-largura_quadrado/2, altura_tela/2-altura_quadrado/2

def desenha_retangulo(x,y):
    pygame.draw.rect(tela, AMARELO, (x,y,largura_quadrado, altura_quadrado), 0)

terminou = False
while not terminou:
    tela.fill(PRETO)
    escreve_texto("Q7",tela,BRANCO,pygame.font.Font(None, 24))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
       
        if event.type == pygame.KEYDOWN and event.key == K_SPACE or event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x,y = random.randint(0, 560),random.randint(0, 560)

    desenha_retangulo(x,y)
    pygame.display.update() 

pygame.display.quit()
pygame.quit()