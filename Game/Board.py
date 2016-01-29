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