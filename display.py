from constantes import *
import pygame
from pygame.locals import *

class Display:
    """Create the maze and Manage all aspects of display."""
    def __init__(self):
        self.maze = []
        self.screen = pygame.display.set_mode(( WIDTH_SCREEN, HEIGHT_SCREEN))
        self.background = pygame.image.load(BACKGROUND_IMG).convert()
    
    def update_display(self, things, character):
        """Update of the display."""

        """Background."""
        self.screen.blit(self.background, (0, 0))
        
        skeleton = pygame.image.load(SKELETON_IMG).convert_alpha()
        guy = pygame.image.load(GUY_IMG).convert_alpha()
        watchman = pygame.image.load(WATCHMAN_IMG).convert_alpha()
        syringe = pygame.image.load(SYRINGE_IMG).convert_alpha()
        ether = pygame.image.load(ETHER_IMG).convert_alpha()
        plastic_tube = pygame.image.load(PLASTIC_TUBE_IMG).convert_alpha()
        wall = pygame.image.load(WALL_IMG).convert_alpha()

        line_nb = 0
        for line in self.maze:
            y = line_nb * PIXEL_SPRITE
            tile_nb = 0
            for tile in line:
                x = tile_nb * PIXEL_SPRITE
                if tile == 1:
                    self.screen.blit(wall, (x, y))
                elif tile == 2:
                    self.screen.blit(skeleton, (x, y))
                elif tile == 3:
                    self.screen.blit(guy, (x, y))
                elif tile == 5:
                    self.screen.blit(watchman, (x, y))
                tile_nb += 1
            line_nb += 1

        """Display items. Area for collected items : 600*45(at the bottom)."""
        self.screen.blit(syringe, (things.syr_pos[0]*PIXEL_SPRITE, things.syr_pos[1]*PIXEL_SPRITE))
        self.screen.blit(ether, (things.eth_pos[0]*PIXEL_SPRITE, things.eth_pos[1]*PIXEL_SPRITE))
        self.screen.blit(plastic_tube, (things.pla_pos[0]*PIXEL_SPRITE, things.pla_pos[1]*PIXEL_SPRITE))

        self.display_mg(character)
        pygame.display.flip()


    def display_mg(self, character):
        """Display MacGiver"""
        macgyver = pygame.image.load(MACGYVER_IMG).convert_alpha()       
        self.screen.blit(macgyver, (character.mg_pos[0]*PIXEL_SPRITE, character.mg_pos[1]*PIXEL_SPRITE))

    def maze_create(self):
        """Creating a maze about a Structure file, and transfor the list of string in list of int"""
        with open("structure", "r") as structure:
            for line in structure:
                line_maze = []
                for tile in line:
                    if tile != "\n":
                        line_maze.append(int(tile))
                self.maze.append(line_maze)
