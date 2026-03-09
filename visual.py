import pygame

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
running=True

#title and icon
caption= pygame.display.set_caption("Rythmica")
iconSurface = pygame.image.load("./assets/logo/rythmica.png")
icon = pygame.display.set_icon(iconSurface)

playerEntity = pygame.image.load("./assets/entities/player.png") 

def player():
    screen.blit(playerEntity, (50,50))

#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    screen.fill((0,0,0))
    
    player()

    pygame.display.update()
