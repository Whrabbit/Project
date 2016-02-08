import pygame
import webbrowser
import random

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

#positions van de tiles
tiles = [(8,13), (170,27), (245,27), (325,27), (405,27), (520,270), (635,27), (710,270), (400,13), (400,13), (707,13), (933,175), (933,245), (933,325), (933,400), (933,520), (933,635), (933,710), (933,785), (933,865), (707,715), (870,937), (790,937), (710,937), (635,937), (520,937), (400,937), (320,937), (245,937), (165,937), (8,715), (23,170), (23,250), (23,325), (23,400), (23,525), (23,640), (0,715), (23,790), (23,870)]


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
x1 = (23)
y1 = (27)
x2 = (933)
y2 = (27)
x3 = (23)
y3 = (937)
x4 = (933)
y4 = (937)
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
        clock.tick(60)

#creating the PlayerClass
class Player(object):
    def __init__(self,HP,CP,Playername,img,position):
        self.HP = 100
        self.CP = 15
        self.PlayerName = ""
        self.img = img
        self.position = position

#creating the players
p1 = Player(100,15,"Mike Tysen",pygame.image.load('img/pawn1.png'),tiles[0])
p2 = Player(100,15,"Badr Heri",pygame.image.load('img/pawn2.png'),tiles[10])
p3 = Player(100,15,"Rocky Belboa",pygame.image.load('img/pawn3.png'),tiles[30])
p4 = Player(100,15,"Manny Pecquiao",pygame.image.load('img/pawn4.png'),tiles[20])
#dices
def dice():
    pygame.draw.rect(screen, black, (1128,177,300,300))
    d = random.randint(1,6)
    if d == 1:
        d = tiles[0] + d
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
    return d

def move(self):
    for n in range(0,d):
        if tiles > 39:
            tiles = 0
        p1.position = tiles[0] + d
        p2.position + d
        p3.position + d
        p4.position + d


#screen of the game
def start():
        screen.fill(white)
        screen.blit(game_board,(a,s))
        screen.blit(pygame.image.load('img/pawn1.png'), tiles[0])

def player_selection():
    start()
    #pygame.mixer.music.load('Dust.wav')
    #pygame.mixer.music.play(-1,0)
    print("Player1 currently has:",p1.HP,"HP and has",p1.CP,"ConditionPoints"),print("Player2 currently has:",p2.HP,"HP and has",p2.CP,"ConditionPoints"),print("Player3 currently has:",p3.HP,"HP and has",p3.CP,"ConditionPoints"),print("Player4 currently has:",p4.HP,"HP and has",p4.CP,"ConditionPoints")
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