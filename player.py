#!/usr/bin/env python3

import pygame


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100

        self.width = 50
        self.height = 50

        self.image = pygame.image.load("img/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.vel = (0.5, 0.5)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel[0]
        if keys[pygame.K_RIGHT]:
            self.x += self.vel[0]
        if keys[pygame.K_UP]:
            self.y -= self.vel[0]
        if keys[pygame.K_DOWN]:
            self.y += self.vel[0]

        self.rect = (self.x, self.y, self.width, self.height)

    def update(self, display):
        # chama para processar qualquer movimento
        self.move()
        # redesenha na tela
        display.blit(self.image, (self.x, self.y))
