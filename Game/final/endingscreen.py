import random
from random import randint

#creating the PlayerClass
class Player(object):
    def __init__(self):
        self.HP = 100
        self.CP = 15
        self.PlayerName = ""

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

#who's gonna die
WGD = randint(1,4)
if WGD == 1:
    Player1.HP = 0
elif WGD == 2:
    Player2.HP = 0
elif WGD == 3:
    Player3.HP = 0
elif WGD == 4:
    Player4.HP = 0

if Player1.HP <= 0:
    loser = Player1.Playername
if Player2.HP <= 0:
    loser = Player2.PlayerName
if Player3.HP <= 0:
    loser = Player3.PlayerName
if Player4.HP <= 0:
    loser = Player4.PlayerName

print("!~!KNOCK OUT!~!",loser,"couldn't keep up with the powerfull blows of his enemies. !~!KNOCK OUT!~!")