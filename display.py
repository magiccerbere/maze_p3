class Display():
    """Create the maze and Manage all aspects of display."""
    def __init__(self):
        self.pixel_sprite = 37
        self.syr_pos = [syr_pos[0]*self.pixel_sprite, syr_pos[1]*self.pixel_sprite]
        self.eth_pos = [eth_pos[0]*self.pixel_sprite, eth_pos[1]*self.pixel_sprite]
        self.pla_pos = [pla_pos[0]*self.pixel_sprite, pla_pos[1]*self.pixel_sprite]
    
    def update_display(self):
        """Update of the display."""
        skeleton = pygame.image.load("skeleton.png").convert_alpha()
        guy = pygame.image.load("guy.png").convert_alpha()
        watchman = pygame.image.load("watchman.png").convert_alpha()
        syringe = pygame.image.load("syringe.png").convert_alpha()
        ether = pygame.image.load("ether.png").convert_alpha()
        plastic = pygame.image.load("plastic_tube").convert_alpha()

        line_nb = 0
        for line in maze:
            x = line_nb * self.pixel_sprite
            tile_nb = 0
            for tile in line:
                y = tile_nb * self.pixel_sprite 
                if tile == 1:
                    screen.blit(wall, (x, y))
                elif tile == 2:
                    screen.blit(skeleton, (x, y))
                elif tile == 3:
                    screen.blit(guy, (x, y))
                elif tile == 4:
                    screen.blit(depart, (x, y))
                elif tile == 5:
                    screen.blit(watchman, (x, y))
                tile_nb += 1
            line_nb += 1

        """Display items. Area for collected items : 600*45(at the bottom)."""
        screen.blit(syringe, (self.syr_pos[0],self.syr_pos[1]))
        screen.blit(ether, (self.eth_pos[0], self.eth_pos[1]))
        screen.blit(plastic_tube, (self.pla_pos[0], self.pla_pos[1]))

        display_mg()
        pygame.display.flip()


    def display_mg():
        """Display MacGiver"""
        macgyver = pygame.image.load("macgyver.png").convert_alpha()
        mg_pos = [i*pixel_sprite for i in mg_pos]
        
        screen.blit(macgyver, (mg_pos[0], mg_pos[1]))

    def maze_create():
        """Creating a maze about a Structure file, and transfor the list of string in list of int"""
        with open("structure", "r") as structure:
            maze = []
            for line in structure:
                line_maze = []
                for tile in line:
                    if tile != "\n":
                        line_maze.append(int(tile))
                maze.append(line_maze)
        return maze
