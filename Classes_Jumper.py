# -*- coding: utf-8 -*-
"""
Created on Wed May  9 00:51:28 2018

@author: Lenovo
"""

import pygame
from random import randint
import numpy as np
from random import randrange
import sys

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

width = 1024
height = 1024
size = 10

#=========  CLASSES ==========

class Boneco (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem,pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
    
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
    
class Plataforma (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
# ===============   INICIALIZAÇÃO   ===============
        
pygame.init()

relogio = pygame.time.Clock() #Cria relogio para definir FPS

tela = pygame.display.set_mode((width,height),0,32) #Tamanho da tela
pygame.display.set_caption('TESTE PULO') #Nome na aba

# carrega imagem de fundo
fundo = pygame.image.load("colored_grass.png").convert()

boneco = Boneco("alienBlue_stand.png",randrange(width),randrange(height),randrange(-10,10), randrange(-20,10))
boneco_group = pygame.sprite.Group()
boneco_group.add(boneco)

plataforma = Plataforma("ground_grass.png", randrange(10),randrange(30))
plataforma_group = pygame.sprite.Group()
plataforma_group.add(plataforma)

# ===============   LOOPING PRINCIPAL   ===============
sair = True
while sair:
    for event in pygame.event.get(): #Controla eventos
       if event.type == pygame.QUIT: #Botao de fechar
           sair = False #Sai do loop 
       pressed_keys=pygame.key.get_pressed()
       if pressed_keys[pygame.K_UP]:
           boneco.rect.y -= 10
       elif pressed_keys[pygame.K_DOWN]:
           boneco.rect.y += 10


    
    tela.blit(fundo, (0, 0))
    boneco_group.draw(tela)
    plataforma_group.draw(tela)
    pygame.display.update()      #coloca a tela na janela










pygame.quit() #Sai do jogo

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    