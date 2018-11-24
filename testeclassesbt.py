import pygame, math, random
from pygame.locals import *
from  random import randint
from menu import *


class Inimigo:

	def __init__(self, playerdz):
		self.playerdz = playerdz
		self.enemypos = [1200, 500]
		self.inimigo = pygame.Rect(self.enemypos[0], self.enemypos[1], self.playerdz.lado, self.playerdz.lado)
		inimigoimg = pygame.image.load('jogador23.png')
		self.inimigoimg = pygame.transform.scale(inimigoimg, (40, 30))
		self.inimigos = []
		self.inimigos1 = []
		self.inimigo_vivo = True
		self.cooldownEnemi = 0
		self.veli = 2

	def inimigo_spawn(self, height, width):
		if self.cooldownEnemi == 0:
			self.cooldownEnemi = 0
			x = randint(1, 4)
			if x == 1:
				self.enemypos = [0, 0]

			elif x == 2:
				self.enemypos = [width, 0]

			elif x == 3:
				self.enemypos = [0, height]

			else:
				self.enemypos = [width, height]
			self.enemypos = [1200,500]
			self.inimigos.append(self.enemypos)
			self.inimigos1.append(self.inimigo)
				
			self.cooldownEnemi -= 1

	def inimigo_move(self, playerdz, tela):
		c = 0
		for dagger in self.inimigos:

			if self.inimigos1[c].left < self.playerdz.player.left:
				dagger[0] += self.veli
				self.inimigos1[c].left = dagger[0]

			if self.inimigos1[c].top < self.playerdz.player.top:
				dagger[1] += self.veli
				self.inimigos1[c].top = dagger[1]

			if self.inimigos1[c].left > self.playerdz.player.left:
				dagger[0] -= self.veli
				self.inimigos1[c].left = dagger[0]

			if self.inimigos1[c].top > self.playerdz.player.top:
				dagger[1] -= self.veli
				self.inimigos1[c].top = dagger[1]

			pygame.draw.rect(tela, (255, 255, 255), self.inimigos1[c])
			c += 1

class Shoot:

	def __init__(self, playerdz):
		self.playerdz = playerdz
		self.daggers = []
		DAGGER_IMG = pygame.image.load('tiro.png')
		self.tiroimg = pygame.transform.scale(DAGGER_IMG, (20, 20))
		self.cooldown = 0
		
	def tiro(self):
		print('something')
		if self.cooldown == 0:

			vel_x = math.cos(self.playerdz.angle) * 5
			vel_y = math.sin(self.playerdz.angle) * 5
			self.dagger_img = pygame.transform.rotate(self.tiroimg, -math.degrees(self.playerdz.angle))
			width, height = self.dagger_img.get_size()
			self.daggers.append(
					[[self.playerdz.player.left, self.playerdz.player.top],  # Pos
					 [vel_x, vel_y],  # Velocity
					 self.tiroimg  # Image
					 ])
			self.cooldown = 15
			print(str(len(self.daggers)))

	def passo_bala(self, tela):
		for dagger in self.daggers:
			tela.blit(self.tiroimg, (dagger[0][0], dagger[0][1]))
			dagger[0][0] += dagger[1][0]
			dagger[0][1] += dagger[1][1]
			
	def coldown(self):
		if self.cooldown > 0:
			self.cooldown -= 1

class Player():
	def __init__(self, tela):
		self.playerpos = [500, 500]
		self.lado = 27
		self.tela = tela
		self.player = pygame.Rect(self.playerpos[0], self.playerpos[1], self.lado, self.lado)
		jogador = pygame.image.load('personagem.png')
		self.jogador = pygame.transform.scale(jogador, (50, 40))

	def movimento(self,playervel):
		
		tecla_pressionada = pygame.key.get_pressed()
		for event in pygame.event.get():
			if tecla_pressionada[pygame.K_a]:
				self.player.move_ip(-playervel, 0)
			if tecla_pressionada[pygame.K_d]:
				self.player.move_ip(playervel, 0)
			if tecla_pressionada[pygame.K_w]:
				self.player.move_ip(0, -playervel)
			if tecla_pressionada[pygame.K_s]:
				self.player.move_ip(0, playervel)

	def sairtela(self, width, height, playervel):

		if self.player.bottom > height:
			self.player.bottom = height - 1

		if self.player.right > width:
			self.player.right = width - 1

		if self.player.left < 0:
			self.player.left = 0

		if self.player.top < 0:
			self.player.top = 0

		self.playerpos = [self.player.left, self.player.top]

	def rotacao(self):
		position = pygame.mouse.get_pos()
		self.angle = math.atan2(position[1] - self.playerpos[1], position[0] - self.playerpos[0])
		self.playerrot = pygame.transform.rotate(self.jogador, 360 - self.angle * 57.29)
		self.playerpos1 = (self.playerpos[0] - self.playerrot.get_rect().width / 2, self.playerpos[1] - self.playerrot.get_rect().height / 2)
		self.tela.blit(self.playerrot, (self.playerpos1[0] + 13, self.playerpos1[1] + 13))

	def show(self):
		pygame.draw.rect(self.tela, (255, 255, 255), self.player)


def main():
	
	playervel = 5
	
	width = 1366
	height = 768
	x = FULLSCREEN
	tela = pygame.display.set_mode([width, height], x)
	pygame.display.set_caption('Cowboy History', 'A historia de um cowboy')
	
	playerdz = Player(tela)
	balas = Shoot(playerdz)
	
	pygame.key.set_repeat(10, 10)
	fundo = pygame.image.load('areia.png')
	fundo = pygame.transform.scale(fundo, (width, height))
		
	mira = pygame.image.load('mira.png')
	mira = pygame.transform.scale(mira, (60, 60))

	inimigosc = Inimigo(playerdz)

	fps = pygame.time.Clock()

	while True:
		fps.tick(30)
		mouse_position = pygame.mouse.get_pos()
		# Distances to the mouse position.
		rise = mouse_position[1] - playerdz.player.centery
		run = mouse_position[0] - playerdz.player.centerx
		angle = math.atan2(rise, run)
		tecla_pressionada = pygame.key.get_pressed()

		if tecla_pressionada[K_ESCAPE]:
			exit(666)

			'''pygame.draw.rect(tela, (255, 255, 255), sair)
			pygame.draw.rect(tela, (255, 255, 255), sair2)
			import menu'''

		tela.fill([255, 255, 255])
		tela.blit(fundo, (0, 0))
		if tecla_pressionada[K_SPACE]:
			balas.tiro()

		inimigosc.inimigo_spawn(height, width)
		inimigosc.inimigo_move(playerdz, tela)

		playerdz.show()
		playerdz.movimento(playervel)
		playerdz.sairtela(width, height,playervel)
		playerdz.rotacao()
		balas.passo_bala( tela)
		mousepos = pygame.mouse.get_pos()
		tela.blit(mira, (mousepos[0]-30, mousepos[1]-30))

		balas.coldown()

		pygame.display.update()


main()
