"""Move MacGiver."""
class MacGiver:
    def mg_move(self,mg_pos):
        """Move MacGiver and return the new position."""
        self.mg_pos[0] = mg_pos[0] # x
        self.mg_pos[1] = mg_pos[1] # y

        """If tile = 1 or 5, MacGiver moves"""
        if event.type == KEYDOWN:
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
            win = True

        return self.mg_pos,win
