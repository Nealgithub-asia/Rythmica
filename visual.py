import pygame
from game import beatDirection,beatTime,randirection

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

        self.hitbox= pygame.Rect(screenMiddlex-self.hWidth//2, screenMiddley-self.hHeight//2, self.width, self.height)
class game_object:
    def __init__(self ,image , width, height, hWidth, hHeight):
        #self.path=path
        self.width=width
        self.height=height
        
        self.hWidth=hWidth
        self.hHeight=hHeight

        #self.image=load(path)
        #self.image=resize(self.image, self.width, self.height)  
        self.image=image
        
        self.update_hitbox(hWidth, hHeight)

    def update_size(self, width, height):
        self.width=width
        self.height=height
        self.image=resize(self.image, self.width, self.height)

        return self.image
        
    def update_hitbox(self, hWidth, hHeight):
        self.hWidth=hWidth
        self.hHeight=hHeight
        
        center_x_start = screenMiddlex - (self.hWidth // 2)
        center_y_start = screenMiddley - (self.hHeight // 2)

        self.leftHitbox = pygame.Rect(0, center_y_start, self.hWidth, self.hHeight)        
        self.rightHitbox = pygame.Rect(screenWidth - self.hWidth, center_y_start, self.hWidth, self.hHeight)
        self.topHitbox = pygame.Rect(center_x_start, 0, self.hWidth, self.hHeight)
        self.bottomHitbox = pygame.Rect(center_x_start, screenHeight - self.hHeight, self.hWidth, self.hHeight)

    def update(self, direction):
        if(direction=="left"):
            if(self.leftHitbox.x < screenMiddlex):
                self.leftHitbox.x+=5
                screen.blit(self.image, (self.leftHitbox.x, self.leftHitbox.y))
        elif(direction=="right"):
            if(self.rightHitbox.x > screenMiddlex):
                self.rightHitbox.x-=5
                screen.blit(self.image, (self.rightHitbox.x, self.rightHitbox.y))
        elif(direction=="top"):
            if(self.topHitbox.y < screenMiddley):
                self.topHitbox.y+=5
                screen.blit(self.image, (self.topHitbox.x, self.topHitbox.y))
        elif(direction=="bottom"):
            if(self.bottomHitbox.y > screenMiddley):
                self.bottomHitbox.y-=5
                screen.blit(self.image, (self.bottomHitbox.x, self.bottomHitbox.y))
                

def load(asset):
    return pygame.image.load(asset)   

def resize(image, width, height):
    return pygame.transform.scale(image, (width, height))    

def draw_ring(color):
    ring=pygame.draw.circle(screen, color , screenMiddle, ringRadius, ringWidth)
    #    pygame.draw.circle(surface, color  , center      , radius    , width)

def draw_ring_hitbox(side):
    if(side=="left"):
        pygame.draw.rect(screen, "red", rectLeft, 2)
    elif(side=="right"):
        pygame.draw.rect(screen, "red", rectRight, 2)
    elif(side=="top"):
        pygame.draw.rect(screen, "red", rectTop, 2) 
    elif(side=="bottom"):
        pygame.draw.rect(screen, "red", rectBottom, 2)

def draw_player():
    screen.blit(player.image , ( (screenWidth-player.width)//2, (screenHeight-player.height)//2) )

pygame.init()

screenWidth, screenHeight=1080,1080
screenMiddle=[screenWidth//2, screenHeight//2]
screenMiddlex=screenWidth//2
screenMiddley=screenHeight//2 
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock=pygame.time.Clock()

caption= pygame.display.set_caption("Rythmica")

iconLoad = pygame.image.load("./assets/logo/rythmica.png")
icon = pygame.display.set_icon(iconLoad)


player=game_player("./assets/entities/player.png", 100, 100, 100, 100 )

objectImage=resize(load("./assets/entities/fireball.png"), 30, 30)
object=game_object(objectImage, 30, 30, 30, 30)


ringRadius=200
ringWidth=30 #ring width is the same as rectangle hitbox width

rectLeft= pygame.Rect((screenMiddlex - ringRadius),( screenMiddley - ringWidth//2), ringWidth, ringWidth)
rectRight= pygame.Rect((screenMiddlex + ringRadius - ringWidth),(screenMiddley - ringWidth//2), ringWidth, ringWidth)
rectTop= pygame.Rect((screenMiddlex - ringWidth//2),(screenMiddley-ringRadius), ringWidth, ringWidth)
rectBottom= pygame.Rect((screenMiddlex - ringWidth//2),(screenMiddley + ringRadius - ringWidth), ringWidth, ringWidth)

speed=5

clock = pygame.time.Clock()
actionDuration=500 #mili seconds
actionInitialize=0 #will get ticks till 1000

timer={"left":0,"right":0,"top":0,"bottom":0}
#game loop
activeobjects=[]
i=0
running=True
while running:
    currentTime=pygame.time.get_ticks()

    screen.fill((0,0,0))
    draw_player()
    draw_ring("blue")

    
    if(i<len(beatTime) and currentTime >= beatTime[i]*1000): 
        for direction in randirection[i]:
            newObj=game_object(objectImage, 30, 30, 30, 30)
            if direction=="left": activeobjects.append((newObj,"left"))
            elif direction=="right": activeobjects.append((newObj,"right"))
            elif direction=="top": activeobjects.append((newObj,"top"))
            elif direction=="bottom": activeobjects.append((newObj,"bottom"))
        i+=1
    
    for obj in reversed(activeobjects):
        
        rect,dir=obj
        
        rect.update(direction=dir)        

        if dir=="left" and rect.leftHitbox.x>=screenMiddlex:
            activeobjects.remove(obj)
        elif dir=="right" and rect.rightHitbox.x<=screenMiddlex:
            activeobjects.remove(obj)
        elif dir=="top" and rect.topHitbox.y>=screenMiddley:
            activeobjects.remove(obj)
        elif dir=="bottom" and rect.bottomHitbox.y<=screenMiddley:
            activeobjects.remove(obj)

        
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False
        #key presses

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running=False

            if event.key == pygame.K_LEFT: timer["left"]=pygame.time.get_ticks()
            if event.key == pygame.K_RIGHT: timer["right"]=pygame.time.get_ticks()
            if event.key == pygame.K_UP: timer["top"]=pygame.time.get_ticks()
            if event.key == pygame.K_DOWN: timer["bottom"]=pygame.time.get_ticks()

    for direction in timer:
        startTime=timer[direction]
        if startTime > 0 and (currentTime - startTime < actionDuration):
            draw_ring_hitbox(direction)
        elif startTime > actionDuration:
            timer[direction] = 0    

    pygame.display.update()
    clock.tick(60)

pygame.quit()
