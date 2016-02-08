import pygame


class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "({},{})".format(self.X, self.Y)


class Tile:
    def __init__(self, position, type, moveable, texture, offset):
        self.Position = position
        self.Type = type
        self.Moveable = moveable

        self.DefaultTexture = pygame.image.load(texture).convert()
        self.Offset = offset

        self.Right = None
        self.Up = None
        self.Left = None
        self.Down = None
        self.Next = None

        self.Printed = False
        self.Loops = None

    def Draw(self, screen):
        if self.Printed == True:
            return

        _width = int(self.Offset / 3)
        if self.Type == 2:
            dim = -20
        elif self.Type == 5:
            dim = 519
        else:
            dim = 39

        screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width + dim)),
                    (_width + self.Position.X * self.Offset, _width + self.Position.Y * self.Offset))

        self.Printed = True

        if (self.Up != None and self.Up.Printed != True):
            self.Up.Draw(screen)
        elif (self.Left != None and self.Left.Printed != True):
            self.Left.Draw(screen)
        elif (self.Down != None and self.Down.Printed != True):
            self.Down.Draw(screen)
        elif (self.Right != None and self.Right.Printed != True):
            self.Right.Draw(screen)

    def Reset(self, loops):
        if self.Printed == True:
            self.Printed = False
        if self.Loops == loops:
            return

        if self.Up != None and self.Up.Loops != loops:
            self.Loops = loops
            self.Up.Reset(loops)
        elif self.Left != None and self.Left.Loops != loops:
            self.Loops = loops
            self.Left.Reset(loops)

        elif self.Down != None and self.Down.Loops != loops:
            self.Loops = loops
            self.Down.Reset(loops)

        elif self.Right != None and self.Right.Loops != loops:
            self.Loops = loops
            self.Right.Reset(loops)
        else:
            self.Loops = loops
            self.Reset(loops)
