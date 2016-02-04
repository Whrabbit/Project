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