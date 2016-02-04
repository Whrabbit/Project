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


def survivor(x, y):
    screen.blit(survivor_logo,(x,y))

x = (width * 0.22)
y = (height * 0.30)


def dice():
    d = random.randint(1,6)



def player_selection():

    while True:
        for event in pygame.event.get():
            button("Roll Dice",(width/4*3),(height/4*0.2),150,50,green,brightgreen,dice)
            d = random.randint(1,6)
            largeText = pygame.font.Font('freesansbold.ttf',75)
            TextSurf, TextRect  = text_objects(str(d), largeText)
            TextRect.center = ((width/2 *1.5),(height/3*2))
            screen.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(10)
pygame.quit()