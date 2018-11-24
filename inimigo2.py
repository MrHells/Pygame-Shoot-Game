import math, random,pygame
from pygame.locals import *
from random import randint

pygame.init()

def mais_vida():
	print('mais vida')
	
def mais_bala():
	print('mais bala')
	
def mais_moeda():
	print('mais moeda')

def bala_tripla():
	print('bala tripla')
	
def infinite_bullet():
	print('infinite bullet')

telacheia=FULLSCREEN
branco = (255,255,255)
width = 1600
height = 900
tela= pygame.display.set_mode([width,height], telacheia)


playerpos = [10,10]
lado = 40
personagem = pygame.Rect(playerpos[0],playerpos[1],lado,lado)
fps = pygame.time.Clock()


enemypos = [1200,500]
inimigo = pygame.Rect(enemypos[0],enemypos[1],lado,lado)
inimigo_vivo = True


HP = 3
vida = pygame.image.load('vida.png')
vida = pygame.transform.scale(vida, (50, 50))
pos_vida = [1,1]


ladobonus = 18
#bonus = pygame.Rect(-200,-200,ladobonus,ladobonus)
bonuses = []

drop_boole = True
drop_aleatorio = randint(0,0)

if drop_aleatorio == 0:
	drop_player = pygame.image.load('vida.png')
	drop_player = pygame.transform.scale(drop_player,(30,30))
	
elif drop_aleatorio == 1:
	drop_player = pygame.image.load('bala.png')
	drop_player = pygame.transform.scale(drop_player,(30,30))
elif drop_aleatorio == 2:
	drop_player = pygame.image.load('bala.png')
	drop_player = pygame.transform.scale(drop_player,(30,30))
elif drop_aleatorio == 3:
	drop_player = pygame.image.load('moeda.png')
	drop_player = pygame.transform.scale(drop_player,(30,30))
elif drop_aleatorio ==4:
	drop_player = pygame.image.load('moeda.png')
	drop_player = pygame.transform.scale(drop_player,(30,30))
elif drop_aleatorio == 5:
	drop_player = pygame.image.load('balatripla.png')
	drop_player = pygame.transform.scale(drop_player,(30,30))
elif drop_aleatorio == 6:
	drop_player = pygame.image.load('infinitebullet.png')
	drop_player = pygame.transform.scale(drop_player,(30,30))
elif drop_aleatorio == 7:
	drop_boole = False

player = pygame.image.load('parede.png')
player = pygame.transform.scale(player,(50,50))
pygame.key.set_repeat(30,30)

vel = 5
veli = vel -3
c = False


while True:
	fps.tick(60)
	tecla_pressionada = pygame.key.get_pressed()
	tela.fill((160,160,160))
	tela.blit(vida,(pos_vida))
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
		
		if personagem.left <= 0:
			personagem.left += vel
		if personagem.right >= width:
			personagem.right -= vel
		if personagem.top <= 0:
			personagem.top += vel
		if personagem.bottom >= height:
			personagem.bottom -= vel


#inimigo:
	if inimigo_vivo == True:
		if inimigo.left < personagem.left:
			inimigo.left +=veli
				
		if inimigo.top < personagem.top:
			inimigo.top +=veli
				
		if inimigo.left > personagem.left:
			inimigo.left -=veli
			
		if inimigo.top > personagem.top:
			inimigo.top -=veli
	else:
		inimigo.left = -100
		inimigo.top = -100
			
	if personagem.colliderect(inimigo):
		c = True
		tela.fill((255,0,0))
		inimigo_vivo = False
		HP -= 1
		bonuspos = [inimigo.left + 100,inimigo.top + 100]
		bonuses.append(bonuspos)
		'''if HP == 0:
			break'''
		
	pygame.draw.rect(tela,(255,255,255),personagem)
	
	if drop_boole == True:
# MUDEI ISSO Q N MUDA EM NADA KKKKKK 
		bonus = pygame.Rect(-200,-200,ladobonus,ladobonus)
		for procurabonus in bonuses:	
			bonus.left = procurabonus[0]
			bonus.top = procurabonus[1]
			pygame.draw.rect(tela,(0,0,0),bonus)
		if c == True:
			tela.blit(drop_player,(bonuspos[0]-10,bonuspos[1]-100))
		
	if personagem.colliderect(bonus):
		bonus.left = -100
		bonus.top = -100
		
		if drop_aleatorio == 0:
			mais_vida()
		elif drop_aleatorio == 1:
			mais_bala()
		elif drop_aleatorio == 2:
			mais_bala()
		elif drop_aleatorio == 3:
			mais_moeda()
		elif drop_aleatorio == 4:
			mais_moeda()
		elif drop_aleatorio == 5:
			bala_tripla()
		elif drop_aleatorio == 6:
			infinite_bullet()
			
	
	pygame.draw.rect(tela,(0,0,0),inimigo)
	posx = inimigo.left
	posy = inimigo.top

		
	tela.blit(player,(personagem.left-6 , personagem.top-6))

	pygame.display.update()
	
pygame.display.quit()
