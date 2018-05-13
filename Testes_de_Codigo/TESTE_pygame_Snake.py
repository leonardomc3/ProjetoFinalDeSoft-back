# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 18:46:29 2018

@author: Lenovo
"""
import pygame
from random import randint

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
pygame.display.set_caption('Snake Muito loko') #Nome na aba

#def snake(pos_x,pos_y):
    #pygame.draw.rect(fundo,blue,[pos_x,pos_y,size,size],0) #Desenha o retangulo. Diz onde, que cor, a posicao e o tamanho. Zero para estar preenchido
def snake(snakeXY):
    for XY in snakeXY:
        pygame.draw.rect(fundo,blue,[XY[0],XY[1],size,size],0)
        
def apple(pos_x,pos_y):
    pygame.draw.rect(fundo,green,[pos_x,pos_y,size,size],0)


def game():
    sair=True
    pos_x=randint(0,(width-size)/10)*10 #Alinhar com a grade
    pos_y=randint(0,(height-size)/10)*10
    apple_x=randint(0,(width-size)/10)*10 #Alinhar com a grade
    apple_y=randint(0,(height-size)/10)*10
    vel_x=0
    vel_y=0
    snakeXY = []
    snakeComp = 5
    while sair: #loop principal do jogo
        for event in pygame.event.get(): #Controla eventos
            if event.type == pygame.QUIT: #Botao de fechar
                sair=False #Sai do loop
            if event.type == pygame.KEYDOWN:#Movendo em size o objeto permanece na grade
                if event.key == pygame.K_LEFT and vel_x!=size: #And para impedir que a cobra consiga se mover para o lado completamente oposto
                    #pos_x-=10
                    vel_y=0
                    vel_x=-size
                if event.key == pygame.K_RIGHT and vel_x!=-size:
                    #pos_x+=10
                    vel_y=0
                    vel_x=+size
                if event.key == pygame.K_DOWN and vel_y!=-size:
                    #pos_y+=10
                    vel_x=0
                    vel_y=size
                if event.key == pygame.K_UP and vel_y!=size:
                    #pos_y-=10
                    vel_x=0
                    vel_y=-size
                    
        
            
        fundo.fill(red) #Cor do fundo
        pos_x+=vel_x
        pos_y+=vel_y
        testapos = []
        testapos.append(pos_x)
        testapos.append(pos_y)
        
        if testapos in snakeXY and testapos!=snakeXY[0]: #Matar cobra ao encostar em si mesma
            pygame.quit()
        
        
        
        snakeinicio = []
        snakeinicio.append(pos_x)
        snakeinicio.append(pos_y)
        snakeXY.append(snakeinicio)
        
        if len(snakeXY) > snakeComp:
            del snakeXY[0]
        
            
        #snake(pos_x,pos_y)
        snake(snakeXY)
        apple(apple_x,apple_y)
        
        
        
        pygame.display.update() #Atualiza a tela com os novos eventos
        relogio.tick(20) #Define FPS
        
        if pos_x == apple_x and pos_y == apple_y:
            apple_x=randint(0,(width-size)/10)*10 #Alinhar com a grade
            apple_y=randint(0,(height-size)/10)*10
            snakeComp+=1
            
        if pos_x>width:#Feito para o objeto "atravessar" as bordas e reaparecer do outro lado
            pos_x=0
        if pos_x<0:
            pos_x=width-size
        if pos_y>height:
            pos_y=0
        if pos_y<0:
            pos_y=height-size
        '''if pos_x>width: #Morre ao tocar nas bordas
            sair=False
        if pos_x<0:
            sair=False
        if pos_y>height:
            sair=False
        if pos_y<0:
            sair=False'''
    
    
game()    
pygame.quit() #Sai do jogo
