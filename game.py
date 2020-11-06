import pygame
import sys

from player import Player
from fuel import Fuel


class Game:

    def __init__(self):

        pygame.init()

        self.screen_width, self.screen_height = 400, 400

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption("Michigan python")

        self.background_color = (120, 240, 200)

        self.clock = pygame.time.Clock()

        self.player = Player(self)

        self.fuel_group = pygame.sprite.Group()

        self.create_fuel()

    def create_fuel(self):
        fuel = Fuel(self)
        self.fuel_group.add(fuel)

    def check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True

    def check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = False


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
    
    def update_screen(self):
        self.screen.fill(self.background_color)

        self.fuel_group.draw(self.screen)

        self.player.update_position()
        self.player.blitme()

        if pygame.sprite.spritecollideany(self.player, self.fuel_group):
            self.fuel_group.empty()
            self.create_fuel()


        pygame.display.update()

    def run_game(self):

        while True:
            self.clock.tick(60)
            self.check_events()
            self.update_screen()

game = Game()
game.run_game()
