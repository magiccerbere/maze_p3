"""Freedom for Mac Gyver is a simple maze game : help Mac Gyver to find the exit.
Version 0.1
Developed by Mickael Sondag for OpenClassRooms' project.
Released under the WTFPL licence."""
#! /usr/bin/env python3
# coding: utf-8
import pygame
from constants import TITLE
from game_loop import GameLoop



def main():
    """Screen init."""
    pygame.init()
    pygame.display.set_caption(TITLE)
    play = GameLoop()
    play.game_loop()


if __name__ == "__main__":
    main()
