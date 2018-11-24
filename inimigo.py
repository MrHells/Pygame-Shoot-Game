import math,pygame
from pygame.locals import *
from random import randint


pygame.init()

telacheia=FULLSCREEN
branco = (255,255,255)
width = 1600
height = 900
tela= pygame.display.set_mode([width,height], telacheia)

playerpos = [10,10]
lado = 40
personagem = pygame.Rect(playerpos[0],playerpos[1],lado,lado)
fps = pygame.time.Clock()

inimigo = pygame.Rect(playerpos[0]+750,playerpos[1]+460,lado,lado)


drop_aleatorio = randint(0,5)

if drop_aleatorio == 0:
	drop_player = pygame.image.load('vida.png')
if drop_aleatorio == 1:
	drop_player = pygame.image.load('bala.png')
if drop_aleatorio == 2:
	drop_player = pygame.image.load('bala.png')
if drop_aleatorio == 3:
	drop_player = pygame.image.load('moeda.png')
if drop_aleatorio ==4:
	drop_player = pygame.image.load('moeda.png')
if drop_aleatorio == 5:
	drop_player = pygame.image.load('bonus.png')


player = pygame.image.load('parede.png')
player = pygame.transform.scale(player,(50,50))
pygame.key.set_repeat(30,30)

vel = 5
veli = vel-3

c = False
while True:
	fps.tick(60)
	tecla_pressionada = pygame.key.get_pressed()
	#p = pygame.mouse.get_pos()
	tela.fill((160,160,160))
	for event in pygame.event.get():
		
#personagem:

		if tecla_pressionada [K_ESCAPE]:
			pygame.quit()
			exit(0)
		if tecla_pressionada[pygame.K_a]:
			personagem.left -= vel
		if tecla_pressionada[pygame.K_d]:
			personagem.left += vel
		if tecla_pressionada[pygame.K_w]:
			personagem.top -= vel
		if tecla_pressionada[pygame.K_s]:
			personagem.top += vel
		if tecla_pressionada [K_ESCAPE]:
			pygame.quit()
			exit(0)
		
#inimigo:
	
	if inimigo.left < personagem.left:
		inimigo.left +=veli
			
	if inimigo.top < personagem.top:
		inimigo.top +=veli
			
	if inimigo.left > personagem.left:
		inimigo.left -=veli
		
	if inimigo.top > personagem.top:
		inimigo.top -=veli
			
		
		
		
		
		
		'''if tecla_pressionada[pygame.K_LEFT]:
			player.left -= vel
		if tecla_pressionada[pygame.K_RIGHT]:
			player.left += vel
		if tecla_pressionada[pygame.K_UP]:
			player.top -= vel
		if tecla_pressionada[pygame.K_DOWN]:
			player.top += vel'''
			
	if personagem.colliderect(inimigo):
		tela.fill((255,0,0))
		
		
		c = True
		
	pygame.draw.rect(tela,(255,255,255),personagem)
	
	if c == True:
		tela.blit(drop_player,(posx, posy))
	else:
		pygame.draw.rect(tela,(0,0,0),inimigo)
		posx = inimigo.left
		posy = inimigo.top
	tela.blit(player,(personagem.left-6 , personagem.top-6))
	
	pygame.display.update()
  
pygame.display.quit()
