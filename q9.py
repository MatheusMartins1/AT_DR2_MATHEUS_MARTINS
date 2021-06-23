# Questao 9
# 9. Usando o código anterior, escreva um novo programa que, quando as teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas,
# ele movimente o círculo com o texto “clique” nas direções corretas.
# Caso colida com algum retângulo, o retângulo que participou da colisão deve desaparecer.


import pygame
from pygame.locals import *
from escrever import escreve_texto
from random import randint
import time

pygame.init()
largura_tela, altura_tela = 800, 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
AZUL, AMARELO = (0, 0, 255), (255, 151, 26)

x_circulo, y_circulo, diametro_circulo = largura_tela/2, 80, 60

fonte = pygame.font.Font(None, 24)
clock = pygame.time.Clock()


def desenha_circulo(x_circulo, y_circulo):
    pygame.draw.circle(tela, AZUL, (x_circulo, y_circulo), diametro_circulo)
    text = fonte.render(f"Clique aqui", 1, BRANCO)
    tela.blit(text, (x_circulo-44, y_circulo - 10))


class Teclas:
    def __init__(self, w, a, s, d):
        self.w = w
        self.a = a
        self.s = s
        self.d = d


teclas = Teclas(False, False, False, False)


def move_circulo(teclas, x_circulo, y_circulo):
    if teclas.w and y_circulo > diametro_circulo:
        y_circulo -= 1
    elif teclas.s and y_circulo < altura_tela-diametro_circulo:
        y_circulo += 1
    if teclas.a and x_circulo > diametro_circulo:
        x_circulo -= 1
    elif teclas.d and x_circulo < largura_tela-diametro_circulo:
        x_circulo += 1

    if x_circulo == diametro_circulo:
        x_circulo = largura_tela-diametro_circulo
    elif x_circulo == largura_tela-diametro_circulo:
        x_circulo = diametro_circulo
    elif y_circulo == diametro_circulo:
        y_circulo = altura_tela-diametro_circulo
    elif y_circulo == altura_tela-diametro_circulo:
        y_circulo = diametro_circulo

    return x_circulo, y_circulo


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

    escreve_texto("Q9", tela, BRANCO, fonte)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

        # Enquanto estiver pressionado, o coelho vai se mexer
        if event.type == pygame.KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                teclas.w = True
            elif event.key == K_a or event.key == K_LEFT:
                teclas.a = True
            elif event.key == K_s or event.key == K_DOWN:
                teclas.s = True
            elif event.key == K_d or event.key == K_RIGHT:
                teclas.d = True

        # No momento que parou de pressionar a tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                teclas.w = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                teclas.a = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                teclas.s = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                teclas.d = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            x_mouse, y_mouse = pos

            # clique dentro do circulo
            if x_mouse >= x_circulo - diametro_circulo and x_mouse <= x_circulo + diametro_circulo and y_mouse >= y_circulo - diametro_circulo and y_mouse <= y_circulo + diametro_circulo:
                retangulo = Retangulo()
                validar_lista_retangulos(retangulo)
    
    x_circulo, y_circulo = move_circulo(teclas, x_circulo, y_circulo)
    desenha_circulo(x_circulo, y_circulo)
    pygame.display.update()

pygame.display.quit()
pygame.quit()
