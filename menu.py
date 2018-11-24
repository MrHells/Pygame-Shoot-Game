import pygame,math,random
from pygame.locals import *
#from testeclassesbt import *
class Mouse():
	def __init__(self):       
		self.click = pygame.Rect(0, 0, 10, 10)
	def clique(self):
		mousepos = pygame.mouse.get_pos()
		self.click.left = mousepos[0]
		self.click.top = mousepos[1]
		pygame.draw.rect(tela, (0, 0, 0), self.click)
		if self.click.colliderect(jogar):
			import testeclassesbt
		if self.click.colliderect(sair):
			exit(0)
		if self.click.colliderect(melhorias):
			import MenuMelhorias
			



pygame.init()
width = 1366
height = 768
x = FULLSCREEN
tela = pygame.display.set_mode([width,height], x)
pygame.display.set_caption('Cowboy History','A historia de um cowboy')
fundo = pygame.image.load('areia.png')

pygame.font.init()

fonte = pygame.font.get_default_font()
jogartxt = pygame.font.SysFont(fonte, 140)
melhoriastxt = pygame.font.SysFont(fonte,140)
sairtxt = pygame.font.SysFont(fonte,140)

ladoy = 100
ladox = 269
jogar = pygame.Rect(width/2 - ladox/2, height/2, ladox, ladoy)

melhorias = pygame.Rect(jogar.left, jogar.top+100, ladox+195, ladoy)

sair = pygame.Rect(jogar.left, jogar.top+200, ladox-70, ladoy-10)

mira = pygame.image.load('mira.png')
mira = pygame.transform.scale(mira, (60, 60))
pygame.mouse.set_visible(False)
x = pygame.time.Clock()

mouse = Mouse()

pygame.key.set_repeat(10,10)

while True:
	tela.fill((0, 0, 0))
	tela.blit(fundo, (0, 0))

	mousepos = pygame.mouse.get_pos()

	tecla_pressionada = pygame.key.get_pressed()
	if tecla_pressionada[K_ESCAPE]:
		pygame.quit()
		exit(0)


	pygame.draw.rect(tela, (255, 0, 0), jogar)
	pygame.draw.rect(tela, (0, 255, 0), melhorias)
	pygame.draw.rect(tela, (0, 0, 255), sair)

	text = jogartxt.render('Jogar', 1, (255,0,255))
	tela.blit(text, (jogar.left,jogar.top))
	text = melhoriastxt.render('Melhorias', 1, (255, 0, 255))
	tela.blit(text, (melhorias.left, melhorias.top))
	text = sairtxt.render('Sair', 1, (255, 0, 255))
	tela.blit(text, (sair.left, sair.top))
	ev = pygame.event.get()

	# proceed events
	for event in ev:

		# handle MOUSEBUTTONUP
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse.clique()
	'''for event in pygame.event.get():
		if tecla_pressionada[K_SPACE]:
			mouse.clique()
		'''	
			
	tela.blit(mira, (mousepos[0]-30, mousepos[1]-30))

	pygame.display.flip()
