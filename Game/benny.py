import pygame

pygame.init()
width, height = 1000, 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Survivor')

black = (0,0,0)
white = (255,255,255)
red = (240,85,0)
green = (85,240,0)
brightred = (255,85,0)
brightgreen = (85,255,0)
blue = (0,85,240)
brightblue = (0,85,255)

clock = pygame.time.Clock()
start = True
survivor_logo = pygame.image.load('/Users/Benny/Desktop/survivor.png')
#########################################
def survivor(x, y):
    screen.blit(survivor_logo,(x,y))

x = (width * 0.07)
y = (height * 0.30)
#########################################
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def quitbutton(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1:
            pygame.quit(),
            quit()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)),(y+(h/2)))
        screen.blit(textSurf, textRect)

def playbutton(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1:
            # THIS ONE SHOULD BE CHANGED TO MAKE A NEW SCREEN
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)),(y+(h/2)))
        screen.blit(textSurf, textRect)

def instructionsbutton(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1:
            # THIS ONE SHOULD BE CHANGED TO MAKE A NEW SCREEN
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)),(y+(h/2)))
        screen.blit(textSurf, textRect)
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

    playbutton("Start Game",(width/5*1),(height/4*3),150,50,green,brightgreen)
    instructionsbutton("Instructions",(width/5*2),(height/4*3),150,50,blue,brightblue)
    quitbutton("Quit Game",(width/5*3),(height/4*3),150,50,red,brightred)


    pygame.display.update()
    clock.tick(60)




pygame.quit()
