import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    """
    The class that runs basically everything about this game.


    Methods: 
        run_game(self): Allows the game to run and function, and sets framerate . Also displays the game BG.
        _check_events(self): Makes sure the game properly closes when the user closes the game.

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

        self.Ship = Ship(self)


    def run_game(self):
        """
        Allows the game to run and function, and sets framerate . Also displays the game BG.
        """
        while self.running:
            self._check_events()

            self._update_screen()
            self.clock.tick(self.settings.FPS)


    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.Ship.draw()
        pygame.display.flip()


    def _check_events(self):
        '''
        Makes sure the game properly closes when the user closes the game.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            
    def _check_keydown_event(self, event):
        pass
    def _check_keyup_event(self, event):
        pass


                    


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
