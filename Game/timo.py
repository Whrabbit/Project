#!#!#!#!#!#!#!#!#!#!#!#!MENU!#!#!#!#!#!#!#!#!#!#!#!#
#importing everything
import pygame
import time
pygame.init()

#defining display resolutions
display_width = 800
display_height = 600

#defining the colors
black = (0,0,0)
white = (255,255,255)
red = (240,85,0)
green = (85,240,0)
brightred = (255,85,0)
brightgreen = (85,255,0)
blue = (0,85,240)
brightblue = (0,85,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('survivor')
clock = pygame.time.Clock()

#defining the color of the text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#creating the buttons
def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1:
            pygame.quit(),
            quit()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

#textinbutton
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)),(y+(h/2)))
        gameDisplay.blit(textSurf, textRect)

#RunStartingScreen
def main_menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #making the display white
        gameDisplay.fill(white)
        #getting the font
        largeText = pygame.font.Font('freesansbold.ttf',75)
        #typing the text
        TextSurf, TextRect = text_objects("Survivor", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

#defining the buttons
        button("Start Game",(display_width/5*1),(display_height/4*3),150,50,green,brightgreen)
        button("Instructions",(display_width/5*2),(display_height/4*3),150,50,blue,brightblue)
        button("Quit Game",(display_width/5*3),(display_height/4*3),150,50,red,brightred)
#defining how many teams per second the screen should get updated
        pygame.display.update()
        clock.tick(60)

#defining the variables
main_menu()
pygame.quit()
quit()

#!#!#!#!#!#!#!#!#!#!#!#!DICE!#!#!#!#!#!#!#!#!#!#!#!#
from random import randint
print(randint(1,12))
                        #link this to dice images

#!#!#!#!#!#!#!#!#!#!#!#!BOARD!#!#!#!#!#!#!#!#!#!#!#!#
#importing everything
import pygame
import time
pygame.init()

#defining display resolutions
display_width = 800
display_height = 600

#defining the colors
black = (0,0,0)
white = (255,255,255)
red = (255,85,0)
green = (85,150,0)
blue = (0,85,150)
yellow = (255,255,85)
gray = (110,110,110)
lightgray = (222,222,222)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('survivor')
clock = pygame.time.Clock()

#defining the pixels on which the pawn can land
tileX = (display_width/17)
tileY = (display_height/17)

#creating the buttons
def button(x,y,w,h,ic):
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

#RunStartingScreen
def main_menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #making the display white
        gameDisplay.fill(white)

#defining the buttons
        #cornerbuttonBlue
        button((tileX),(tileY),(tileX*2),(tileY*2),blue)
        #cornerbuttonYellow
        button((tileX),(tileY*13),(tileX*2),(tileY*2),yellow)
        #cornerbuttonRed
        button((tileX*13),tileY,(tileX*2),(tileY*2),red)
        #cornerbuttonGreen
        button((tileX*13),(tileY*13),(tileX*2),(tileY*2),green)
        #LeftbuttonFight
        button((tileX),(tileY*7),(tileX*2),(tileY*2),gray)
        #RightbuttonFight
        button((tileX*13),(tileY*7),(tileX*2),(tileY*2),gray)
        #TopbuttonFight
        button((tileX*7),(tileY),(tileX*2),(tileY*2),gray)
        #BottombuttonFight
        button((tileX*7),(tileY*13),(tileX*2),(tileY*2),gray)
        #TilesLeftSide
        button((tileX),(tileY*3),(tileX*2),(tileY),lightgray)
        button((tileX),(tileY*4),(tileX*2),(tileY),white)
        button((tileX),(tileY*5),(tileX*2),(tileY),lightgray)
        button((tileX),(tileY*6),(tileX*2),(tileY),white)
        button((tileX),(tileY*9),(tileX*2),(tileY),lightgray)
        button((tileX),(tileY*10),(tileX*2),(tileY),white)
        button((tileX),(tileY*11),(tileX*2),(tileY),lightgray)
        button((tileX),(tileY*12),(tileX*2),(tileY),white)
        #TilesRightSide
        button((tileX*13),(tileY*3),(tileX*2),(tileY),lightgray)
        button((tileX*13),(tileY*4),(tileX*2),(tileY),white)
        button((tileX*13),(tileY*5),(tileX*2),(tileY),lightgray)
        button((tileX*13),(tileY*6),(tileX*2),(tileY),white)
        button((tileX*13),(tileY*9),(tileX*2),(tileY),lightgray)
        button((tileX*13),(tileY*10),(tileX*2),(tileY),white)
        button((tileX*13),(tileY*11),(tileX*2),(tileY),lightgray)
        button((tileX*13),(tileY*12),(tileX*2),(tileY),white)
        #TilesTopSide
        button((tileX*3),(tileY),(tileX),(tileY*2),lightgray)
        button((tileX*4),(tileY),(tileX),(tileY*2),white)
        button((tileX*5),(tileY),(tileX),(tileY*2),lightgray)
        button((tileX*6),(tileY),(tileX),(tileY*2),white)
        button((tileX*9),(tileY),(tileX),(tileY*2),lightgray)
        button((tileX*10),(tileY),(tileX),(tileY*2),white)
        button((tileX*11),(tileY),(tileX),(tileY*2),lightgray)
        button((tileX*12),(tileY),(tileX),(tileY*2),white)
        #TilesBotSide
        button((tileX*3),(tileY*13),(tileX),(tileY*2),lightgray)
        button((tileX*4),(tileY*13),(tileX),(tileY*2),white)
        button((tileX*5),(tileY*13),(tileX),(tileY*2),lightgray)
        button((tileX*6),(tileY*13),(tileX),(tileY*2),white)
        button((tileX*9),(tileY*13),(tileX),(tileY*2),lightgray)
        button((tileX*10),(tileY*13),(tileX),(tileY*2),white)
        button((tileX*11),(tileY*13),(tileX),(tileY*2),lightgray)
        button((tileX*12),(tileY*13),(tileX),(tileY*2),white)
#defining how many teams per second the screen should get updated
        pygame.display.update()
        clock.tick(60)

#defining the variables
main_menu()
pygame.quit()
quit()