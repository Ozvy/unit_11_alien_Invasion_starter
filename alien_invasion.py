import sys
import pygame
from settings import Settings
from ship import ship
from arsenal import Arsenal
from alien import Alien
class AlienInvasion:
    """
    The class that runs basically everything about this game.

    Attributes:
        event: the event that is fired.
    Methods: 
        run_game(self): Allows the game to run and function, and sets framerate .
        _check_events(self): Makes sure the game properly closes when the user closes the game, and checks for
        other events that run in the game.
        _update_screen(self): displays everything on the screen and updates anything on the screen to its new position.
        _check_keydown_event(self, event): Checks if the key is pressed down. Keys:
            K_Right: fires an event that makes the ship move right.
            K_Left: Ditto, but left.
            K_Space: Plays a sound when pressed and makes the ship fire a bullet.
            K_q: exits out of the game.
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

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)

        self.ship = ship(self, Arsenal(self))
        self.alien = Alien(self, 10, 10)

        
        


    def run_game(self):
        """
        Allows the game to run and function, and sets framerate . Also displays the game BG.
        """
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)


    def _update_screen(self):
        '''
         displays everything on the screen and updates anything on the screen to its new position.
        '''
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien.draw_alien()
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
        
        Keys:
            K_Right: fires an event that makes the ship move right.
            K_Left: Ditto, but left.
            K_Space: Plays a sound when pressed and makes the ship fire a bullet.
            K_q: exits out of the game.
        '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(300)
                
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
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


                    


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
