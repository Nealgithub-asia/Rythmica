import pygame
from game import randirection, beatTime

def resize(image, width, height):
    return pygame.transform.scale(image, (width, height))    

def draw_player():
    screen.blit(playerLoad, ( (screenWidth-playerWidth)//2, (screenHeight-playerHeight)//2) )

def draw_ring():
    ring=pygame.draw.circle(screen, "white" , screenMiddle, ringRadius, ringWidth)
    #    pygame.draw.circle(surface, color  , center      , radius    , width)

pygame.init()


screenWidth, screenHeight=1920,1080
screenMiddle=[screenWidth//2, screenHeight//2] 
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock=pygame.time.Clock()

caption= pygame.display.set_caption("Rythmica")

iconLoad = pygame.image.load("./assets/logo/rythmica.png")
icon = pygame.display.set_icon(iconLoad)

playerLoad = pygame.image.load("./assets/entities/player.png") 
playerWidth, playerHeight=100,100
playerLoad= resize(playerLoad,playerWidth,playerHeight)

objectLoad= pygame.image.load("./assets/entities/player.png")
objectWidth, objectHeight=100,100
objectLoad= resize(objectLoad,objectWidth,objectHeight)

ringRadius=200
ringWidth=30
rectLeft= pygame.Rect((screenMiddle[0] - ringRadius), screenMiddle[1], ringWidth, ringWidth)
rectRight= pygame.Rect((screenMiddle[0] + ringRadius),screenMiddle[1], ringWidth, ringWidth)
rectTop= pygame.Rect(screenMiddle[0],(screenMiddle[1]-ringRadius), ringWidth, ringWidth)
rectBottom= pygame.Rect(screenMiddle[0],(screenMiddle[1]+ringRadius), ringWidth, ringWidth)


speed=5

#game loop
running=True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False
        
        #key presses
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
    draw_player()
    draw_ring()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
