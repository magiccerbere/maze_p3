"""Class Display"""
from pygame import display, image, time
from constants import WIDTH_SCREEN, HEIGHT_SCREEN, BACKGROUND_IMG,\
    SKELETON_IMG, GUY_IMG, WATCHMAN_IMG, SYRINGE_IMG, ETHER_IMG,\
    PLASTIC_TUBE_IMG, WALL_IMG, MACGYVER_IMG, PIXEL_SPRITE, GAME_OVER_IMG


class Display:
    """Create the maze and manage all the display aspects."""
    def __init__(self):
        self.maze = []
        self.screen = display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        self.background = image.load(BACKGROUND_IMG).convert()

    def update_display(self, things, character):
        """Update of the display : background and items"""
        self.screen.blit(self.background, (0, 0))

        skeleton = image.load(SKELETON_IMG).convert_alpha()
        guy = image.load(GUY_IMG).convert_alpha()
        watchman = image.load(WATCHMAN_IMG).convert_alpha()
        syringe = image.load(SYRINGE_IMG).convert_alpha()
        ether = image.load(ETHER_IMG).convert_alpha()
        plastic_tube = image.load(PLASTIC_TUBE_IMG).convert_alpha()
        wall = image.load(WALL_IMG).convert_alpha()
        mac_gyver = image.load(MACGYVER_IMG).convert_alpha()

        line_nb = 0
        for line in self.maze:
            pos_y = line_nb * PIXEL_SPRITE
            tile_nb = 0
            for tile in line:
                pos_x = tile_nb * PIXEL_SPRITE
                if tile == 1:
                    self.screen.blit(wall, (pos_x, pos_y))
                elif tile == 2:
                    self.screen.blit(skeleton, (pos_x, pos_y))
                elif tile == 3:
                    self.screen.blit(guy, (pos_x, pos_y))
                elif tile == 4:
                    self.screen.blit(mac_gyver, (pos_x, pos_y))
                    character.mg_pos = [line_nb, tile_nb]
                elif tile == 5:
                    self.screen.blit(watchman, (pos_x, pos_y))

                tile_nb += 1
            line_nb += 1

        self.screen.blit(syringe, (things.syr_pos[1]*PIXEL_SPRITE,
                                   things.syr_pos[0]*PIXEL_SPRITE))
        self.screen.blit(ether, (things.eth_pos[1]*PIXEL_SPRITE,
                                 things.eth_pos[0]*PIXEL_SPRITE))
        self.screen.blit(plastic_tube, (things.pla_pos[1]*PIXEL_SPRITE,
                                        things.pla_pos[0]*PIXEL_SPRITE))

        display.flip()

    def maze_create(self):
        """Creating a maze about a Structure file.
        Transform the list of string in list of int."""
        with open("structure", "r") as structure:
            structure_maze = []
            for line in structure:
                line_maze = []
                for tile in line:
                    if tile != "\n":
                        line_maze.append(int(tile))
                structure_maze.append(line_maze)
            self.maze = structure_maze

    def gameover(self):
        """Display a screen of end."""

        game_over = image.load(GAME_OVER_IMG).convert()
        self.screen.blit(game_over, (0, 0))
        display.flip()
        time.wait(1500)
        self.screen.fill((0, 0, 0))
