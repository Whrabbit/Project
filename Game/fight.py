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
player1damageblocked = 0
player2damageblocked = 0
player3damageblocked = 0
player4damageblocked = 0

#creating the value damage
damage = 5

#creating the CPLoss value
player1CPLoss = 0
player2CPLoss = 0
player3CPLoss = 0
player4CPLoss = 0

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
Fighter1Roll = randint(1,4)
if Fighter2Roll == Fighter1Roll:
    if Fighter2Roll >= 2:
        Fighter2Roll = Fighter2Roll - 1
    else:
        Fighter2Roll = Fighter2Roll + 1

#creating the class Player
class Player(object):
    def __init__(self):
        self.HP = 100
        self.CP = 15
        self.PlayerName = ""

#define realdamage variable
realdamage = 0

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

if Fighter1Roll == 1:
    fighter1 = Player1.PlayerName
if Fighter1Roll == 2:
    fighter1 = Player2.PlayerName
if Fighter1Roll == 3:
    fighter1 = Player3.PlayerName
if Fighter1Roll == 4:
    fighter1 = Player4.PlayerName

#defining the options for defending
if fighter2 == Player1.PlayerName or fighter1 == Player1.PlayerName:
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            player1damageblocked = 3
            player1CPLoss = 1
        if OptionRoll == 2:
            player1damageblocked = 9
            player1CPLoss = 2
        if OptionRoll == 3:
            player1damageblocked = 19
            player1CPLoss = 3
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            player1damageblocked = 5
            player1CPLoss = 2
        if OptionRoll == 2:
            player1damageblocked = 11
            player1CPLoss = 3
        if OptionRoll == 3:
            player1damageblocked = 15
            player1CPLoss = 5
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            player1damageblocked = 7
            player1CPLoss = 2
        if OptionRoll == 2:
            player1damageblocked = 12
            player1CPLoss = 3
        if OptionRoll == 3:
            player1damageblocked = 16
            player1CPLoss = 4
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            player1damageblocked = 2
            player1CPLoss = 1
        if OptionRoll == 2:
            player1damageblocked = 4
            player1CPLoss = 2
        if OptionRoll == 3:
            player1damageblocked = 6
            player1CPLoss = 3
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            player1damageblocked = 10
            player1CPLoss = 2
        if OptionRoll == 2:
            player1damageblocked = 20
            player1CPLoss = 5
        if OptionRoll == 3:
            player1damageblocked = 30
            player1CPLoss = 8
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            player1damageblocked = 8
            player1CPLoss = 3
        if OptionRoll == 2:
            player1damageblocked = 13
            player1CPLoss = 4
        if OptionRoll == 3:
            player1damageblocked = 17
            player1CPLoss = 5

if fighter2 == Player2.PlayerName or fighter1 == Player2.PlayerName:
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            player2damageblocked = 5
            player2CPLoss = 2
        if OptionRoll == 2:
            player2damageblocked = 11
            player2CPLoss = 3
        if OptionRoll == 3:
            player2damageblocked = 15
            player2CPLoss = 3
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            player2damageblocked = 3
            player2CPLoss = 1
        if OptionRoll == 2:
            player2damageblocked = 9
            player2CPLoss = 2
        if OptionRoll == 3:
            player2damageblocked = 19
            player2CPLoss = 3
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            player2damageblocked = 2
            player2CPLoss = 1
        if OptionRoll == 2:
            player2damageblocked = 4
            player2CPLoss = 2
        if OptionRoll == 3:
            player2damageblocked = 6
            player2CPLoss = 3
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            player2damageblocked = 7
            player2CPLoss = 2
        if OptionRoll == 2:
            player2damageblocked = 12
            player2CPLoss = 3
        if OptionRoll == 3:
            player2damageblocked = 16
            player2CPLoss = 4
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            player2damageblocked = 8
            player2CPLoss = 3
        if OptionRoll == 2:
            player2damageblocked = 13
            player2CPLoss = 4
        if OptionRoll == 3:
            player2damageblocked = 17
            player2CPLoss = 5
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            player2damageblocked = 10
            player2CPLoss = 2
        if OptionRoll == 2:
            player2damageblocked = 20
            player2CPLoss = 5
        if OptionRoll == 3:
            player2damageblocked = 30
            player2CPLoss = 8

if fighter2 == Player3.PlayerName or fighter1 == Player3.PlayerName:
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            player3damageblocked = 10
            player3CPLoss = 2
        if OptionRoll == 2:
            player3damageblocked = 20
            player3CPLoss = 5
        if OptionRoll == 3:
            player3damageblocked = 30
            player3CPLoss = 8
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            player3damageblocked = 8
            player3CPLoss = 3
        if OptionRoll == 2:
            player3damageblocked = 13
            player3CPLoss = 4
        if OptionRoll == 3:
            player3damageblocked = 17
            player3CPLoss = 5
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            player3damageblocked = 3
            player3CPLoss = 1
        if OptionRoll == 2:
            player3damageblocked = 9
            player3CPLoss = 2
        if OptionRoll == 3:
            player3damageblocked = 19
            player3CPLoss = 3
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            player3damageblocked = 5
            player3CPLoss = 2
        if OptionRoll == 2:
            player3damageblocked = 11
            player3CPLoss = 3
        if OptionRoll == 3:
            player3damageblocked = 15
            player3CPLoss = 5
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            player3damageblocked = 7
            player3CPLoss = 2
        if OptionRoll == 2:
            player3damageblocked = 12
            player3CPLoss = 3
        if OptionRoll == 3:
            player3damageblocked = 16
            player3CPLoss = 4
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            player3damageblocked = 2
            player3CPLoss = 1
        if OptionRoll == 2:
            player3damageblocked = 4
            player3CPLoss = 2
        if OptionRoll == 3:
            player3damageblocked = 6
            player3CPLoss = 3

if fighter2 == Player4.PlayerName or fighter1 == Player4.PlayerName:
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            player4damageblocked = 8
            player4CPLoss = 3
        if OptionRoll == 2:
            player4damageblocked = 13
            player4CPLoss = 4
        if OptionRoll == 3:
            player4damageblocked = 17
            player4CPLoss = 5
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            player4damageblocked = 10
            player4CPLoss = 2
        if OptionRoll == 2:
            player4damageblocked = 20
            player4CPLoss = 5
        if OptionRoll == 3:
            player4damageblocked = 30
            player4CPLoss = 8
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            player4damageblocked = 5
            player4CPLoss = 2
        if OptionRoll == 2:
            player4damageblocked = 11
            player4CPLoss = 3
        if OptionRoll == 3:
            player4damageblocked = 15
            player4CPLoss = 5
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            player4damageblocked = 3
            player4CPLoss = 1
        if OptionRoll == 2:
            player4damageblocked = 9
            player4CPLoss = 2
        if OptionRoll == 3:
            player4damageblocked = 19
            player4CPLoss = 3
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            player4damageblocked = 2
            player4CPLoss = 1
        if OptionRoll == 2:
            player4damageblocked = 4
            player4CPLoss = 2
        if OptionRoll == 3:
            player4damageblocked = 6
            player4CPLoss = 3
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            player4damageblocked = 7
            player4CPLoss = 2
        if OptionRoll == 2:
            player4damageblocked = 12
            player4CPLoss = 3
        if OptionRoll == 3:
            player4damageblocked = 16
            player4CPLoss = 4

print("the two fighters where:",fighter2,"and",fighter1)

if fighter2 == Player1.PlayerName or fighter1 == Player1.PlayerName and fighter2 == Player2.PlayerName or fighter1 == Player2.PlayerName:
    if player1damageblocked > player2damageblocked:
        realdamage = player1damageblocked - player2damageblocked
        Player1.CP = Player1.CP - player1CPLoss
        Player2.HP = Player2.HP - realdamage
        Player2.CP = Player2.CP - player2CPLoss
    elif player1damageblocked < player2damageblocked:
        realdamage = player2damageblocked - player1damageblocked
        Player1.CP = Player1.CP - player1CPLoss
        Player1.HP = Player1.HP - realdamage
        Player2.CP = Player2.CP - player2CPLoss

if fighter2 == Player1.PlayerName or fighter1 == Player1.PlayerName and fighter2 == Player3.PlayerName or fighter1 == Player3.PlayerName:
    if player1damageblocked > player3damageblocked:
        realdamage = player1damageblocked - player3damageblocked
        Player1.CP = Player1.CP - player1CPLoss
        Player3.HP = Player3.HP - realdamage
        Player3.CP = Player3.CP - player3CPLoss
    elif player1damageblocked < player3damageblocked:
        realdamage = player3damageblocked - player1damageblocked
        Player1.CP = Player1.CP - player1CPLoss
        Player1.HP = Player1.HP - realdamage
        Player3.CP = Player3.CP - player3CPLoss

if fighter2 == Player1.PlayerName or fighter1 == Player1.PlayerName and fighter2 == Player4.PlayerName or fighter1 == Player4.PlayerName:
    if player1damageblocked > player4damageblocked:
        realdamage = player1damageblocked - player4damageblocked
        Player1.CP = Player1.CP - player1CPLoss
        Player4.HP = Player4.HP - realdamage
        Player4.CP = Player4.CP - player4CPLoss
    elif player1damageblocked < player4damageblocked:
        realdamage = player4damageblocked - player1damageblocked
        Player1.CP = Player1.CP - player1CPLoss
        Player1.HP = Player1.HP - realdamage
        Player4.CP = Player4.CP - player4CPLoss

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

if fighter2 == Player2.PlayerName or fighter1 == Player2.PlayerName and fighter2 == Player1.PlayerName or fighter1 == Player1.PlayerName:
    if player2damageblocked > player1damageblocked:
        realdamage = player2damageblocked - player1damageblocked
        Player2.CP = Player2.CP - player2CPLoss
        Player1.HP = Player1.HP - realdamage
        Player1.CP = Player1.CP - player1CPLoss
    elif player2damageblocked < player1damageblocked:
        realdamage = player1damageblocked - player2damageblocked
        Player2.CP = Player2.CP - player2CPLoss
        Player2.HP = Player2.HP - realdamage
        Player1.CP = Player1.CP - player1CPLoss

if fighter2 == Player2.PlayerName or fighter1 == Player2.PlayerName and fighter2 == Player3.PlayerName or fighter1 == Player3.PlayerName:
    if player2damageblocked > player3damageblocked:
        realdamage = player2damageblocked - player3damageblocked
        Player2.CP = Player2.CP - player2CPLoss
        Player3.HP = Player3.HP - realdamage
        Player3.CP = Player3.CP - player3CPLoss
    elif player2damageblocked < player3damageblocked:
        realdamage = player3damageblocked - player2damageblocked
        Player2.CP = Player2.CP - player2CPLoss
        Player2.HP = Player2.HP - realdamage
        Player3.CP = Player3.CP - player3CPLoss

if fighter2 == Player2.PlayerName or fighter1 == Player2.PlayerName and fighter2 == Player4.PlayerName or fighter1 == Player4.PlayerName:
    if player2damageblocked > player4damageblocked:
        realdamage = player2damageblocked - player4damageblocked
        Player2.CP = Player2.CP - player2CPLoss
        Player4.HP = Player4.HP - realdamage
        Player4.CP = Player4.CP - player4CPLoss
    elif player2damageblocked < player4damageblocked:
        realdamage = player4damageblocked - player2damageblocked
        Player2.CP = Player2.CP - player2CPLoss
        Player2.HP = Player2.HP - realdamage
        Player4.CP = Player4.CP - player4CPLoss

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

if fighter2 == Player3.PlayerName or fighter1 == Player3.PlayerName and fighter2 == Player1.PlayerName or fighter1 == Player1.PlayerName:
    if player3damageblocked > player1damageblocked:
        realdamage = player3damageblocked - player1damageblocked
        Player3.CP = Player3.CP - player3CPLoss
        Player1.HP = Player1.HP - realdamage
        Player1.CP = Player1.CP - player1CPLoss
    elif player3damageblocked < player1damageblocked:
        realdamage = player1damageblocked - player3damageblocked
        Player3.CP = Player3.CP - player3CPLoss
        Player3.HP = Player3.HP - realdamage
        Player1.CP = Player1.CP - player1CPLoss

if fighter2 == Player3.PlayerName or fighter1 == Player3.PlayerName and fighter2 == Player2.PlayerName or fighter1 == Player2.PlayerName:
    if player3damageblocked > player2damageblocked:
        realdamage = player3damageblocked - player2damageblocked
        Player3.CP = Player3.CP - player3CPLoss
        Player2.HP = Player2.HP - realdamage
        Player2.CP = Player2.CP - player2CPLoss
    elif player3damageblocked < player2damageblocked:
        realdamage = player2damageblocked - player3damageblocked
        Player3.CP = Player3.CP - player3CPLoss
        Player3.HP = Player3.HP - realdamage
        Player2.CP = Player2.CP - player2CPLoss

if fighter2 == Player3.PlayerName or fighter1 == Player3.PlayerName and fighter2 == Player4.PlayerName or fighter1 == Player4.PlayerName:
    if player3damageblocked > player4damageblocked:
        realdamage = player3damageblocked - player4damageblocked
        Player3.CP = Player3.CP - player3CPLoss
        Player4.HP = Player4.HP - realdamage
        Player4.CP = Player4.CP - player4CPLoss
    elif player3damageblocked < player4damageblocked:
        realdamage = player4damageblocked - player3damageblocked
        Player3.CP = Player3.CP - player3CPLoss
        Player3.HP = Player3.HP - realdamage
        Player4.CP = Player4.CP - player4CPLoss

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

if fighter2 == Player4.PlayerName or fighter1 == Player4.PlayerName and fighter2 == Player1.PlayerName or fighter1 == Player1.PlayerName:
    if player4damageblocked > player1damageblocked:
        realdamage = player4damageblocked - player1damageblocked
        Player4.CP = Player4.CP - player4CPLoss
        Player1.HP = Player1.HP - realdamage
        Player1.CP = Player1.CP - player1CPLoss
    elif player4damageblocked < player1damageblocked:
        realdamage = player1damageblocked - player4damageblocked
        Player4.CP = Player4.CP - player4CPLoss
        Player4.HP = Player4.HP - realdamage
        Player1.CP = Player1.CP - player1CPLoss

if fighter2 == Player4.PlayerName or fighter1 == Player4.PlayerName and fighter2 == Player2.PlayerName or fighter1 == Player2.PlayerName:
    if player4damageblocked > player2damageblocked:
        realdamage = player4damageblocked - player2damageblocked
        Player4.CP = Player4.CP - player4CPLoss
        Player2.HP = Player2.HP - realdamage
        Player2.CP = Player2.CP - player2CPLoss
    elif player4damageblocked < player2damageblocked:
        realdamage = player2damageblocked - player4damageblocked
        Player4.CP = Player4.CP - player4CPLoss
        Player4.HP = Player4.HP - realdamage
        Player2.CP = Player2.CP - player2CPLoss

if fighter2 == Player4.PlayerName or fighter1 == Player4.PlayerName and fighter2 == Player3.PlayerName or fighter1 == Player3.PlayerName:
    if player4damageblocked > player3damageblocked:
        realdamage = player4damageblocked - player3damageblocked
        Player4.CP = Player4.CP - player4CPLoss
        Player3.HP = Player3.HP - realdamage
        Player3.CP = Player3.CP - player3CPLoss
    elif player4damageblocked < player3damageblocked:
        realdamage = player3damageblocked - player4damageblocked
        Player4.CP = Player4.CP - player4CPLoss
        Player4.HP = Player4.HP - realdamage
        Player3.CP = Player3.CP - player3CPLoss


print("he hit for:",damage)
print("but","of his damage was blocked.")
print("Player1 has:",Player1.HP,"HP left.")
print("Player2 has:",Player2.HP,"HP left.")
print("Player3 has:",Player3.HP,"HP left.")
print("Player4 has:",Player4.HP,"HP left.")