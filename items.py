import random
from constantes import *

class Items:
    """Create items and update their status"""
    def __init__(self):
        self.backpack = []
        self.syr_pos = []
        self.eth_pos = []
        self.pla_pos = []
    
    def items_create(self, maze):
        """Create the items and find a random position from each"""
        line_nb = 0
        possible_tile = []
        for line in maze:
            tile_nb = 0
            for tile in line:
                if tile == 0:
                    possible_tile.append([line_nb, tile_nb])
                tile_nb += 1
            line_nb += 1
        self.syr_pos, self.eth_pos, self.pla_pos = random.sample(possible_tile, k=3)

    def items_colleted(self, character):
        """Compare position MacGiver with positions items. If the same, item is collected."""
        if character.mg_pos == self.syr_pos:
            self.backpack.append("syringe")
            self.syr_pos = [X_COL[0], Y_COL]

        if character.mg_pos == self.eth_pos:
            self.backpack.append("ether")
            self.eth_pos = [X_COL[1], Y_COL]

        if character.mg_pos == self.pla_pos:
            self.backpack.append("plastic_tube")
            self.pla_pos = [X_COL[2], Y_COL]
