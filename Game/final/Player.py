import pygame

#positions van de tiles
tiles = [(8,13), (170,27), (245,27), (325,27), (405,27), (520,270), (635,27), (710,270), (400,13), (400,13), (707,13)
    , (933,175), (933,245), (933,325), (933,400), (933,520), (933,635), (933,710), (933,785), (933,865), (707,715),
            (870,937), (790,937), (710,937), (635,937), (520,937), (400,937), (320,937), (245,937), (165,937), (8,715),
            (23,170), (23,250), (23,325), (23,400), (23,525), (23,640), (0,715), (23,790), (23,870)]

class Player:
    def __init__(self,Player,Image):
        self.Player = Player
        self.Image = Image
        self.X = 0
        self.Y = 0

    def movePlayer(self, x, y):
        self.X += x
        self.Y += y
        self.drawPlayer()

    def drawPlayer(self, screen = pygame.display.set_mode((1500, 800))):
        screen.blit(pygame.image.load(str(self.Image)), (self.X, self.Y))

#p1 = Player("Mike Tysen",tiles[0],pygame.image.load('img/pawn1.png'), 100, 15)
#p2 = Player("Badr Heri",tiles[10],pygame.image.load('img/pawn2.png'), 100, 15)
#p3 = Player("Rocky Belboa",tiles[30],pygame.image.load('img/pawn3.png'), 100, 15)
#p4 = Player("Manny Pecquiao",tiles[20],pygame.image.load('img/pawn4.png'), 100, 15)

