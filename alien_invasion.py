import sys
import pygame

class AlienInvasion:
    '''Overall class to manage game alerts and behavior'''

    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Alien Invasion')
        self.bg_colour =(210,210,230)


    def rungame(self):
        '''Start the main loop for the game'''
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(self.bg_colour)
            pygame.display.flip()




if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.rungame()




