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
red = (150,0,0)
green = (0,150,0)
brightred = (255,0,0)
brightgreen = (0,255,0)
blue = (0,0,150)
brightblue = (0,0,255)

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

#creating the buttons
def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1:
            pygame.quit(),
            quit()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#
#FunctionThatsCurrentlyNotBeingUsed
#def action (str):
    #if action == ("quitgame"):
        #(
        #print("heyhoy")
        #)
    #elif action("playgame"):
        #(
        #print("lets find some friends and play")
        #)

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
        TextSurf, TextRect = text_objects("Panda Survivor", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

#defining the buttons
        button("Start Game",150,450,150,50,green,brightgreen)
        button("Instructions",350,100,150,50,blue,brightblue)
        button("Quit Game",550,450,150,50,red,brightred)

#defining how many teams per second the screen should get updated
        pygame.display.update()
        clock.tick(60)

#defining the variables
main_menu()
pygame.quit()
quit()