import pygame
import webbrowser

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
        if click[0] == 1:
          action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)),(y+(h/2)))
        screen.blit(textSurf, textRect)

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
x2 = (width * 0.5)
y2 = (height * 0)
x3 = (width * 0)
y3 = (height * 0.5)
x4 = (width * 0.5)
y4 = (height * 0.5)

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
    while True:
        for event in pygame.event.get():
            i=1
        start()


        button("Roll",(width/4*1),(height/4*3),150,50,green,brightgreen,dice)



        pygame.display.flip()
game_intro()
pygame.quit()
