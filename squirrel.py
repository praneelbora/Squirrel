from telnetlib import GA
import pygame

WIDTH, HEIGHT = 900,600
BG = (255,255,255)
BLACK=(0,0,0)

VELOCITY=5

GAME = pygame.display.set_mode((900,600))

BACK = pygame.image.load("Assets/tile.jpg")
BACK = pygame.transform.scale(BACK,(WIDTH,HEIGHT))

SCORE =0

NUT = pygame.image.load("Assets/nut.png")
NUT = pygame.transform.scale(NUT,(50,50))

SQUIRREL=pygame.image.load("Assets/squirrel.png")
SQUIRREL=pygame.transform.scale(SQUIRREL,(110,110))

NUT_COLLECTED = pygame.USEREVENT +1

def draw(squirrel,nut):
    GAME.blit(BACK,(0,0))
    
    GAME.blit(NUT,(nut.x,nut.y))

    GAME.blit(SQUIRREL,(squirrel.x,squirrel.y))
    pygame.display.update()


def move_nut(squirrel,nut):
    nut.y +=VELOCITY
    if squirrel.colliderect(nut):
        pygame.event.post(pygame.event.Event(NUT_COLLECTED))


def move_squirrel(keypress,squirrel):
    if (keypress[pygame.K_LEFT] and squirrel.x-VELOCITY>0):
        squirrel.x -= VELOCITY 
    if (keypress[pygame.K_RIGHT] and squirrel.x+VELOCITY+squirrel.width<WIDTH):
        squirrel.x += VELOCITY 

def main():
    running = True
    clock = pygame.time.Clock()

    squirrel = pygame.Rect(100,450,110,110)
    nut = pygame.Rect(100,100,50,50)
    GAME.fill(BG)
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        if event.type == NUT_COLLECTED:
            SCORE +=1
        keypress = pygame.key.get_pressed()
        move_squirrel(keypress,squirrel)
        move_nut(squirrel,nut)
        draw(squirrel,nut)  
    pygame.quit()
if __name__ == '__main__':
    main()
