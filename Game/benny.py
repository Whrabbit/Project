import pygame

pygame.init()

width   =   1000
height  =   1000


surface = pygame.display.set_mode((width,height))
pygame.display.set_caption('Survivor')
clock = pygame.time.Clock()


start = True

while start:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key ==  pygame.K_ESCAPE):
            start = False
        print (event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()