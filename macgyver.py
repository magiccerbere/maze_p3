import pygame
from pygame.locals import *
from constantes import *

class MacGyver:
    """Move MacGyver."""
    def __init__(self):
        self.mg_pos = [X_START,Y_START]
        self.win = False
        self.lose = False
    
    def mg_move(self, draw):
        """Move MacGyver and return the new position."""
        """If tile = 1 or 5, MacGyver moves"""
        
        pygame.key.set_repeat(400, 30) # ne fonctionne pas... Ou le mettre ? Car on sort de la boucle a chaque fois...
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP and self.mg_pos[1] != 0:
                    if draw.maze[1][self.mg_pos[1] - 1] == 1 or draw.maze[1][self.mg_pos[1] - 1] == 5:
                        self.mg_pos[1] -= 1
                          
                elif event.key == K_DOWN and self.mg_pos[1] != 14:
                    if draw.maze[1][self.mg_pos[1] + 1] == 1 or draw.maze[1][self.mg_pos[1] + 1] == 5:
                        self.mg_pos[1] += 1

                elif event.key == K_RIGHT and self.mg_pos[0] != 14:
                    if draw.maze[self.mg_pos[0] + 1][0] == 1 or draw.maze[0][self.mg_pos[0] + 1] == 5:
                        self.mg_pos[0] += 1

                elif event.key == K_LEFT and self.mg_pos[0] != 0:
                    if draw.maze[0][self.mg_pos[0] -1] == 1 or draw.maze[0][self.mg_pos[0] -1] == 5:
                        self.mg_pos[0] -= 1

            if draw.maze[self.mg_pos[0]][self.mg_pos[1]] == 5:
                if len(things.backpack) == 3:
                    self.win = True
                else :
                    self.lose = True

        return self.win, self.lose
