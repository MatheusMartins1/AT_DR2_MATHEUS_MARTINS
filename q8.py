# Questao 8
# 8. Usando a biblioteca ‘pygame’, escreva um programa que desenha um botão (círculo) com o texto “clique” sobre ele na parte superior da tela.
# Quando o botão for clicado, ele deve chamar uma função que desenha um retângulo em uma posição aleatória na tela.
# Caso um retângulo apareça na mesma posição que um já existente, ambos devem ser eliminados.

import pygame
from pygame.locals import *
from escrever import escreve_texto
from random import randint
import time

pygame.init()
largura_tela, altura_tela = 800, 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO, AZUL, AMARELO = (255, 0, 0), (0, 0, 255), (255, 151, 26)

largura_retangulo, altura_retangulo = 100, 80
x_bola, y_bola, diametro_bola = largura_tela/2, 80, 60

fonte = pygame.font.Font(None, 24)
clock = pygame.time.Clock()


class Retangulo():
    def __init__(self):
        self.largura_retangulo = 160
        self.altura_retangulo = 130
        self.x = randint(0, largura_tela-self.largura_retangulo)
        self.y = randint(0, altura_tela-self.altura_retangulo)
        self.area = pygame.Rect(self.x, self.y, self.largura_retangulo, self.altura_retangulo)
        self.cor = AMARELO

    def desenha_retangulo(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)


def desenha_circulo():
    pygame.draw.circle(tela, AZUL, (x_bola, y_bola), diametro_bola)
    text = fonte.render(f"Clique aqui", 1, BRANCO)
    tela.blit(text, (x_bola-44, y_bola - 10))


lista_retangulos = []
def validar_lista_retangulos(retangulo):
    lista_retangulos.append(retangulo)
    
    if len(lista_retangulos) > 0:
        for rct in lista_retangulos:
            if rct != retangulo:
                index = pygame.Rect.collidepoint(retangulo.area, rct.x, rct.y)
                if index == 1:
                    lista_retangulos.remove(rct)


terminou = False
while not terminou:
    tela.fill(PRETO)

    for retangulo_desenhado in lista_retangulos:
        retangulo_desenhado.desenha_retangulo(tela)

    escreve_texto("Q8", tela, BRANCO, fonte)
    desenha_circulo()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            x_mouse, y_mouse = pos

            # clique dentro do circulo
            if x_mouse >= x_bola - diametro_bola and x_mouse <= x_bola + diametro_bola and y_mouse >= y_bola - diametro_bola and y_mouse <= y_bola + diametro_bola:
                retangulo = Retangulo()
                validar_lista_retangulos(retangulo)

    pygame.display.update()

pygame.display.quit()
pygame.quit()
