from telnetlib import GA
import pygame
import random
WIDTH, HEIGHT = 900,600
BG = (255,255,255)
BLACK=(0,0,0)
FPS=60
pygame.font.init()
pygame.mixer.init()
SCORE__FONT = pygame.font.SysFont('comicsans',32)

N_VELOCITY=5
S_VELOCITY=6.5

GAME = pygame.display.set_mode((900,600))

BACK = pygame.image.load("Assets/tile.jpg")
BACK = pygame.transform.scale(BACK,(WIDTH,HEIGHT))



NUT = pygame.image.load("Assets/nut.png")
NUT = pygame.transform.scale(NUT,(50,50))

SQUIRREL=pygame.image.load("Assets/squirrel.png")
SQUIRREL=pygame.transform.scale(SQUIRREL,(110,110))

NUT_COLLECTED = pygame.USEREVENT +1

def draw(squirrel,nut,SCORE):
    GAME.blit(BACK,(0,0))
    GAME.blit(NUT,(nut.x,nut.y))
    GAME.blit(SQUIRREL,(squirrel.x,squirrel.y))
    score = SCORE__FONT.render("SCORE : "+str(SCORE),1,True)
    GAME.blit(score,(0,0))
    pygame.display.update()


def move_nut(squirrel,nut,nuts,SCORE):
    
    for nut in nuts:
        nut.y +=N_VELOCITY
        if squirrel.colliderect(nut):
            pygame.event.post(pygame.event.Event(NUT_COLLECTED))
            nut.y=1000
            nuts.remove(nut)
        elif nut.y + N_VELOCITY> 650:
            nuts.remove(nut)
            nut.y=1000




def move_squirrel(keypress,squirrel):
    if (keypress[pygame.K_LEFT] and squirrel.x-S_VELOCITY>0):
        squirrel.x -= S_VELOCITY 
    if (keypress[pygame.K_RIGHT] and squirrel.x+S_VELOCITY+squirrel.width<WIDTH):
        squirrel.x += S_VELOCITY 

def main():
    running = True
    clock = pygame.time.Clock()
    SCORE =0
    nuts=[]
    time = 0
    squirrel = pygame.Rect(100,450,110,110)
    
    GAME.fill(BG)
    while running:
        loc=  random.randrange(0,850,50)
        number=100
        if time %number <1:
            nut = pygame.Rect(loc,100,50,50)
            nuts.append(nut)
            if time>number:
                time/=number
        time +=1
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == NUT_COLLECTED:
                SCORE +=1
        keypress = pygame.key.get_pressed()
        move_squirrel(keypress,squirrel,)
        move_nut(squirrel,nut,nuts,SCORE)
        draw(squirrel,nut,SCORE)  
    pygame.quit()
    print("\n\n",SCORE,"\n\n")
if __name__ == '__main__':
    main()
