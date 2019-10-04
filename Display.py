"""Create the maze and update each changes about display"""
class Display():
    """Manage all aspects of display."""
    
    def update_display(self):
        """Update of the display."""
        skeleton = pygame.image.load("skeleton.png").convert_alpha()
        guy = pygame.image.load("guy.png").convert_alpha()
        watchman = pygame.image.load("watchman.png").convert_alpha()
        macgyver = pygame.image.load("macgyver.png").convert_alpha()
        syringe_image = pygame.image.load("syringe.png").convert_alpha()
        ether_image = pygame.image.load("ether.png").convert_alpha()
        plastic_tube = pygame.image.load("plastic_tube").convert_alpha()

        """Size of sprites : 37*37."""
        pixel_sprite = 37

        line_nb = 0
        for line in maze:
            x = line_nb * pixel_sprite
            tile_nb = 0
            for tile in line:
                y = tile_nb * pixel_sprite 
                if tile == 1:
                    screen.blit(wall,(x,y))
                elif tile == 2:
                    screen.blit(skeleton,(x,y))
                elif tile == 3:
                    screen.blit(guy,(x,y))
                elif tile == 4:
                    screen.blit(depart,(x,y))
                elif tile == 5:
                    screen.blit(arrival,(x,y))
                tile_nb += 1
            line_nb += 1

        """Area for collected items : 600*45(at the bottom)"""
        if len(backpack) > 0:
            for items in backpack:
                if items == "syringe":
                    screen.blit(syringe,(0,560))
                if items == "ether":
                    screen.blit(ether,(50,560))
                if items == "plastic_tube":
                    screen.blit(plastic_tube,(50,560))
            
        
        pygame.display.flip()
        
    def maze_create():
        """Creating a maze about a Structure file"""
        with open("Structure", "r") as structure:
            maze = []
            for line in structure:
                line_maze = []
                for tile in line:
                    if tile != "\n":
                        line_maze.append(tile)
                maze.append(line_maze)
        return maze
    


    
