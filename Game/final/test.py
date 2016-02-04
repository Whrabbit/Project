import pygame
import webbrowser
import random

pygame.init()
width, height = 1500, 1040

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

survivor_logo = pygame.image.load('survivor.png')
game_board = pygame.image.load('scaled_boardgame.jpg')
pawn1 = pygame.image.load('pawn1.png')
pawn2 = pygame.image.load('pawn2.png')
pawn3 = pygame.image.load('pawn3.png')
pawn4 = pygame.image.load('pawn4.png')
dice1 = pygame.image.load('dice1.png').convert()
dice2 = pygame.image.load('dice2.png').convert()
dice3 = pygame.image.load('dice3.png').convert()
dice4 = pygame.image.load('dice4.png').convert()
dice5 = pygame.image.load('dice5.png').convert()
dice6 = pygame.image.load('dice6.png').convert()
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


def dice():
    pygame.draw.rect(screen, black, (1128,177,300,300))
    d = random.randint(1,6)
    if d == 1:
        screen.blit(dice1, [1150, 200])
    elif d == 2:
        screen.blit(dice2, [1150, 200])
    elif d == 3:
        screen.blit(dice3, [1150, 200])
    elif d == 4:
        screen.blit(dice4, [1150, 200])
    elif d == 5:
        screen.blit(dice5, [1150, 200])
    else:
        screen.blit(dice6, [1150, 200])
def start():
        screen.fill(white)
        screen.blit(game_board,(a,s))
        screen.blit(pawn1,(x1,y1))
        screen.blit(pawn2,(x2,y2))
        screen.blit(pawn3,(x3,y3))
        screen.blit(pawn4,(x4,y4))

a = (width * 0)
s = (height * 0)
x1 = (width * 0)
y1 = (height * 0)
x2 = (width * 0.64)
y2 = (height * 0)
x3 = (width * 0)
y3 = (height * 0.928)
x4 = (width * 0.64)
y4 = (height * 0.928)

def open():
    webbrowser.open_new(r'Manual.pdf')

def quitgame():
    pygame.quit()
    quit()

def game_intro(start_screen = True):
    while start_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

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
        clock.tick(60)


def player_selection():
    start()
    while True:
        for event in pygame.event.get():
            button("Roll Dice",(width/4*3),(height/4*0.2),150,50,green,brightgreen,dice)
        pygame.display.update()
        clock.tick(10)
game_intro()
pygame.quit()