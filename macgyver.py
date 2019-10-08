import pygame
from pygame.locals import *

class MacGiver:
    """Move MacGiver."""
    def __init__(self):
        self.mg_pos = [0,0]
    
    def mg_move(self, mg_pos, maze):
        """Move MacGiver and return the new position."""
        """If tile = 1 or 5, MacGiver moves"""

        self.mg_pos = mg_pos[0],mg_pos[1]
        
        pygame.key.set_repeat(400, 30)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP and self.mg_pos[1] != 0:
                    if maze[1][self.mg_pos[1] - 1] == 1 or 5:
                        self.mg_pos[1] -= 1
                          
                elif event.key == K_DOWN and mg_pos[1] != 14:
                    if maze[1][self.mg_pos[1] + 1] == 1 or 5:
                        self.mg_pos[1] += 1

                elif event.key == K_RIGHT and mg_pos[0] != 14:
                    if maze[0][self.mg_pos[0] + 1] == 1 or 5:
                        self.mg_pos[0] += 1

                elif event.key == K_LEFT and mg_pos[0] != 0:
                    if maze[0][self.mg_pos[0] -1] == 1 or 5:
                        self.mg_pos[0] -= 1

            if maze[self.mg_pos[0]][self.mg_pos[1]] == 5:
                if len(backpack) == 3:
                    win = True
                else :
                    lose = True

        return self.mg_pos, win, lose
