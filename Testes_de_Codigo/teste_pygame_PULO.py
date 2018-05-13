# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 18:46:29 2018

@author: Lenovo
"""
import pygame
from random import randint
import numpy

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)


pygame.init()

width=640
height=480
size=10

relogio=pygame.time.Clock() #Cria relogio para definir FPS



fundo=pygame.display.set_mode((640,480)) #Tamanho da tela
pygame.display.set_caption('TESTE PULO') #Nome na aba

#def snake(pos_x,pos_y):
    #pygame.draw.rect(fundo,blue,[pos_x,pos_y,size,size],0) #Desenha o retangulo. Diz onde, que cor, a posicao e o tamanho. Zero para estar preenchido
def Boneco(pos_x,pos_y):
        pygame.draw.rect(fundo,blue,[pos_x,pos_y,2*size,3*size],0)
        
def Plataforma1(pos_x,pos_y):
    pygame.draw.rect(fundo,green,[pos_x,pos_y,4*size,size],0)
def Plataforma2(pos_x,pos_y):
    pygame.draw.rect(fundo,green,[pos_x,pos_y,4*size,size],0)
def Plataforma3(pos_x,pos_y):
    pygame.draw.rect(fundo,green,[pos_x,pos_y,4*size,size],0)


def game():
    sair=True
    pos_x=randint(0,(width-size)/10)*10 #Alinhar com a grade
    pos_y=randint(0,(height-size)/10)*10
    plat_x1=randint(0,(width-size)/10)*10 #Alinhar com a grade
    plat_y1=randint(0,(height-size)/10)*10
    plat_x2=randint(0,(width-size)/10)*10 #Alinhar com a grade
    plat_y2=randint(0,(height-size)/10)*10
    plat_x3=randint(0,(width-size)/10)*10 #Alinhar com a grade
    plat_y3=randint(0,(height-size)/10)*10
    vel_x=0
    vel_y=5
    while sair: #loop principal do jogo
        for event in pygame.event.get(): #Controla eventos
            if event.type == pygame.QUIT: #Botao de fechar
                sair=False #Sai do loop
            if event.type == pygame.KEYDOWN:#Movendo em size o objeto permanece na grade
                if event.key == pygame.K_LEFT: #And para impedir que a cobra consiga se mover para o lado completamente oposto
                    pos_x-=20
                    #vel_x=-size
                if event.key == pygame.K_RIGHT:
                    pos_x+=20
                    #vel_x=+size
                #if event.key == pygame.K_DOWN:
                    #pos_y+=20
                    #vel_x=0
                    #vel_y=size
                if event.key == pygame.K_UP:
                    pos_y-=40
                    #vel_x=0
                    #vel_y=-size'''
                    
        
            
        fundo.fill(red) #Cor do fundo
        pos_x+=vel_x
        pos_y+=vel_y
        
        
            
        Boneco(pos_x,pos_y)
        Plataforma1(plat_x1,plat_y1)
        Plataforma2(plat_x2,plat_y2)
        Plataforma3(plat_x3,plat_y3)
        
        if pos_y+20 == plat_y1 and pos_x in numpy.arange(plat_x1-10,plat_x1+50,1):
            pos_y-=200
        if pos_y+20 == plat_y2 and pos_x in numpy.arange(plat_x2-10,plat_x2+50,1):
            pos_y-=200
        if pos_y+20 == plat_y3 and pos_x in numpy.arange(plat_x3-10,plat_x3+50,1):
            pos_y-=200
        
        
        if pos_x>width:#Feito para o objeto "atravessar" as bordas e reaparecer do outro lado
            pos_x=0
        if pos_x<0:
            pos_x=width-size
        if pos_y>height-4*size:
            sair=False
        
        
        pygame.display.update() #Atualiza a tela com os novos eventos
        relogio.tick(20) #Define FPS
        
            
    
    
    
game()    
pygame.quit() #Sai do jogo
