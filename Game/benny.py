import pygame

pygame.init()

class window():
    def __init__(self, screen, bg_color=(255,255,255)):

        self.screen = screen
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

    def run(self):

        loop = False

        while not loop:
            self.clock.tick(60)                      #clock.tick is for the smoothness of the frames, in this case 60

            for event in pygame.event.get():         #this function reads the "events" that are made and makes a list, like where are you pointing with your mouse at
                if event.type == pygame.QUIT:        #QUIT function will recognize when you want to close the window and shuts itself off
                    loop = True
                print(event)                         #prints every motion made with a mouse or keyboard

            self.screen.fill(self.bg_color)
            pygame.display.update()

if __name__ == "__main__":
    surface = pygame.display.set_mode((640, 480))    #surface width & length
    pygame.display.set_caption('Survivor')           #title on the window
    w = window(surface)
    w.run()


