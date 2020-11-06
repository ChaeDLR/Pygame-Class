import pygame
from pygame.sprite import Sprite

class Player(Sprite):

    def __init__(self, game):

        super().__init__()

        self.screen = game.screen

        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("assets/ship.png")

        self.rect = self.image.get_rect()

        self.movement_speed = 8

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update_position(self):

        if self.moving_up and self.rect.top >= 0:
            self.rect.y -= self.movement_speed
        elif self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.y += self.movement_speed
        elif self.moving_left and self.rect.left >= 0:
            self.rect.x -= self.movement_speed
        elif self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.x += self.movement_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)