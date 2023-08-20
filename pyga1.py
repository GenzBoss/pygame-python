import pygame
from pygame.locals import *

pygame.init()

gamewindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Adventure Game")
black= (0,0,0)
white=(255,255,255)
img=pygame.image.load("spritel.png")

def sprite(x,y):
    gamewindow.blit(img, (x,y))

x = (0.45)
y = (0.8)

xchange=0
imgspeed=0
    


running=True

while running:
    
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
            pygame.quit()
    
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            xchange=-5
        elif event.key == pygame.K_RIGHT:
            xchange=5
    if event.type== pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            xchange=0
    
    x +=xchange

    gamewindow.fill(white)
    sprite(x, y)
    pygame.display.update()

pygame.quit()

    

    

