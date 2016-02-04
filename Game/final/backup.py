import pygame
import webbrowser

pygame.init()
width, height = 1040, 1040

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Survivor game group 3')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
brightred = (255,85,0)
brightgreen = (85,255,0)
blue = (0,0,255)
brightblue = (0,85,255)
grey = (150,150,150)

clock = pygame.time.Clock()
start = True
survivor_logo = pygame.image.load('survivor.png')
game_board = pygame.image.load('scaled_boardgame.jpg')

#########################################
def survivor(x, y):
    screen.blit(survivor_logo,(x,y))

x = (width * 0.07)
y = (height * 0.30)
#########################################
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

a = (width * 0)
s = (height * 0)

def open():
    webbrowser.open_new(r'Manual.pdf')

def quitgame():
    pygame.quit()
    quit()

################################################################
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

           start = False

    screen.fill(white)
    survivor(x, y)

    largeText = pygame.font.Font('freesansbold.ttf',75)
    TextSurf, TextRect = text_objects(" ", largeText)
    TextRect.center = ((width/2),(height/3))
    screen.blit(TextSurf, TextRect)

    button("Start Game",(width/5*1),(height/4*3),150,50,green,brightgreen,start)
    button("Instructions",(width/5*2),(height/4*3),150,50,blue,brightblue,open)
    button("Quit Game",(width/5*3),(height/4*3),150,50,red,brightred,quitgame)


    pygame.display.update()
    clock.tick(60)




pygame.quit()