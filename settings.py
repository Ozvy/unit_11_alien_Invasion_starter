from pathlib import Path

class Settings:
    '''
    Allows the user to change certain things about the game if they wanted to.
    '''
    def __init__(self):
        '''
        Some aspects of the game that can be changed easily. Includes the screen and ship's size and image used.
        '''
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60