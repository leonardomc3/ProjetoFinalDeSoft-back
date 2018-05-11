# -*- coding: utf-8 -*-
"""
Created on Wed May  9 00:51:28 2018

@author: Lenovo
"""

import pygame
import random
import numpy as np
import sys

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

width = 800
height = 600
size = 10
gravity = 1

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
        self.platforms = [[400, 500, 0, 0]]
        
    def generatePlatforms(self):
        on = 600
        while on > -100:
            x = random.randint(0,700)
            self= random.randint(0, 1000)
            if self < 800:
                self = 0
            elif self < 900:
                self = 1
            else:
                self = 2
            self.image.append([x, on, self, 0])
            on -= 50
        
# ===============   INICIALIZAÇÃO   ===============
        
pygame.init()

relogio = pygame.time.Clock() #Cria relogio para definir FPS

tela = pygame.display.set_mode((width,height),0,32) #Tamanho da tela
pygame.display.set_caption('TESTE PULO') #Nome na aba

# carrega imagem de fundo
fundo = pygame.image.load("Imagens/Fundo_800x600.png").convert()

boneco = Boneco("Imagens/Alien_80x80.png",width/2,height/4,0,-1/10)
boneco_group = pygame.sprite.Group()
boneco_group.add(boneco)

plataforma = Plataforma("Imagens/Plataforma_verde.png",width/2,height/2)
plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(width),random.randrange(height))
plataforma3 = Plataforma("Imagens/Plataforma_verde.png",width/3,height/3)
plataforma_group = pygame.sprite.Group()
plataforma_group.add(plataforma)
plataforma_group.add(plataforma2)
plataforma_group.add(plataforma3)

# ===============   LOOPING PRINCIPAL   ===============
sair = True
while sair:
    for event in pygame.event.get(): #Controla eventos
       if event.type == pygame.QUIT: #Botao de fechar
           sair = False #Sai do loop 
       pressed_keys=pygame.key.get_pressed()
       if pressed_keys[pygame.K_UP]:
           boneco.vy -= 10
       elif pressed_keys[pygame.K_DOWN]:
           boneco.vx = 0
       elif pressed_keys[pygame.K_LEFT]:
           boneco.vx = -3
       elif pressed_keys[pygame.K_RIGHT]:
           boneco.vx = +3
           
    if pygame.sprite.spritecollide(boneco,plataforma_group,False):
        #boneco.vx=-boneco.vx
        #boneco.vy=-boneco.vy
        boneco.vy = -20
    
    boneco.rect.y += boneco.vy
    boneco.rect.x += boneco.vx
    boneco.vy += gravity
    
#Feito para o objeto "atravessar" as bordas e reaparecer do outro lado
    if boneco.rect.x > width:
        boneco.rect.x = 0
    if boneco.rect.x < 0:
        boneco.rect.x = width-size
    if boneco.rect.y > height:
        sair=False

    tela.blit(fundo, (0, 0))
    boneco_group.draw(tela)
    plataforma_group.draw(tela)
    pygame.display.update()      #coloca a tela na janela
    relogio.tick(20) #Define FPS









pygame.quit() #Sai do jogo

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    