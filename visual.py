import pygame
from game import randirection

def resize(name, width, height):
    return pygame.transform.scale(name, (width, height))    

def player(): #render
    screen.blit(playerLoad, ( (x-playerWidth)/2, (y-playerHeight)/2) )

pygame.init()

x,y=1920,1080
screen = pygame.display.set_mode((x,y))

caption= pygame.display.set_caption("Rythmica")

iconLoad = pygame.image.load("./assets/logo/rythmica.png")
icon = pygame.display.set_icon(iconLoad)

playerLoad = pygame.image.load("./assets/entities/player.png") 
playerWidth, playerHeight=100,100
resize(playerLoad,playerWidth,playerHeight)

objectLoad=  pygame.image.load("./assets/entities/player.png")
objectWidth, objectHeight=100,100
resize(objectLoad,30,30)

#game loop
running=True
while running:
    for event in pygame.event.get():

        #game quit
        if event.type == pygame.QUIT:
            running=False
        
        #key counter
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
                pass
            if event.key == pygame.K_RIGHT:
                
                pass
            if event.key == pygame.K_UP:
                
                pass
            if event.key == pygame.K_DOWN:
                
                pass


    screen.fill((0,0,0))

    player()
    
    pygame.display.update()
