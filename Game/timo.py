import pygame
import time
import sys
sys.setrecursionlimit(10000)
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (150,0,0)
green = (0,150,0)
brightred = (255,0,0)
brightgreen = (0,255,0)

block_color = (53,115,255)

car_width = 73


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('survivor')
clock = pygame.time.Clock()

#defining the color of the text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#defining text
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1:
            pygame.quit(),
            quit()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

#def action (str):
    #if action == ("quitgame"):
        #(
        #print("heyhoy")
        #)
    #elif action("playgame"):
        #(
        #print("lets find some friends and play")
        #)

#textinbuttonnotworkin
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)),(y+(h/2)))
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #making the display white
        gameDisplay.fill(white)
        #getting the font
        largeText = pygame.font.Font('freesansbold.ttf',75)
        #typing the text
        TextSurf, TextRect = text_objects("Panda Survivor", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,brightgreen)
        button("Quit",550,450,100,50,red,brightred)
        pygame.display.update()
        clock.tick(60)

game_intro()
pygame.quit()
quit()