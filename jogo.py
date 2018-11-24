
import pygame
from pygame.locals import *
pygame.init()
try:
    comprimento_ecra = 1300
    altura_ecra = 700
    ecra = pygame.display.set_mode((comprimento_ecra, altura_ecra))
    fps = pygame.time.Clock()
except:
    print('Não deu')
vermelho = (255, 0, 0)
fundo = (0, 0, 255)

comprimento_ecra = 1300
altura_ecra = 700
ecra = pygame.display.set_mode((comprimento_ecra, altura_ecra))

pygame.mixer.music.load('undone.mp3')
pygame.mixer.music.play()
pygame.event.wait()

raio_circulo = 20

xpos = 100
ypos = 100
xpos_bala = xpos
ypos_bala = ypos

player_pos =(ecra,(xpos, ypos))
movimento = 10
mvimento_bala = 40
pygame.display.update()

pygame.key.set_repeat(1, 1)
class player ():
    def __init__(self,screen):
        self.screen        = screen
        self.screen_rect   = screen.get_react()
        self.image         = pygame.image.load("Player.png")
        self.rect          = self.image.get_rect()
        self.rect.centerx  = self.screen_rect.centerx
        self.rect.bottom   = self.screen_rect.bottom
    def desenho (self):
        self.screen.blint(self.image, self.rect)


while True:
    for event in pygame.event.get():
        pass
    event = pygame.event.wait()
    tecla_pressionada = pygame.key.get_pressed()

    if tecla_pressionada[K_a]:
        xpos -= movimento
        xpos_bala = xpos
    if tecla_pressionada[K_d]:
        xpos += movimento
        xpos_bala = xpos
    if tecla_pressionada[K_w]:
        ypos -= movimento
        ypos_bala = ypos
    if tecla_pressionada[K_s]:
        ypos += movimento
        ypos_bala = ypos


    if tecla_pressionada[K_UP]:
        xpos_bala -= movimento_bala

    if tecla_pressionada[K_DOWN]:
        xpos_bala += movimento_bala

    if tecla_pressionada[K_LEFT]:
        ypos_bala -= movimento_bala

    if tecla_pressionada[K_RIGHT]:
        ypos_bala += movimento_bala

    if event.type == pygame.QUIT:
        break

    ecra.fill(fundo)
    #circulo = pygame.draw.circle(ecra, vermelho, (xpos, ypos), raio_circulo)
    player = pygame.image.load("Player1.png")
    pygame.font.init()
    player_size = player.get_size()
    pygame.display.update()
'''	if event_saida True()
        pygame.quit()
        quit()'''
'''import pygame
from pygame.locals import *
    
testeinicializacao = pygame.init()
print(testeinicializacao)
display_width = 800
display_height = 600
tela = pygame.display.set_mode((display_width,display_height))
pygame.display.update()
if k_key('up')
input()'''
