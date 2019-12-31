import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # A CLASS TO REPRESENT A SINGLE ALIEN IN THE FLEET.
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/thai_fighter.png")
        self.rect = self.image.get_rect()

        # START EACH NEW ALIEN NEW THE TOP LEFT OF THE SCREEN.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #STORE THE ALIENS EXACT HORIZONTAL POSITION.
        self.x = float(self.rect.x)

    def check_edges(self):
        # RETURN TRUE IF ALIEN IS AT EDGE OF SCREEN.
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # MOVE THE ALIEN TO THE RIGHT
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
