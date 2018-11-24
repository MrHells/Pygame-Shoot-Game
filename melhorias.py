import math, random,pygame
from pygame.locals import *
from random import randint

pygame.init()

fps = pygame.time.Clock()

telacheia=FULLSCREEN
branco = (255,255,255)
width = 1366
height = 768
tela= pygame.display.set_mode([width,height], telacheia)



comp = 800
alt = 50
quadrado = 50

retangulo1 = pygame.Rect(150,200,comp,alt)
retangulo2 = pygame.Rect(150,350,comp,alt)
retangulo3 = pygame.Rect(150,500,comp,alt)
retangulo4 = pygame.Rect(150,650,comp,alt)
retangulo5 = pygame.Rect(150,800,comp,alt)

quadrado1 = pygame.Rect(50,200,quadrado,quadrado)
quadrado2 = pygame.Rect(50,350,quadrado,quadrado)
quadrado3 = pygame.Rect(50,500,quadrado,quadrado)
quadrado4 = pygame.Rect(50,650,quadrado,quadrado)
quadrado5 = pygame.Rect(50,800,quadrado,quadrado)

pygame.font.init()


fonte_padrao = pygame.font.get_default_font()

titulo = pygame.font.SysFont(fonte_padrao,85)
texto_titulo = titulo.render('MELHORIAS',1,(0,0,0))

texto = pygame.font.SysFont(fonte_padrao,30)

titulo_velocidade = texto.render('Velocidade de Movimentação:',1,(0,0,0))
texto_velocidade = texto.render('A melhoria de velocidade permite que Hugo ande mais rápido!',1,(0,0,0))
mira = pygame.image.load('mira.png')
mira = pygame.transform.scale(mira, (60, 60))

while True:
	fps.tick(60)
	tecla_pressionada = pygame.key.get_pressed()
	tela.fill((branco))
	for event in pygame.event.get():
		if tecla_pressionada [K_ESCAPE]:
			pygame.quit()
			exit(0)

	pygame.draw.rect(tela,(0,0,0),retangulo1)
	pygame.draw.rect(tela,(0,0,0),retangulo2)
	pygame.draw.rect(tela,(0,0,0),retangulo3)
	pygame.draw.rect(tela,(0,0,0),retangulo4)
	pygame.draw.rect(tela,(0,0,0),retangulo5)

	pygame.draw.rect(tela,(0,0,0),quadrado1)
	pygame.draw.rect(tela,(0,0,0),quadrado2)
	pygame.draw.rect(tela,(0,0,0),quadrado3)
	pygame.draw.rect(tela,(0,0,0),quadrado4)
	pygame.draw.rect(tela,(0,0,0),quadrado5)

	mousepos = pygame.mouse.get_pos()
	tela.blit(mira, (mousepos[0]-30, mousepos[1]-30))


	tela.blit(texto_titulo,(620,70))


	tela.blit(titulo_velocidade,(970,200))
	tela.blit(texto_velocidade,(970,230))

	pygame.display.update()
	

pygame.display.quit()
