import pygame
import random
from pygame.sprite import Sprite

class Fuel(Sprite):

    def __init__(self, game):

        super().__init__()

        self.image = pygame.image.load("assets/fuel.png")

        self.rect = self.image.get_rect()

        self.rect.top = random.randint(0, game.screen_height-32)
        self.rect.right = random.randint(32, game.screen_width)