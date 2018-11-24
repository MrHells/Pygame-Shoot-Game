#https://stackoverflow.com/questions/44465783/how-to-make-arrow-shoot-in-direction-of-mouse
#site para ver

import math, random,pygame,base64
from pygame.locals import *

class Actor(object):

    surf = None

    def __init__(self):
        self.x, self.y = (0, 0)
        self.speed, self.angle = 1.7, 0
        self.target_vector = [0, 0]

    @property
    def img(self):
        if not self.surf:
            self.surf = get_image()
        return self.surf


    @property
    def pos(self):
        return self.x, self.y

    @property
    def int_pos(self):
        return map(int, self.pos)

    @property
    def center_pos(self):
        return [a-16 for a in self.int_pos]

    def update(self):
        if self.speed == 0:
            return

        # apply speed to target_vector
        move_vector = [c * self.speed for c in normalize(self.target_vector)]

        # update position by adding the position vector to the movment vector
        self.x, self.y = add(self.pos, move_vector)

    def draw(self, s):
        # substract 90 from angle because the image is actually
        # an arrow already rotated by 90 degree
        s.blit(rot_center(self.img, self.angle-90), self.center_pos)


def direcao(girado,posicaoDoGirado):
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - posicaoDoGirado[1],position[0] - posicaoDoGirado[0])
    playerrot = pygame.transform.rotate(girado,360-angle*57.29)
    playerpos1 = (posicaoDoGirado[0]-playerrot.get_rect().width/2,posicaoDoGirado[1]-playerrot.get_rect().height/2)
    #tela.blit(playerrot,playerpos1)
    return playerrot,playerpos1



def colision(player1,parede,tela,cor_parede,lado_parede_x,lado_parede_y):
            x = 2
            cor_pared = (255,255,222)
            posicao_parede_x = parede.left
            posicao_parede_y = parede.top


            parede_top = pygame.Rect(posicao_parede_x +2 ,posicao_parede_y,lado_parede_x-4,(lado_parede_y+1)-lado_parede_y)
            pygame.draw.rect(tela,cor_pared,parede_top)
            parede_bot = pygame.Rect(posicao_parede_x +2 ,posicao_parede_y+lado_parede_x,lado_parede_x-4,(lado_parede_y+1)-lado_parede_y)
            pygame.draw.rect(tela,cor_pared, parede_bot)

            parede_left = pygame.Rect(posicao_parede_x,posicao_parede_y+1,(lado_parede_x+1)-lado_parede_x,lado_parede_y-1)
            pygame.draw.rect(tela,cor_parede,parede_left)

            parede_right = pygame.Rect(245,155,5,90)
            pygame.draw.rect(tela,cor_parede,parede_right)
            if player1.colliderect(parede_top):
                player1.move_ip(0,-x)

            if player1.colliderect(parede_left):
                player1.move_ip(-x,0)

            if player1.colliderect(parede_right):
                player1.move_ip(x ,0)

            if player1.colliderect(parede_bot):
                player1.move_ip(0,x)
            pygame.mixer.music.load('Punch_03.wav')
            pygame.mixer.music.play()

pygame.init()

width = 1365
height = 765
x = FULLSCREEN
tela = pygame.display.set_mode([width,height],x)
pygame.display.set_caption('Cowboy History','A historia de um cowboy')

fps = pygame.time.Clock()

acc = [0,0]
arrows =[]
balaimg = pygame.image.load('tiro.png').convert()
balaimg = pygame.transform.scale(tela,(10,10))
blx = pygame.Rect(0,0,10,10)
fundo = pygame.image.load('areia.png')
fundo = pygame.transform.scale(fundo, (width, height))


lado = 34
mov = 2
playerpos = [500,500]

player = pygame.Rect(playerpos[0], playerpos[1], lado , lado)
jogador = pygame.image.load('Player.png')
jogador  = pygame.transform.scale(jogador, (40, 30))

lado_parede_x = 10
lado_parede_y = height
parede_esquerda = pygame.Rect(0,0,lado_parede_x,lado_parede_y)



lado_parede_x = 10
lado_parede_y = height
parede_direita = pygame.Rect(width-10,0,lado_parede_x,lado_parede_y)

lado_parede_x = width
lado_parede_y = 10
parede_cima = pygame.Rect(0,0,lado_parede_x,lado_parede_y)
#o
lado_parede_x = width
lado_parede_y = 10
parede_baixo = pygame.Rect(0,height-10,lado_parede_x,lado_parede_y)
mira = pygame.image.load('mira.png')
mira = pygame.transform.scale(mira,(60,60))
pygame.mouse.set_visible(False)

tiroRec = pygame.Rect(playerpos[0],playerpos[1],10,10)
tiroRecPos =[playerpos[0],playerpos[1]]
#o
#tiro = pygame.image.load('tiro.png')
#tiro = pygame.transform.scale(tiro,(10,10))

pygame.key.set_repeat(30,30)

parede_teste = pygame.Rect(500,500,100,100)

jogador = Actor()
jogador.x, jogador.y, jogador.speed = 134, 134, 0
actors = [jogador]


#balaimg = pygame.Rect(playerpos[0],playerpos[1],10,10)

while True:
    tela.fill((2,2,2))
    #tela.fill((255,255,255))
    fps.tick(60)

    tecla_pressionada = pygame.key.get_pressed()
    p = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if tecla_pressionada [K_ESCAPE]:
            pygame.quit()
            exit(0)
        if tecla_pressionada[pygame.K_a]:
            playerpos[0] -= 5
        if tecla_pressionada[pygame.K_d]:
            playerpos[0] += 5
        if tecla_pressionada[pygame.K_w]:
            playerpos[1] -= 5
        if tecla_pressionada[pygame.K_s]:
            playerpos[1] += 5
        if tecla_pressionada[pygame.K_SPACE]:
            posicao = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(posicao[1]-(playerpos[1]), posicao[0] -(playerpos[0])),playerpos1[0],playerpos1[1]])
    player.left = playerpos[0] - 17
    player.top = playerpos[1] - 17
    #pygame.draw.rect(tela,(255,255,255),player)
    tela.blit(fundo,(0,0))


    tela.blit(mira,(p[0]-30,p[1]-30))

    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - playerpos[1],position[0] - playerpos[0])
    playerrot = pygame.transform.rotate(jogador,360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
    tela.blit(playerrot,playerpos1)
    for tiro in arrows:
        index = 0
        velx = math.cos(tiro[0]) *10
        vely = math.sin(tiro[0]) *10
        tiro[1] += velx
        tiro[2] += vely
        print('tero')
        if tiro[1] < -64 or tiro[1] > width or tiro[2] > -64 or tiro[2] > height :
            arrows.pop(index)
        index += 1
        print('index')
        for projetil in arrows:
            bala = pygame.transform.rotate(balaimg ,360 - projetil[0]*57.29)
            tela.blit(bala,(projetil[1], projetil[2]))
            print('hahaha')
        for passo in arrows:
            andar = arrows[passo]
            andar[0] = andar[0] + velx
            andar[1] = andar[1] + vely
            tela.blit(andar)
            arrows[passo] = andar




#o




            print('i')

#o
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    #wtela.blit(fundo,(0,0))
    pygame.draw.rect(tela,(0,0,255),blx)

    for bullet in arrows:
        tela.blit(balaimg, pygame.Rect(bullet[0], bullet [1], 10, 10))
        print('jujuasasa')

    pygame.draw.rect(tela,(0,0,255),parede_esquerda)
    pygame.draw.rect(tela,(255,255,255),parede_direita)
    pygame.draw.rect(tela,(255,0,0),parede_cima)
    pygame.draw.rect(tela,(0,255,0),parede_baixo)


    #tela.blit(jogador,(playerpos[0],playerpos[1]))
#    goBALA(playerpos,balas,tiroRec,tiroRecPos,tiro)
    pygame.display.flip()





#o




