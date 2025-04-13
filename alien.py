import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """
    Represents a bullet fired by the player's ship.

    Inherits from pygame.sprite.Sprite, allowing it to be easily managed in sprite groups.

    Attributes:
        
        x (float): The bullet's horizontal position.
    """
    def __init__(self, game: 'AlienInvasion', x: float, y: float):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.x = float(self.rect.x)
        
    def update(self):
        pass

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)