import pygame
from pygame.locals import *
from display import *
from items import *
from macgyver import *


class GameLoop:
    """Game Loop."""
    def __init__(self):
        self.things = Items()
        self.character = MacGyver()
        self.draw = Display()

    def game_loop(self):
        start = True
        while start:
            pygame.time.Clock().tick(30)
            self.draw = Display()
            self.character = MacGyver()
            self.things = Items()
            self.draw.maze_create()
            self.things.items_create(self.draw.maze)
            while self.character.win is False and self.character.lose is False:
                self.draw.update_display(self.things, self.character)
                self.character.mg_move(self.draw, self.things)
                if len(self.things.backpack) <= 3:
                    self.things.items_colleted(self.character)
            if self.character.lose is True:
                self.draw.gameover()
            else:
                exit()
