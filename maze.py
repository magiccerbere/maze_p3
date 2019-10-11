"""Maze is a simple maze game : help Mac Giver to find the exit !
Version 0.1
Developed by Mickael Sondag for OpenClassRooms' projet
Released under the WTFPL licence."""
# coding: utf8
import pygame
from pygame.locals import *
import random
from display import *
from items import *
from macgyver import *
from game_loop import *
from constantes import *

def main():
    """ if __name__ == "__main__"""
    """Screen init."""
    pygame.init()
    pygame.display.set_caption(TITLE)

    play = GameLoop()
    play.game_loop()
   
main()
