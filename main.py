#!/usr/bin/env python3

import pygame
import sys

from player import Player

pygame.init()  # inicializa a biblioteca

WIDTH = 350
HEIGHT = 650
display = pygame.display.set_mode((WIDTH, HEIGHT))  # inicia a tela
pygame.display.set_caption("Nome do Meu Jogo")

clock = pygame.time.Clock()  # inicia o relógio

p = Player()  # cria um jogador

while True:
    # Processa os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # background
    display.fill((255, 255, 255))

    # Processa o jogador
    p.update(display)

    pygame.display.update()  # atualiza a tela

    clock.tick(60)  # 60 frames por segundo
