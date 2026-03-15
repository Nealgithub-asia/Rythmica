import pygame
from game import randirection

class game_player:
    def __init__(self ,path , width, height, hWidth, hHeight):
        self.path=path

        self.width=width
        self.height=height

        self.hWidth=hWidth
        self.hHeight=hHeight

        self.image=load(self.path)
        self.image=resize(self.image, self.width, self.height)  

        self.update_hitbox(hWidth, hHeight)

    def update_size(self, width, height):
        self.width=width
        self.height=height
        self.image=resize(self.image, self.width, self.height)
        return self.image
        
    def update_hitbox(self, hWidth, hHeight):
        self.hWidth=hWidth
        self.hHeight=hHeight

        self.hitbox= pygame.Rect(screenMiddle[0]-self.hWidth//2, screenMiddle[1]-self.hHeight//2, self.width, self.height)
class game_object:
    def __init__(self ,path , width, height, hWidth, hHeight):
        self.path=path
        self.width=width
        self.height=height
        self.hWidth=hWidth
        self.hHeight=hHeight

        self.image=load(path)
        self.image=resize(self.image, self.width, self.height)  

        self.update_hitbox(hWidth, hHeight)

    def update_size(self, width, height):
        self.width=width
        self.height=height
        self.image=resize(self.image, self.width, self.height)

        return self.image
        
    def update_hitbox(self, hWidth, hHeight):
        self.hWidth=hWidth
        self.hHeight=hHeight
        
        center_x_start = screenMiddle[0] - (self.hWidth // 2)
        center_y_start = screenMiddle[1] - (self.hHeight // 2)

        self.leftHitbox = pygame.Rect(0, center_y_start, self.hWidth, self.hHeight)        
        self.rightHitbox = pygame.Rect(screenWidth - self.hWidth, center_y_start, self.hWidth, self.hHeight)
        self.topHitbox = pygame.Rect(center_x_start, 0, self.hWidth, self.hHeight)
        self.bottomHitbox = pygame.Rect(center_x_start, screenHeight - self.hHeight, self.hWidth, self.hHeight)    

def load(asset):
    return pygame.image.load(asset)   

def resize(image, width, height):
    return pygame.transform.scale(image, (width, height))    

def draw_ring(color):
    ring=pygame.draw.circle(screen, color , screenMiddle, ringRadius, ringWidth)
    #    pygame.draw.circle(surface, color  , center      , radius    , width)

def draw_player():
    screen.blit(player.image , ( (screenWidth-player.width)//2, (screenHeight-player.height)//2) )

pygame.init()


screenWidth, screenHeight=1920,1080
screenMiddle=[screenWidth//2, screenHeight//2] 
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock=pygame.time.Clock()

caption= pygame.display.set_caption("Rythmica")

iconLoad = pygame.image.load("./assets/logo/rythmica.png")
icon = pygame.display.set_icon(iconLoad)


player=game_player("./assets/entities/player.png", 100, 100, 100, 100 )

object=game_object("./assets/entities/player.png", 30, 30, 30, 30)

ringRadius=200
ringWidth=30

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
    draw_ring("green")
    pygame.display.update()
    clock.tick(60)

pygame.quit()
