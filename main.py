#The Islannd survival
import pygame
import time
import random
import math


pygame.init()

display_width = 800
display_height = 800
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)

block_width = 100
block_height = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Island Survial')
clock = pygame.time.Clock()

grassImg = pygame.image.load('grass.png')
woodImg = pygame.image.load('wood.png')
stoneImg = pygame.image.load('stone.png')
waterImg = pygame.image.load('water.png')
homeImg = pygame.image.load('home.png')
fireImg = pygame.image.load('fire.png')
gameIcon = pygame.image.load('grass.png')

pygame.display.set_icon(gameIcon)

pause = False

def Wood(Wcount):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Wood: "+str(Wcount), True, black)
    gameDisplay.blit(text,(0,0))
def Stone(scount):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Stone: "+str(scount), True, black)
    gameDisplay.blit(text,(0,25))
def craft():
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Press 1 To craft small home", True, black)
    gameDisplay.blit(text,(0,45))

def cw():
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("You Need To Builid Home ", True, black)
    gameDisplay.blit(text,(0,45))
def fr():
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("You Need To Build Fire ", True, black)
    gameDisplay.blit(text,(0,45))
    

def grass(x3,y3):
    gameDisplay.blit(grassImg,(x3,y3))
def stone(x1,y1):
    gameDisplay.blit(stoneImg,(x1,y1))
def wood(x2,y2):
    gameDisplay.blit(woodImg,(x2,y2))
def water(x,y):
    gameDisplay.blit(waterImg,(x,y))
def home(x4,y4):
    gameDisplay.blit(homeImg,(x4,y4))
def fire(x5,y5):
    gameDisplay.blit(fireImg,(x5,y5))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects(" Island Survial ", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)




def game_loop():
    global pause

    h = 0
    wv = 80
    sv = 50
    s = 0
    w = 0
    x = 0
    y = 0
    x3 = 100
    y3 = 100
    y_9 = 0
    x_9 = 800
    x_1 = x + 100
    x_2 = x_1 + 100
    x_3 = x_2 + 100
    x_4 = x_3 + 100
    x_5 = x_4 + 100
    x_6 = x_5 + 100
    x_7 = x_6 + 100
    x_8 = x_7 + 100
    y_1 = y + 100
    y_2 = y_1 + 100
    y_3 = y_2 + 100
    y_4 = y_3 + 100
    y_5 = y_4 + 100
    y_6 = y_5 + 100
    y_7 = y_6 + 100
    y_8 = y_7 + 100
    x3_1 = x3 + 100
    x3_2 = x3_1 + 100
    x3_3 = x3_2 + 100
    x3_4 = x3_3 + 100
    x3_5 = x3_4 + 100
    x3_6 = x3_5 + 100
 
 
    wcount = 2500

    scount = 3800
    gameExit = False
 
    while not gameExit:
        wv = 80
        sv = 50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                if event.key == pygame.K_w:
                    w = 1
                if event.key == pygame.K_s:
                    s = 1

        if w == 1:
            wcount += 1
            w = 0
        if s == 1:
            scount += 1
            s = 0
            

        
        water(x,y)
        water(x_1,y)
        water(x_2,y)
        water(x_3,y)
        water(x_4,y)
        water(x_5,y)
        water(x_6,y)
        water(x_7,y)
        water(x_8,y)
        water(x,y_1)
        water(x,y_2)
        water(x,y_3)
        water(x,y_4)
        water(x,y_5)
        water(x,y_6)
        water(x,y_7)
        water(x,y_8)
        grass(x3,y3)
        grass(x3_1,y3)
        grass(x3_2,y3)
        grass(x3_3,y3)
        grass(x3_4,y3)
        grass(x3_5,y3)
        water(700,100)
        water(700,200)
        water(700,300)
        water(700,400)
        water(700,500)
        water(700,600)
        water(700,700)
        water(700,800)
        water(0,700)
        water(100,700)
        water(200,700)
        water(300,700)
        water(400,700)
        water(500,700)
        water(600,700)
        water(700,700)
        grass(x3_1,200)
        grass(x3_2,200)
        grass(x3_3,200)
        grass(x3_4,200)
        wood(x3_5,200)
        stone(100,200)
        grass(200,300)
        wood(300,300)
        grass(400,300)
        grass(500,300)
        grass(600,300)
        grass(100,300)
        grass(100,400)
        grass(200,400)
        grass(300,400)
        grass(400,400)
        grass(500,400)
        grass(600,400)
        grass(100,400)
        grass(100,500)
        grass(200,500)
        grass(300,500)
        grass(400,500)
        grass(500,500)
        grass(600,500)
        grass(100,500)
        grass(100,600)
        grass(200,600)
        grass(300,600)
        grass(400,600)
        grass(500,600)
        grass(600,600)
        grass(100,600)


        Stone(scount)
        Wood(wcount)
        if wcount > 49 and scount > 79 and h == 0:
            craft()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = True
                        paused()
                    if event.key == pygame.K_1:
                        scount -= 80
                        wcount -= 50
                        h = 1
        if h == 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_2:
                        #if wcount > 89 and scount > 39:
                    fr()
                    fire(100,600)
                            
        if h == 1:
            home(500,300)  
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
