#imports
import random
from random import randint

#creating the playerfighter value
PlayerFighter = "Insert PlayerFighter"

#creating the value damageblocked
damageblocked = 0

#creating the value damage
damage = 0

#creating the CPLoss value
CPLoss = 0

#defining who the fighters are
#fighter number 1
fighter1name = "player1"
#fighter number 2
fighter2name = "player2"

#getting a dice roll
class diceroll(object):
    def __init__(self):
        self.roll = randint(1,6)

#defining the different rolls we need
RollinThemDices = diceroll()
ConditionPointsRoll = randint(1,6)
OptionRoll = randint(1,3)
Fighter2Roll = randint(1,4)
Fighter1Roll = randint(1,4)

#creating the class Player
class Player(object):
    def __init__(self):
        self.HP = 100
        self.CP = 15
        self.PlayerName = ""

#creating the realdamage variable
realdamage = 0

class damage(object):
    def __init__(self):
        self.damageblocked = 0
        self.CPLoss = 0

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

if Fighter2Roll == Fighter1Roll:
    if Fighter2Roll > 1:
        Fighter2Roll = Fighter2Roll - 1
    else:
        Fighter2Roll = Fighter2Roll + 1

if Fighter2Roll == 1:
    fighter2name = Player1.PlayerName
if Fighter2Roll == 2:
    fighter2name = Player2.PlayerName
if Fighter2Roll == 3:
    fighter2name = Player3.PlayerName
if Fighter2Roll == 4:
    fighter2name = Player4.PlayerName

#defining the options for defending
if fighter2name == Player1.PlayerName:
    fighter2 = damage()
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            fighter2.damageblocked = 3
            fighter2.CPLoss = 1
        if OptionRoll == 2:
            fighter2.damageblocked = 9
            fighter2.CPLoss = 2
        if OptionRoll == 3:
            fighter2.damageblocked = 19
            fighter2.CPLoss = 3
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            fighter2.damageblocked = 5
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 11
            fighter2.CPLoss = 3
        if OptionRoll == 3:
            fighter2.damageblocked = 15
            fighter2.CPLoss = 5
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            fighter2.damageblocked = 7
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 12
            fighter2.CPLoss = 3
        if OptionRoll == 3:
            fighter2.damageblocked = 16
            fighter2.CPLoss = 4
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            fighter2.damageblocked = 2
            fighter2.CPLoss = 1
        if OptionRoll == 2:
            fighter2.damageblocked = 4
            fighter2.CPLoss = 2
        if OptionRoll == 3:
            fighter2.damageblocked = 6
            fighter2.CPLoss = 3
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            fighter2.damageblocked = 10
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 20
            fighter2.CPLoss = 5
        if OptionRoll == 3:
            fighter2.damageblocked = 30
            fighter2.CPLoss = 8
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            fighter2.damageblocked = 8
            fighter2.CPLoss = 3
        if OptionRoll == 2:
            fighter2.damageblocked = 13
            fighter2.CPLoss = 4
        if OptionRoll == 3:
            fighter2.damageblocked = 17
            fighter2.CPLoss = 5

if fighter2name == Player2.PlayerName:
    fighter2 = damage()
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            fighter2.damageblocked = 5
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 11
            fighter2.CPLoss = 3
        if OptionRoll == 3:
            fighter2.damageblocked = 15
            fighter2.CPLoss = 3
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            fighter2.damageblocked = 3
            fighter2.CPLoss = 1
        if OptionRoll == 2:
            fighter2.damageblocked = 9
            fighter2.CPLoss = 2
        if OptionRoll == 3:
            fighter2.damageblocked = 19
            fighter2.CPLoss = 3
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            fighter2.damageblocked = 2
            fighter2.CPLoss = 1
        if OptionRoll == 2:
            fighter2.damageblocked = 4
            fighter2.CPLoss = 2
        if OptionRoll == 3:
            fighter2.damageblocked = 6
            fighter2.CPLoss = 3
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            fighter2.damageblocked = 7
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 12
            fighter2.CPLoss = 3
        if OptionRoll == 3:
            fighter2.damageblocked = 16
            fighter2.CPLoss = 4
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            fighter2.damageblocked = 8
            fighter2.CPLoss = 3
        if OptionRoll == 2:
            fighter2.damageblocked = 13
            fighter2.CPLoss = 4
        if OptionRoll == 3:
            fighter2.damageblocked = 17
            fighter2.CPLoss = 5
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            fighter2.damageblocked = 10
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 20
            fighter2.CPLoss = 5
        if OptionRoll == 3:
            fighter2.damageblocked = 30
            fighter2.CPLoss = 8

if fighter2name == Player3.PlayerName:
    fighter2 = damage()
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            fighter2.damageblocked = 10
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 20
            fighter2.CPLoss = 5
        if OptionRoll == 3:
            fighter2.damageblocked = 30
            fighter2.CPLoss = 8
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            fighter2.damageblocked = 8
            fighter2.CPLoss = 3
        if OptionRoll == 2:
            fighter2.damageblocked = 13
            fighter2.CPLoss = 4
        if OptionRoll == 3:
            fighter2.damageblocked = 17
            fighter2.CPLoss = 5
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            fighter2.damageblocked = 3
            fighter2.CPLoss = 1
        if OptionRoll == 2:
            fighter2.damageblocked = 9
            fighter2.CPLoss = 2
        if OptionRoll == 3:
            fighter2.damageblocked = 19
            fighter2.CPLoss = 3
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            fighter2.damageblocked = 5
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 11
            fighter2.CPLoss = 3
        if OptionRoll == 3:
            fighter2.damageblocked = 15
            fighter2.CPLoss = 5
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            fighter2.damageblocked = 7
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 12
            fighter2.CPLoss = 3
        if OptionRoll == 3:
            fighter2.damageblocked = 16
            fighter2.CPLoss = 4
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            fighter2.damageblocked = 2
            fighter2.CPLoss = 1
        if OptionRoll == 2:
            fighter2.damageblocked = 4
            fighter2.CPLoss = 2
        if OptionRoll == 3:
            fighter2.damageblocked = 6
            fighter2.CPLoss = 3

if fighter2name == Player4.PlayerName:
    fighter2 = damage()
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            fighter2.damageblocked = 8
            fighter2.CPLoss = 3
        if OptionRoll == 2:
            fighter2.damageblocked = 13
            fighter2.CPLoss = 4
        if OptionRoll == 3:
            fighter2.damageblocked = 17
            fighter2.CPLoss = 5
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            fighter2.damageblocked = 10
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 20
            fighter2.CPLoss = 5
        if OptionRoll == 3:
            fighter2.damageblocked = 30
            fighter2.CPLoss = 8
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            fighter2.damageblocked = 5
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 11
            fighter2.CPLoss = 3
        if OptionRoll == 3:
            fighter2.damageblocked = 15
            fighter2.CPLoss = 5
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            fighter2.damageblocked = 3
            fighter2.CPLoss = 1
        if OptionRoll == 2:
            fighter2.damageblocked = 9
            fighter2.CPLoss = 2
        if OptionRoll == 3:
            fighter2.damageblocked = 19
            fighter2.CPLoss = 3
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            fighter2.damageblocked = 2
            fighter2.CPLoss = 1
        if OptionRoll == 2:
            fighter2.damageblocked = 4
            fighter2.CPLoss = 2
        if OptionRoll == 3:
            fighter2.damageblocked = 6
            fighter2.CPLoss = 3
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            fighter2.damageblocked = 7
            fighter2.CPLoss = 2
        if OptionRoll == 2:
            fighter2.damageblocked = 12
            fighter2.CPLoss = 3
        if OptionRoll == 3:
            fighter2.damageblocked = 16
            fighter2.CPLoss = 4

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

if Fighter1Roll == 1:
    fighter1name = Player1.PlayerName
if Fighter1Roll == 2:
    fighter1name = Player2.PlayerName
if Fighter1Roll == 3:
    fighter1name = Player3.PlayerName
if Fighter1Roll == 4:
    fighter1name = Player4.PlayerName

#defining the options for defending
if fighter1name == Player1.PlayerName:
    fighter1 = damage()
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            fighter1.damageblocked = 3
            fighter1.CPLoss = 1
        if OptionRoll == 2:
            fighter1.damageblocked = 9
            fighter1.CPLoss = 2
        if OptionRoll == 3:
            fighter1.damageblocked = 19
            fighter1.CPLoss = 3
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            fighter1.damageblocked = 5
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 11
            fighter1.CPLoss = 3
        if OptionRoll == 3:
            fighter1.damageblocked = 15
            fighter1.CPLoss = 5
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            fighter1.damageblocked = 7
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 12
            fighter1.CPLoss = 3
        if OptionRoll == 3:
            fighter1.damageblocked = 16
            fighter1.CPLoss = 4
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            fighter1.damageblocked = 2
            fighter1.CPLoss = 1
        if OptionRoll == 2:
            fighter1.damageblocked = 4
            fighter1.CPLoss = 2
        if OptionRoll == 3:
            fighter1.damageblocked = 6
            fighter1.CPLoss = 3
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            fighter1.damageblocked = 10
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 20
            fighter1.CPLoss = 5
        if OptionRoll == 3:
            fighter1.damageblocked = 30
            fighter1.CPLoss = 8
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            fighter1.damageblocked = 8
            fighter1.CPLoss = 3
        if OptionRoll == 2:
            fighter1.damageblocked = 13
            fighter1.CPLoss = 4
        if OptionRoll == 3:
            fighter1.damageblocked = 17
            fighter1.CPLoss = 5

if fighter1name == Player2.PlayerName:
    fighter1 = damage()
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            fighter1.damageblocked = 5
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 11
            fighter1.CPLoss = 3
        if OptionRoll == 3:
            fighter1.damageblocked = 15
            fighter1.CPLoss = 3
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            fighter1.damageblocked = 3
            fighter1.CPLoss = 1
        if OptionRoll == 2:
            fighter1.damageblocked = 9
            fighter1.CPLoss = 2
        if OptionRoll == 3:
            fighter1.damageblocked = 19
            fighter1.CPLoss = 3
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            fighter1.damageblocked = 2
            fighter1.CPLoss = 1
        if OptionRoll == 2:
            fighter1.damageblocked = 4
            fighter1.CPLoss = 2
        if OptionRoll == 3:
            fighter1.damageblocked = 6
            fighter1.CPLoss = 3
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            fighter1.damageblocked = 7
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 12
            fighter1.CPLoss = 3
        if OptionRoll == 3:
            fighter1.damageblocked = 16
            fighter1.CPLoss = 4
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            fighter1.damageblocked = 8
            fighter1.CPLoss = 3
        if OptionRoll == 2:
            fighter1.damageblocked = 13
            fighter1.CPLoss = 4
        if OptionRoll == 3:
            fighter1.damageblocked = 17
            fighter1.CPLoss = 5
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            fighter1.damageblocked = 10
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 20
            fighter1.CPLoss = 5
        if OptionRoll == 3:
            fighter1.damageblocked = 30
            fighter1.CPLoss = 8

if fighter1name == Player3.PlayerName:
    fighter1 = damage()
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            fighter1.damageblocked = 10
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 20
            fighter1.CPLoss = 5
        if OptionRoll == 3:
            fighter1.damageblocked = 30
            fighter1.CPLoss = 8
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            fighter1.damageblocked = 8
            fighter1.CPLoss = 3
        if OptionRoll == 2:
            fighter1.damageblocked = 13
            fighter1.CPLoss = 4
        if OptionRoll == 3:
            fighter1.damageblocked = 17
            fighter1.CPLoss = 5
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            fighter1.damageblocked = 3
            fighter1.CPLoss = 1
        if OptionRoll == 2:
            fighter1.damageblocked = 9
            fighter1.CPLoss = 2
        if OptionRoll == 3:
            fighter1.damageblocked = 19
            fighter1.CPLoss = 3
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            fighter1.damageblocked = 5
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 11
            fighter1.CPLoss = 3
        if OptionRoll == 3:
            fighter1.damageblocked = 15
            fighter1.CPLoss = 5
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            fighter1.damageblocked = 7
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 12
            fighter1.CPLoss = 3
        if OptionRoll == 3:
            fighter1.damageblocked = 16
            fighter1.CPLoss = 4
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            fighter1.damageblocked = 2
            fighter1.CPLoss = 1
        if OptionRoll == 2:
            fighter1.damageblocked = 4
            fighter1.CPLoss = 2
        if OptionRoll == 3:
            fighter1.damageblocked = 6
            fighter1.CPLoss = 3

if fighter1name == Player4.PlayerName:
    fighter1 = damage()
    if ConditionPointsRoll == 1:
        if OptionRoll == 1:
            fighter1.damageblocked = 8
            fighter1.CPLoss = 3
        if OptionRoll == 2:
            fighter1.damageblocked = 13
            fighter1.CPLoss = 4
        if OptionRoll == 3:
            fighter1.damageblocked = 17
            fighter1.CPLoss = 5
    elif ConditionPointsRoll == 2:
        if OptionRoll == 1:
            fighter1.damageblocked = 10
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 20
            fighter1.CPLoss = 5
        if OptionRoll == 3:
            fighter1.damageblocked = 30
            fighter1.CPLoss = 8
    elif ConditionPointsRoll == 3:
        if OptionRoll == 1:
            fighter1.damageblocked = 5
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 11
            fighter1.CPLoss = 3
        if OptionRoll == 3:
            fighter1.damageblocked = 15
            fighter1.CPLoss = 5
    elif ConditionPointsRoll == 4:
        if OptionRoll == 1:
            fighter1.damageblocked = 3
            fighter1.CPLoss = 1
        if OptionRoll == 2:
            fighter1.damageblocked = 9
            fighter1.CPLoss = 2
        if OptionRoll == 3:
            fighter1.damageblocked = 19
            fighter1.CPLoss = 3
    elif ConditionPointsRoll == 5:
        if OptionRoll == 1:
            fighter1.damageblocked = 2
            fighter1.CPLoss = 1
        if OptionRoll == 2:
            fighter1.damageblocked = 4
            fighter1.CPLoss = 2
        if OptionRoll == 3:
            fighter1.damageblocked = 6
            fighter1.CPLoss = 3
    elif ConditionPointsRoll == 6:
        if OptionRoll == 1:
            fighter1.damageblocked = 7
            fighter1.CPLoss = 2
        if OptionRoll == 2:
            fighter1.damageblocked = 12
            fighter1.CPLoss = 3
        if OptionRoll == 3:
            fighter1.damageblocked = 16
            fighter1.CPLoss = 4
#damage calculation



print("the first fighter is:",fighter1name)
print("the second fighter is:",fighter2name)

if fighter2.damageblocked > fighter1.damageblocked:
    realdamage = fighter2.damageblocked - fighter1.damageblocked
    if fighter1name == Player1.PlayerName:
        Player1.HP = Player1.HP - realdamage
    elif fighter1name == Player2.PlayerName:
        Player2.HP = Player2.HP - realdamage
    elif fighter1name == Player3.PlayerName:
        Player3.HP = Player3.HP - realdamage
    elif fighter1name == Player4.PlayerName:
        Player4.HP = Player4.HP - realdamage

if fighter1.damageblocked > fighter2.damageblocked:
    realdamage = fighter1.damageblocked - fighter2.damageblocked
    if fighter2name == Player1.PlayerName:
        Player1.HP = Player1.HP - realdamage
    elif fighter2name == Player2.PlayerName:
        Player2.HP = Player2.HP - realdamage
    elif fighter2name == Player3.PlayerName:
        Player3.HP = Player3.HP - realdamage
    elif fighter2name == Player4.PlayerName:
        Player4.HP = Player4.HP - realdamage

if fighter1.damageblocked == fighter2.damageblocked:
    print("ULTRA BLOCK")

if fighter1name == Player1.PlayerName:
    Player1.CP = Player1.CP - fighter1.CPLoss
elif fighter1name == Player2.PlayerName:
    Player2.CP = Player2.CP - fighter1.CPLoss
elif fighter1name == Player3.PlayerName:
    Player3.CP = Player3.CP - fighter1.CPLoss
elif fighter1name == Player4.PlayerName:
    Player4.CP = Player4.CP - fighter1.CPLoss

if fighter2name == Player1.PlayerName:
    Player1.CP = Player1.CP - fighter1.CPLoss
elif fighter2name == Player2.PlayerName:
    Player2.CP = Player2.CP - fighter1.CPLoss
elif fighter2name == Player3.PlayerName:
    Player3.CP = Player3.CP - fighter1.CPLoss
elif fighter2name == Player4.PlayerName:
    Player4.CP = Player4.CP - fighter1.CPLoss

print("fighter1dmg",fighter1.damageblocked)
print("fighter2dmg",fighter2.damageblocked)
print("Player1 has:",Player1.HP,"HP left and",Player1.CP,"ConditionPoints left.")
print("Player2 has:",Player2.HP,"HP left and",Player2.CP,"ConditionPoints left.")
print("Player3 has:",Player3.HP,"HP left and",Player3.CP,"ConditionPoints left.")
print("Player4 has:",Player4.HP,"HP left and",Player4.CP,"ConditionPoints left.")