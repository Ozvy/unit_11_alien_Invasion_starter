import sys
import pygame
from settings import Settings
from ship import ship
class AlienInvasion:
    """
    The class that runs basically everything about this game.


    Methods: 
        run_game(self): Allows the game to run and function, and sets framerate .
        _check_events(self): Makes sure the game properly closes when the user closes the game, and checks for
        other events that run in the game.
        _update_screen(self): displays everything on the screen and updates anything on the screen to its new position.
        _check_keydown_event(self, event): Checks if the key is pressed down. if it is, move the ship.
        _check_keyup_event(self, event): Checks if the key is not being pressed. if it isn't pressed, keep the ship completely still.
        
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

        self.ship = ship(self)
        


    def run_game(self):
        """
        Allows the game to run and function, and sets framerate . Also displays the game BG.
        """
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)


    def _update_screen(self):
        '''
         displays everything on the screen and updates anything on the screen to its new position.
        '''
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
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
        '''
        Checks if the key is pressed down. if it is, move the ship.
        '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_event(self, event):
        '''
        Checks if the key is not being pressed. if it isn't pressed, keep the ship completely still.
        '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


                    


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
