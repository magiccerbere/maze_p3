import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_RIGHT, K_LEFT, K_DOWN


class MacGyver:
    """Move MacGyver."""
    def __init__(self):
        self.mg_pos = []
        self.win = False
        self.lose = False

    def mg_move(self, draw, things):
        """If tile = 1 or 5, MacGyver moves"""

        free_tile = (0, 5)

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                previous_mg_pos = list(self.mg_pos)
                if event.key == K_UP and self.mg_pos[0] != 0 and \
                   draw.maze[self.mg_pos[0]-1][self.mg_pos[1]] in free_tile:
                    self.mg_pos[0] -= 1

                elif event.key == K_DOWN and self.mg_pos[0] != 14 and \
                   draw.maze[self.mg_pos[0]+1][self.mg_pos[1]] in free_tile:
                    self.mg_pos[0] += 1

                elif event.key == K_RIGHT and self.mg_pos[1] != 14 and \
                    draw.maze[self.mg_pos[0]][self.mg_pos[1]+1] in free_tile:
                    self.mg_pos[1] += 1

                elif event.key == K_LEFT and self.mg_pos[1] != 0 and \
                    draw.maze[self.mg_pos[0]][self.mg_pos[1]-1] in free_tile:
                    self.mg_pos[1] -= 1

                if draw.maze[self.mg_pos[0]][self.mg_pos[1]] == 5:
                    if len(things.backpack) == 3:
                        self.win = True
                    else:
                        self.lose = True

                draw.maze[previous_mg_pos[0]][previous_mg_pos[1]] = 0
                draw.maze[self.mg_pos[0]][self.mg_pos[1]] = 4
