"""Maze is a simple maze game : help Mac Giver to find the exit !
Version 0.1
Developed by Mickael Sondag for OpenClassRooms' projet
Released under the WTFPL licence."""
# coding: utf8

import pygame
from pygame.locals import *
import random
from display import *
from macgyver import *
from watchman import *
from items import *


def main():
    """ if __name__ == "__main__"""
    """Screen init."""
    pygame.init()
    screen = pygame.display.set_mode((555, 600))
    pygame.display.set_caption("Mac Gyver, The Maze!")

    """Background."""
    background = pygame.image.load("background.jpg").convert()
    screen.blit(background, (0, 0))

    """Game Loop."""
    start = 1
    while start:
        pygame.time.Clock().tick(30)
        maze = Display.maze_create()
        Items.items_create(maze)
        win = False
        lose = False
        backpack = []
        mg_pos = [0, 0]
        while win == False and lose == False:
            mg_pos, win, lose = MacGiver.mg_move(mg_pos, maze)
            if len(backpack) <= 3:
                items.items_colleted()
            update_display()
        if lose == True:
            print("Mac Gyver a perdu!")
        else:
            print("Mac Giver a gagné!")
        if input("Tapez oui pour rejouer ou ce que vous voulez pour arrêtez") != "oui":
            exit()

main()
