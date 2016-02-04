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

#creating the CPLoss value
CPLoss = 1

#defining who the fighters are
#fighter number 1
fighter1 = "player1"
#fighter number 2
fighter2 = "player2"

#getting a dice roll
class diceroll(object):
    def __init__(self):
        self.roll = randint(1,6)

#defining the different rolls we need
RollinThemDices = diceroll()
SuperFightCardPick = RollinThemDices.roll
SuperFighterDmgRoll = RollinThemDices.roll
ConditionPointsRoll = randint(1,6)
OptionRoll = randint(1,3)
Fighter2Roll = randint(1,4)

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

#define realdamage variable
realdamage = 1

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

#creating the players
#Player1
Player1 = Player()
Player1.HP = 100
Player1.CP = 15
Player1.X = 10
Player1.Y = 10
Player1.PlayerName = "Mike Tysen"

#Player2
Player2 = Player()
Player2.HP = 100
Player2.CP = 15
Player2.X = 10
Player2.Y = 10
Player2.PlayerName = "Badr Heri"

#Player3
Player3 = Player()
Player3.HP = 100
Player3.CP = 15
Player3.X = 10
Player3.Y = 10
Player3.PlayerName = "Rocky Belboa"

#Player4
Player4 = Player()
Player4.HP = 100
Player4.CP = 15
Player4.X = 10
Player4.Y = 10
Player4.PlayerName = "Manny Pecquiao"

if Fighter2Roll == 1:
    fighter2 = Player1.PlayerName
if Fighter2Roll == 2:
    fighter2 = Player2.PlayerName
if Fighter2Roll == 3:
    fighter2 = Player3.PlayerName
if Fighter2Roll == 4:
    fighter2 = Player4.PlayerName

#defining the options for defending
if fighter2 == Player1.PlayerName:
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            damageblocked = 3
            CPLoss = 1
        if OptionRoll == 2:
            damageblocked = 9
            CPLoss = 2
        if OptionRoll == 3:
            damageblocked = 19
            CPLoss = 3
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            damageblocked = 5
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 11
            CPLoss = 3
        if OptionRoll == 3:
            damageblocked = 15
            CPLoss = 5
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            damageblocked = 7
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 12
            CPLoss = 3
        if OptionRoll == 3:
            damageblocked = 16
            CPLoss = 4
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            damageblocked = 2
            CPLoss = 1
        if OptionRoll == 2:
            damageblocked = 4
            CPLoss = 2
        if OptionRoll == 3:
            damageblocked = 6
            CPLoss = 3
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            damageblocked = 10
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 20
            CPLoss = 5
        if OptionRoll == 3:
            damageblocked = 30
            CPLoss = 8
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            damageblocked = 8
            CPLoss = 3
        if OptionRoll == 2:
            damageblocked = 13
            CPLoss = 4
        if OptionRoll == 3:
            damageblocked = 17
            CPLoss = 5

if fighter2 == Player2.PlayerName:
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            damageblocked = 5
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 11
            CPLoss = 3
        if OptionRoll == 3:
            damageblocked = 15
            CPLoss = 3
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            damageblocked = 3
            CPLoss = 1
        if OptionRoll == 2:
            damageblocked = 9
            CPLoss = 2
        if OptionRoll == 3:
            damageblocked = 19
            CPLoss = 3
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            damageblocked = 2
            CPLoss = 1
        if OptionRoll == 2:
            damageblocked = 4
            CPLoss = 2
        if OptionRoll == 3:
            damageblocked = 6
            CPLoss = 3
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            damageblocked = 7
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 12
            CPLoss = 3
        if OptionRoll == 3:
            damageblocked = 16
            CPLoss = 4
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            damageblocked = 8
            CPLoss = 3
        if OptionRoll == 2:
            damageblocked = 13
            CPLoss = 4
        if OptionRoll == 3:
            damageblocked = 17
            CPLoss = 5
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            damageblocked = 10
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 20
            CPLoss = 5
        if OptionRoll == 3:
            damageblocked = 30
            CPLoss = 8

if fighter2 == Player3.PlayerName:
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            damageblocked = 10
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 20
            CPLoss = 5
        if OptionRoll == 3:
            damageblocked = 30
            CPLoss = 8
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            damageblocked = 8
            CPLoss = 3
        if OptionRoll == 2:
            damageblocked = 13
            CPLoss = 4
        if OptionRoll == 3:
            damageblocked = 17
            CPLoss = 5
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            damageblocked = 3
            CPLoss = 1
        if OptionRoll == 2:
            damageblocked = 9
            CPLoss = 2
        if OptionRoll == 3:
            damageblocked = 19
            CPLoss = 3
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            damageblocked = 5
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 11
            CPLoss = 3
        if OptionRoll == 3:
            damageblocked = 15
            CPLoss = 5
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            damageblocked = 7
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 12
            CPLoss = 3
        if OptionRoll == 3:
            damageblocked = 16
            CPLoss = 4
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            damageblocked = 2
            CPLoss = 1
        if OptionRoll == 2:
            damageblocked = 4
            CPLoss = 2
        if OptionRoll == 3:
            damageblocked = 6
            CPLoss = 3

if fighter2 == Player4.PlayerName:
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            damageblocked = 8
            CPLoss = 3
        if OptionRoll == 2:
            damageblocked = 13
            CPLoss = 4
        if OptionRoll == 3:
            damageblocked = 17
            CPLoss = 5
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            damageblocked = 10
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 20
            CPLoss = 5
        if OptionRoll == 3:
            damageblocked = 30
            CPLoss = 8
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            damageblocked = 5
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 11
            CPLoss = 3
        if OptionRoll == 3:
            damageblocked = 15
            CPLoss = 5
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            damageblocked = 3
            CPLoss = 1
        if OptionRoll == 2:
            damageblocked = 9
            CPLoss = 2
        if OptionRoll == 3:
            damageblocked = 19
            CPLoss = 3
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            damageblocked = 2
            CPLoss = 1
        if OptionRoll == 2:
            damageblocked = 4
            CPLoss = 2
        if OptionRoll == 3:
            damageblocked = 6
            CPLoss = 3
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            damageblocked = 7
            CPLoss = 2
        if OptionRoll == 2:
            damageblocked = 12
            CPLoss = 3
        if OptionRoll == 3:
            damageblocked = 16
            CPLoss = 4
#damage calculation

if damageblocked >= damage:
    print("BLOCK!")
elif damageblocked < damage:
    realdamage = (damage - damageblocked)

print("the defending fighter was:",fighter2)

if fighter2 == Player1.PlayerName:
    Player1.HP = Player1.HP - realdamage
    Player1.CP = Player1.CP - CPLoss

if fighter2 == Player2.PlayerName:
    Player2.HP = Player2.HP - realdamage
    Player2.CP = Player2.CP - CPLoss

if fighter2 == Player3.PlayerName:
    Player3.HP = Player3.HP - realdamage
    Player3.CP = Player3.CP - CPLoss

if fighter2 == Player4.PlayerName:
    Player4.HP = Player4.HP - realdamage
    Player4.CP = Player4.CP - CPLoss

print("the superfighter was:",SuperFighter)
print("he hit for:",damage)
print("but",damageblocked,"of his damage was blocked.")
print("Player1 has:",Player1.HP,"HP left.")
print("Player2 has:",Player2.HP,"HP left.")
print("Player3 has:",Player3.HP,"HP left.")
print("Player4 has:",Player4.HP,"HP left.")