import sys
import pygame
from settings import Settings
class AlienInvasion:
    """
    The class that runs basically everything about this game.


    Methods: 
        run_game(): Allows the game to run and function, and sets framerate to 60.
    """
    def __init__(self):
        """
        Sets the display resolution and name of the window, as well as ensures the program runs. 
        Runs at the number of fps that is displayed in settings.py. 
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()
    
    def run_game(self):
        """
        Allows the game to run and function, and sets framerate . Also displays the game BG.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.bg, (0,0))
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)
                    


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
