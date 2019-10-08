import random

class Items:
    """Create items and update their status"""
    def __init_(self):
        """Initialize. x_col and y_col mean items collected"""
        self.x_col = [1,2,3]
        self.y_col = 16
    
    def items_create(maze):
        """Create the items and find a random position from each"""
        line_nb = 0
        possible_tile = []
        pixel_sprite = 37
        for line in maze:
            tile_nb = 0
            for tile in line:
                if tile == 0:
                    possible_tile.append([line_nb, tile_nb])
                tile_nb += 1
            line_nb += 1
        syr_pos, eth_pos, pla_pos = random.sample(possible_tile, k=3)
        syr_pos = [i*pixel_sprite for i in syr_pos]
        eth_pos = [i*pixel_sprite for i in eth_pos]
        pla_pos = [i*pixel_sprite for i in pla_pos]

        return syr_pos, eth_pos, pla_pos

    def items_colleted(self, mg_pos):
        """Compare position MacGiver with positions items. If the same, item is collected."""
        if mg_pos == syr_pos:
            backpack.append("syringe")
            syr_pos = [self.x_col[0], self.y_col]

        if mg_pos == eth_pos:
            backpack.append("ether")
            eth_pos = [self.x_col[1], self.y_col]

        if mg_pos == pla_pos:
            backpack.append("plastic_tube")
            pla_pos = [self.x_col[2], self.y_col]

        return backpack
