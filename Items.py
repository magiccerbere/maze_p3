class Items:
    """Create items and update their status"""
    def items_create(self,maze):
        """Create the items and find a random position from each"""

        possible_tile = []
        line_nb = 0
        for line in maze:
            tile_nb = 0
            for tile in line:
                if tile == 0:
                    possible_tile.append([line_nb, tile_nb])
                tile_nb += 1
            line_nb += 1
        syr_pos, eth_pos, pla_pos = random.sample(possible_tile, k=3)

        return syr_pos, eth_pos, pla_pos

    def items_colleted(self):
        """Compare position MacGiver with positions items. If the same, item is collected."""
        if mg_pos == syr_pos:
            backpack.append("syringe")
            syr_pos = []

        if mg_pos == eth_pos:
            backpack.append("ether")
            eth_pos = []

        if mg_pos == pla_pos:
            backpack.append("plastic_tube")
            pla_pos = []

        return backpack
