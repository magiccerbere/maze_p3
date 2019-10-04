"""Maze is a simple maze game : help Mac Giver to find the exit !
Version 0.1
Developed by Mickael Sondag for OpenClassRooms' projet
Released under the WTFPL licence."""

import pygame
from pygame.locals import *
import random
from Display import *
from MacGiver import *
from Watchman import *
from Items import *


def main():
    """ if __name__ == "__main__"""
    """Screen init."""
    pygame.init()
    screen = pygame.display.set_mode((555, 600))
    pygame.display.set_caption("Mac Gyver, The Maze!")

    """Background."""
    background = pygame.image.load("background.jpg").convert()
    screen.blit(background,(0, 0))
    mg_pos = [0, 0]
    backpack = []
    win = False

    """Game Loop."""
    start = 1
    while start:
        pygame.time.Clock().tick(30) #Max 30 images per seconde
        maze = Display.maze_create()
        Items.items_create(maze)
        while win == False:
            pygame.key.set_repeat(400, 30)
            for event in pygame.event:
                if event.type == QUIT:
                    break
                else:
                    mg_pos, win = mg_pos.mg_move()
                    if len(backpack) <= 3:
                        Items.items_colleted()
                    update_display()

main()
