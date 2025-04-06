import pygame
from settings import Settings
from typing import TYPE_CHECKING
from arsenal import Arsenal
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion



class ship:
    """
    Manages the player's ship.

    This class is responsible for:
    - Initializing the ship's appearance and starting position.
    - Handling the ship's movement based on user input.
    - Ensuring the ship stays within the game screen boundaries.
    - Drawing the ship on the screen.


    Notes on changes from original code:
    - The ship's vertical position (`self.y`) is tracked separately as a float for potentially smoother vertical movement.
    - Boolean flags (`self.moving_up`, `self.moving_down`) are introduced to handle upward and downward movement based on user input, mirroring the existing horizontal movement flags.
    - The original input handling for horizontal movement is assumed to remain in place within the game's event loop.
    """

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """
        Initializes the ship and sets its starting position.

        Args:
            game (AlienInvasion): References the main python script.
            arsenal (Arsenal): References the Arsenal instance managing the lasers the ship fires.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))
        
        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.arsenal = arsenal

    def update(self):
        '''
        Updates the ship position and arsenal.
        '''
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """
        Updates the ship's horizontal and vertical position based on movement events, and makes sure
        the ship doesn't leave the boundaries of the window.
        """
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y


    def draw(self):
        """
        Draws the ship and the bullets on screen.
        """

        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """
        Tells the ship's arsenal to fire a bullet.

        Returns:
            pygame.sprite.Sprite or None: The newly fired bullet sprite if firing is successful, otherwise None.
        """
        return self.arsenal.fire_bullet()
