import pygame,math,random
from pygame.locals import *
class Shoot:
	def __init__(self):
		pass
class Player():
	def __init__(self,tela):
		self.playerpos = [500,500]
		self.lado = 27
		self.tela = tela
		self.player = pygame.Rect(self.playerpos[0], self.playerpos[1], self.lado , self.lado)
		jogador = pygame.image.load('jogador23.png')
		self.jogador  = pygame.transform.scale(jogador, (50, 40))
	def movimento(self):
		tecla_pressionada = pygame.key.get_pressed()
		for event in pygame.event.get():
			if tecla_pressionada[pygame.K_a]:
				self.player.move_ip(-3,0)
			if tecla_pressionada[pygame.K_d]:
				self.player.move_ip(3,0)
			if tecla_pressionada[pygame.K_w]:
				self.player.move_ip(0,-3)
			if tecla_pressionada[pygame.K_s]:
				self.player.move_ip(0,3)
			self.playerpos = [self.player.left,self.player.top]
	def rotacao(self):
		position = pygame.mouse.get_pos()
		angle = math.atan2(position[1] - self.playerpos[1],position[0] - self.playerpos[0])
		self.playerrot = pygame.transform.rotate( self.jogador , 360 - angle * 57.2999999999999999)
		self.playerpos1 = (self.playerpos[0]-self.playerrot.get_rect().width/2,self.playerpos[1]-self.playerrot.get_rect().height/2)
		self.tela.blit(self.playerrot,(self.playerpos1[0] +13, self.playerpos1[1] + 13))
	def show(self):
		pygame.draw.rect(self.tela,(255,255,255),self.player)
def main():
	width = 1600
	height = 900
	x = FULLSCREEN
	tela = pygame.display.set_mode([width,height], x)
	pygame.display.set_caption('Cowboy History','A historia de um cowboy')
	playerdz = Player(tela)
	pygame.key.set_repeat(10,10)
	fundo = pygame.image.load('areia.png')
	fundo = pygame.transform.scale(fundo, (width, height))
	DAGGER_IMG = pygame.image.load('tiro.png')
	tiroimg = pygame.transform.scale(DAGGER_IMG,(10,10))
	daggers = []
	cooldown = 0
	
	while True:
		mouse_position = pygame.mouse.get_pos()
		# Distances to the mouse position.
		rise = mouse_position[1] - playerdz.player.centery
		run = mouse_position[0] - playerdz.player.centerx
		angle = math.atan2(rise, run)
		playerdz.show()

		tela.fill([255, 255, 255])
		tela.blit(fundo,(0,0))
		for dagger in daggers:
			tela.blit(tiroimg, (dagger[0][0], dagger[0][1]))
			dagger[0][0] += dagger[1][0]
			dagger[0][1] += dagger[1][1]
		playerdz.movimento()
		playerdz.rotacao()
		

		tecla_pressionada = pygame.key.get_pressed()
		if tecla_pressionada [K_ESCAPE]:
			pygame.quit()
			exit(0)			
		if tecla_pressionada [K_SPACE]:
			if cooldown == 0:
				print('alguma coisa')
				# Use sine and cosine to get the velocity of the projectile.
				# To make it move faster, you need to scale the velocity
				# (i.e. multiply it by a number).
				vel_x = math.cos(angle) * 20
				vel_y = math.sin(angle) * 20
				# Now rotate the original image by the negative angle (because
				# pygame's y-axis is flipped).
				dagger_img = pygame.transform.rotate(tiroimg, -math.degrees(angle))
				width, height = dagger_img.get_size()
				# The projectile data consists of position, velocity and the
				# rotated image. -width/2 and -height/2 to center them.
				daggers.append(
					[[playerdz.player.left, playerdz.player.top],  # Pos
					[vel_x, vel_y],  # Velocity
					tiroimg  # Image
					 ])
				cooldown = 10
			print(str(len(daggers)))

		if cooldown > 0:
			cooldown -= 1
		
		pygame.display.update()
main()
