from telnetlib import GA
import pygame
import random
import time
WIDTH, HEIGHT = 900,600
BG = (255,255,255)
BLACK=(0,0,0)

FPS=60
maxhealth=3
pygame.font.init()
pygame.mixer.init()

SCORE_FONT = pygame.font.SysFont('comicsans',32)
HIGH_FONT= pygame.font.SysFont('comicsans',16)

N_VELOCITY=5
S_VELOCITY=6.5
A_VELOCITY=5

GAME = pygame.display.set_mode((900,600))

BACK = pygame.image.load("Assets/jungle.jpeg")
BACK = pygame.transform.scale(BACK,(WIDTH,HEIGHT))

GAMEOVER = pygame.font.SysFont('comicsans',64)

NUT = pygame.image.load("Assets/nut.png")
NUT = pygame.transform.scale(NUT,(45,45))
BANANA = pygame.image.load("Assets/banana.png")
BANANA = pygame.transform.scale(BANANA,(70,55))

RED = pygame.image.load("Assets/red.png")
RED = pygame.transform.scale(RED,(35,35))
HALF = pygame.image.load("Assets/half.png")
HALF = pygame.transform.scale(HALF,(35,35))
WHITE = pygame.image.load("Assets/white.png")
WHITE = pygame.transform.scale(WHITE,(35,35))

SQUIRREL=pygame.image.load("Assets/squirrel.png")
SQUIRREL=pygame.transform.scale(SQUIRREL,(90,108))

NUT_COLLECTED = pygame.USEREVENT +1
BANANA_COLLECTED=pygame.USEREVENT +1

def draw(squirrel,nuts,bananas,SCORE,hearts,death):
    GAME.blit(BACK,(0,0))
    for nut in nuts:
        GAME.blit(NUT,(nut.x,nut.y))
    for banana in bananas:
        GAME.blit(BANANA,(banana.x,banana.y))
    GAME.blit(SQUIRREL,(squirrel.x,squirrel.y))
    
    
    score = SCORE_FONT.render("SCORE : "+str(SCORE),2,True)
    
    f = open("highscore.txt", 'r')
    highscore = f.read()
    highscore = int(highscore)


    high=HIGH_FONT.render(f"High Score : {highscore}",2,True)

    GAME.blit(score,(0,0))
    GAME.blit(high,(0,40))
    i=0
    for heart in hearts:
        pos=770+i*40
        if i<death:
            GAME.blit(WHITE,(pos,10))
        else:   
            GAME.blit(RED,(pos,10))
        i+= 1
    if death==3:
        game_over(SCORE)
    pygame.display.update()

def game_over(SCORE):
    gameover= GAMEOVER.render("GAME OVER",2,True)
    f = open("highscore.txt", 'r')
    highscore = f.read()
    highscore = int(highscore)  
    if highscore<SCORE:
        f = open("highscore.txt",'w')
        SCORE = str(SCORE)
        highscore = f.write(SCORE)
        print("Congrats you beat the High score!!!\n")
    else:
        print(f" Your score was {SCORE} and the high score is {highscore}\n")
    

    GAME.blit(gameover,(270,250))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    
def move_nut(squirrel,nut,nuts,SCORE):
    
    for nut in nuts:
        nut.y +=N_VELOCITY
        if squirrel.colliderect(nut):
            pygame.event.post(pygame.event.Event(NUT_COLLECTED))
            nut.y=1000
            SCORE+=1
            print("\nNUT : ",SCORE+1)
        elif nut.y + N_VELOCITY> 650:
            nuts.remove(nut)
            nut.y=1000
    return SCORE

def move_banana(squirrel,banana,bananas,SCORE):

    for banana in bananas:
        banana.y +=A_VELOCITY
        if squirrel.colliderect(banana):          
            pygame.event.post(pygame.event.Event(BANANA_COLLECTED))
            banana.y=1000
            SCORE-=1
            print("\nBANANA : ",SCORE-1)
            
            
            bananas.remove(banana)   
        elif  banana.y + A_VELOCITY>650:
            banana.y=1000
            bananas.remove(banana)    
    return SCORE       


def move_squirrel(keypress,squirrel):
    if (keypress[pygame.K_LEFT] and squirrel.x-S_VELOCITY>0):
        squirrel.x -= S_VELOCITY 
    if (keypress[pygame.K_RIGHT] and squirrel.x+S_VELOCITY+squirrel.width<WIDTH):
        squirrel.x += S_VELOCITY

def main():
    running = True
    clock = pygame.time.Clock()
    
    nuts=[]
    bananas=[]
    hearts=[maxhealth]
    for i in [0,maxhealth-1]:
        heart=pygame.Rect(770,10,35,35)
        hearts.append(heart)
   
    death=0
    
    SCORE = 0
    time  = 0
    
    squirrel = pygame.Rect(100,450,90,108)
    number=90
    uplim=3
    GAME.fill(BG)
    while running:
       
        loc1  = random.randrange(0,850,50)
        loc2  = random.randrange(0,850,50)

        rand = random.randint(1,uplim)
        
        nut=pygame.Rect(loc1,100,45,45)
        banana=pygame.Rect(loc2,100,70,55)
        
        time +=1
        if time == number:
            if rand==uplim:
                bananas.append(banana) 
                

            else:
                nuts.append(nut)
            time=0

            
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        keypress = pygame.key.get_pressed()

        move_squirrel(keypress,squirrel,)
        SCORE=move_nut(squirrel,nut,nuts,SCORE)
        temp=SCORE
        SCORE=move_banana(squirrel,banana,bananas,SCORE)
        if(temp>SCORE):
            death+=1
            
        draw(squirrel,nuts,bananas,SCORE,hearts,death)  
    pygame.quit()
    print("\n\n",SCORE,"\n\n")

if __name__ == '__main__':
    main()