"""Class Items"""
from random import sample
from constants import X_COL, Y_COL


class Items:
    """Create items and update their status"""
    def __init__(self):
        self.backpack = []
        self.syr_pos = []
        self.eth_pos = []
        self.pla_pos = []

    def items_create(self, maze):
        """Create the items and find a random position for each"""
        line_nb = 0
        possible_tile = []
        for line in maze:
            tile_nb = 0
            for tile in line:
                if tile == 0:
                    possible_tile.append([line_nb, tile_nb])
                tile_nb += 1
            line_nb += 1
        self.syr_pos, self.eth_pos, self.pla_pos = \
            sample(possible_tile, k=3)

    def items_colleted(self, character):
        """Compare MacGyver's position with items' position.
        If position is the same, item is collected."""

        if character.mg_pos == self.syr_pos:
            self.backpack.append("syringe")
            self.syr_pos = [Y_COL, X_COL[0]]

        if character.mg_pos == self.eth_pos:
            self.backpack.append("ether")
            self.eth_pos = [Y_COL, X_COL[1]]

        if character.mg_pos == self.pla_pos:
            self.backpack.append("plastic_tube")
            self.pla_pos = [Y_COL, X_COL[2]]
