""" Maze is a simple maze game : help Mac Giver to find the exit !
Version 0.1
Developed by Mickaël Sondag for OpenClassRooms' projet
Released under the WTFPL licence."""

import pygame
from pygame.locals import *

class Display():
    """Manage all aspects of display."""
    def update_display(self):
        """Update of the display."""

        pygame.display.flip()
        
    def maze_create(self):
        """Creating of the maze"""
        maze = []
"""Labyrinthe = []
Map = lien_vers_la_carte 
for line in map:
     ligne_laby = []
     for tile in line:
            //faire ton parsing ici
            ligne_laby.append(valeur_de_la_case)
      Labyrinthe.append(ligne_laby)"""
        return maze
    

class Characters:
    """Manage Mac Giver, the watchman and the items."""

class MacGiver:
    def mg_move(self, key,mg_pos):
        pygame.key.set_repeat(400, 30)
        if event.type == KEYDOWN:
            if event.key == K_UP:
                #update mg_pos
            elif event.key == K_DOWN:

            elif event.key == K_RIGHT:

            elif event.key == K_LEFT:

            else: # wrong key

        return # mg_pos

    def items(self):
        """Create, is collected ?"""
        syringe_image = pygame.image.load("syringe.png").convert_alpha()
        ether_image = pygame.image.load("ether.png").convert_alpha()
        plastic_tube = pygame.image.load("plastic_tube").convert_alpha()
        syringe, ether, plastic_tube = False "False means isn't collected"

class watchman:

    def watchman(self):
        """Create the watchman."""
        whatchman_image = pygame.image.load("watchman.png").convert_alpha()
        

def main():
    if __name__ == "__main__"  
    """Screen init."""
    pygame.init()
    screen = pygame.display.set_mode((480,480))
    pygame.display.set_caption("Mac Gyver, The Maze!")

    """Background."""
    background = pygame.image.load("background.jpg").convert()
    screen.blit(background,(0,0))

    """Game Loop."""
    start = 1
    while start:
        clock.tick(30) #Max 30 images per seconde
        maze = maze_create()

    

main()
