import pygame
import webbrowser
import random
from Player import *

pygame.init()
width, height = 1500, 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Survivor game group 3')

black = (0,0,0)
white = (255,255,255)
red = (240,85,0)
green = (85,240,0)
brightred = (255,85,0)
brightgreen = (85,255,0)
blue = (0,85,240)
brightblue = (0,85,255)

clock = pygame.time.Clock()


survivor_logo = pygame.image.load('img/survivor.png')
game_board = pygame.image.load('img/scaled_boardgame.png')

#dice img
dice1 = pygame.image.load('img/dice1.png').convert()
dice2 = pygame.image.load('img/dice2.png').convert()
dice3 = pygame.image.load('img/dice3.png').convert()
dice4 = pygame.image.load('img/dice4.png').convert()
dice5 = pygame.image.load('img/dice5.png').convert()
dice6 = pygame.image.load('img/dice6.png').convert()
# Positions of pawns
a = (width * 0)
s = (height * 0)

#pygame.display.set_mode((0,0),pygame.FULLSCREEN)

def survivor(x, y):
    screen.blit(survivor_logo,(x,y))

x = (width * 0.22)
y = (height * 0.30)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)),(y+(h/2)))
        screen.blit(textSurf, textRect)
        if click[0] == 1:
          action()

    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)),(y+(h/2)))
        screen.blit(textSurf, textRect)

#instructions
def open():
    webbrowser.open_new(r'Manual.pdf')

def quitgame():
    pygame.quit()
    quit()
#start screen
def game_intro(start_screen = True):
    #pygame.mixer.music.load('Dust.wav')
    #pygame.mixer.music.play(-1,0)
    while start_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):

               start_screen = False


        screen.fill(white)
        survivor(x, y)

        button("Start Game",(width/4*1),(height/4*3),150,50,green,brightgreen,player_selection)
        button("Instructions",(width/4.5*2),(height/4*3),150,50,blue,brightblue,open)
        button("Quit Game",(width/4.7*3),(height/4*3),150,50,red,brightred,quitgame)

        largeText = pygame.font.Font('freesansbold.ttf',75)
        TextSurf, TextRect = text_objects(" ", largeText)
        TextRect.center = ((width/2),(height/3))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(10)

#dices
def dice():
    pygame.draw.rect(screen, black, (1128,177,300,300))
    d = random.randint(1,6)
    p1.tilesY = 20
    p1.tilesX = 0
    p2.tilesY = 500
    p2.tilesX = 0
    if d == 1:
        screen.blit(dice1, [1150, 200])
        if p1.movePlayer(p1.tilesY + 50, p1.tilesX + 0):
            if p1.tilesY >= 425 and True:
                p1.movePlayer(p1.tilesY + 0, p1.tilesX + 50)
    elif d == 2:
        screen.blit(dice2, [1150, 200])
        p1.movePlayer(p1.tilesY + 100, p1.tilesX + 0)
        if p1.tilesY >= 425 and True:
            p1.movePlayer(p1.tilesY + 0, p1.tilesX + 100)
    elif d == 3:
        screen.blit(dice3, [1150, 200])
        p1.movePlayer(p1.tilesY + 200, p1.tilesX + 0)
        if p1.tilesY >= 425 and True:
            p1.movePlayer(p1.tilesY + 0, p1.tilesX + 200)
    else:
        d == 4
        screen.blit(dice4, [1150, 200])
        p1.movePlayer(p1.tilesY + 250, p1.tilesX + 0)
        if p1.tilesY >= 425 and True:
            p1.movePlayer(p1.tilesY + 0, p1.tilesX + 250)


#screen of the game
def start():
    screen.fill(white)
    screen.blit(game_board,(a,s))
    screen.blit(pygame.image.load('img/pawn1.png'),tiles[0])
    screen.blit(pygame.image.load('img/pawn2.png'),tiles[10])
    screen.blit(pygame.image.load('img/pawn3.png'),tiles[30])
    screen.blit(pygame.image.load('img/pawn4.png'),tiles[20])
    #screen.blit(pygame.image.load('img/pawn1.png'), tiles[0])


def player_selection():
    start()
    #pygame.mixer.music.load('Dust.wav')
    #pygame.mixer.music.play(-1,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            button("Roll Dice",(width/4*3),(height/4*0.2),150,50,green,brightgreen,dice)


        pygame.display.update()
        clock.tick(10)

game_intro()
pygame.quit()