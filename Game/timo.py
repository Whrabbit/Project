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
def quitbutton(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1:
            pygame.quit(),
            quit()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

def playbutton(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1:
            print("playgame!!")
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

def instructionsbutton(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1:
            print("instructions")
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
        playbutton("Start Game",(display_width/5*1),(display_height/4*3),150,50,green,brightgreen)
        instructionsbutton("Instructions",(display_width/5*2),(display_height/4*3),150,50,blue,brightblue)
        quitbutton("Quit Game",(display_width/5*3),(display_height/4*3),150,50,red,brightred)
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

class position:
    self.x = int
    self.y = int

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

#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#SUPERFIGHT#!#!#!#!#!#!#!#!#!#!#!#!#!#!
#imports
import random
from random import randint

#creating the superfighter value
SuperFighter = "Insert SuperFighter"

#creating the playerfighter value
PlayerFighter = "Insert PlayerFighter"

#creating the damagesuperfighter value
SuperFighterDmgRoll = 5

#creating the value damageblocked
damageblocked = 5

#creating the value damage
damage = 5

#getting a dice roll
class diceroll(object):
    def __init__(self):
        self.roll = randint(1,6)

#defining the different rolls we need
RollinThemDices = diceroll()
SuperFightCardPick = RollinThemDices.roll
SuperFighterDmgRoll = RollinThemDices.roll
ConditionPointsRoll = randint(1,1)
OptionRoll = randint(1,3)

#defining the options for defending
if ConditionPointsRoll == 1:
    if OptionRoll == 1:
        damageblocked = 3
        CPLoss = 1
    if OptionRoll == 2:
        damageblocked = 9
        CPLoss = 2
    if OptionRoll == 3:
        CPLoss = 3

#creating the class Player
class Player(object):
    def __init__(self):
        self.HP = 100
        self.CP = 15
        self.PlayerName = ""

#creating the Superfighter dmg
class ClassSuperFightCard(object):
    def __init__(self):
        if SuperFighterDmgRoll == 1:
            self.DMG1 = int
        elif SuperFighterDmgRoll == 2:
            self.DMG2 = int
        elif SuperFighterDmgRoll == 3:
            self.DMG3 = int
        elif SuperFighterDmgRoll == 4:
            self.DMG4 = int
        elif SuperFighterDmgRoll == 5:
            self.DMG5 = int
        elif SuperFighterDmgRoll == 6:
            self.DMG6 = int

#insert Dice IMG
#print(SuperFighterDmgRoll)

#defining what card they will use
SuperFighterCard = ClassSuperFightCard()
if SuperFightCardPick == 1:
    #InsertFighterIMG's
    SuperFighter = "TerryCrewCard"
    damage = SuperFighterCard.DMG1 = 10
    damage = SuperFighterCard.DMG2 = 15
    damage = SuperFighterCard.DMG3 = 25
    damage = SuperFighterCard.DMG4 = 20
    damage = SuperFighterCard.DMG5 = 15
    damage = SuperFighterCard.DMG6 = 10

#------------------------------#

if SuperFightCardPick == 2:
    #InsertFighterIMG's
    SuperFighter = "JasonStathamCard"
    damage = SuperFighterCard.DMG1 = 15
    damage = SuperFighterCard.DMG2 = 17
    damage = SuperFighterCard.DMG3 = 19
    damage = SuperFighterCard.DMG4 = 21
    damage = SuperFighterCard.DMG5 = 23
    damage = SuperFighterCard.DMG6 = 26

#------------------------------#

if SuperFightCardPick == 3:
    #InsertFighterIMG's
    SuperFighter = "WesleySniperCard"
    damage = SuperFighterCard.DMG1 = 10
    damage = SuperFighterCard.DMG2 = 12
    damage = SuperFighterCard.DMG3 = 14
    damage = SuperFighterCard.DMG4 = 16
    damage = SuperFighterCard.DMG5 = 14
    damage = SuperFighterCard.DMG6 = 12

#------------------------------#

if SuperFightCardPick == 4:
    #InsertFighterIMG's
    SuperFighter = "JetRiCard"
    damage = SuperFighterCard.DMG1 = 10
    damage = SuperFighterCard.DMG2 = 30
    damage = SuperFighterCard.DMG3 = 12
    damage = SuperFighterCard.DMG4 = 25
    damage = SuperFighterCard.DMG5 = 14
    damage = SuperFighterCard.DMG6 = 23

#------------------------------#

if SuperFightCardPick == 5:
    #InsertFighterIMG's
    SuperFighter = "SteveSeagalCard"
    damage = SuperFighterCard.DMG1 = 10
    damage = SuperFighterCard.DMG2 = 15
    damage = SuperFighterCard.DMG3 = 12
    damage = SuperFighterCard.DMG4 = 11
    damage = SuperFighterCard.DMG5 = 25
    damage = SuperFighterCard.DMG6 = 20

#------------------------------#

if SuperFightCardPick == 6:
    #InsertFighterIMG's
    SuperFighter = "SuperMerioCard"
    damage = SuperFighterCard.DMG1 = 10
    damage = SuperFighterCard.DMG2 = 10
    damage = SuperFighterCard.DMG3 = 30
    damage = SuperFighterCard.DMG4 = 30
    damage = SuperFighterCard.DMG5 = 15
    damage = SuperFighterCard.DMG6 = 15

#damage calculation

if damageblocked >= damage:
    print("BLOCK!")
elif damageblocked < damage:
    realdamage = (damage - damageblocked)

#creating the players
Player1 = Player()
Player1.HP = 100
Player1.CP = 15
Player1.PlayerName = "Mike Tysen"
Player1.HP = Player1.HP - realdamage
Player1.CP = Player1.CP - CPLoss
print("the superfighter was:",SuperFighter)
print("he hit for:",damage)
print("but",damageblocked,"of his damage was blocked.")
print("player",Player1.PlayerName,"has taken:",damage,"damage, but blocked",damageblocked,"damage which leaves player1 with",Player1.HP,"HP and",Player1.CP,"Condition Points")