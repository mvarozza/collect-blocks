import pygame
import random
import time

# Initialize Pygame

class StartGame():
    
    """Initializes the game with a single player sprite and black blocks to collect"""
        
    def __init__(self):
        
        """This function initializes basic variables that create the foundation of the game and will be
        used later to move the player block. Code within modified from 
        http://programarcadegames.com/python_examples/show_file.php?file=sprite_collect_blocks.py"""
        
        pygame.init()

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.periwinkle = (100, 0, 255)

        self.screen_width = 600
        self.screen_height = 600

        # Create the screen and add a caption
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.game_title = pygame.display.set_caption('Exit game and press enter in terminal when all 10' 
                                                     + ' blocks are collected!')
        
        # Set variables to be used later in moving our player block
        self.x1 = self.screen_width/2
        self.y1 = self.screen_height/2

        self.x1_change = 0
        self.y1_change = 0

        self.one_unit = 10
      
    class Block(pygame.sprite.Sprite):

        """ This class creates the ability to have blocks or targets within
        the game. It uses the function sprite and class Sprite which are both
         preexisting abilities of the pygame package. Modified code from 
         http://programarcadegames.com/python_examples/show_file.php?file=sprite_collect_blocks.py"""
            
        def __init__(self, color, width, height):
            
            """ Block method that initializes a single block variable. Calls on the Sprite class 
            within pygame to create visible game objects

            Parameters
            ----------
            color : variable that has been previously created as a tuple in StartGame.init()
            width : variable that has been previously created as an integer in StartGame.init()
            height : variable that has been previously created as an integer in StartGame.init()"""

            super().__init__()
            
            self.image = pygame.Surface([width, height])
            self.image.fill(color)
            self.rect = self.image.get_rect()

    def use_blocks(self):
            
            """Compiles all blocks and player block into a single function that can be called later. The 
            loop within this function creates 10 game blocks to collect and store them along with the 
            player block into self.block_list and self.all_sprites_list which are both managed by the
            Group class within pygame. Code within is modified slightly from 
            http://programarcadegames.com/python_examples/show_file.php?file=sprite_collect_blocks.py but 
            has been written into a methos to be more accessible"""

            self.block_list = pygame.sprite.Group()
            self.all_sprites_list = pygame.sprite.Group()

            # The for loop is used to control how many blocks the game initializes for the player to 
            # collect
            for i in range(10):

                # a single block is created 
                self.block = self.Block(self.black, 20, 15)

                # Set a random location for the block
                self.block.rect.x = random.randrange(self.screen_width)
                self.block.rect.y = random.randrange(self.screen_height)

                # Add the block to the list of objects
                self.block_list.add(self.block)
                self.all_sprites_list.add(self.block)

            # Create a white player block
            self.player = self.Block(self.white, 20, 15)
            self.all_sprites_list.add(self.player)

            # Used to manage how fast the screen updates
            self.clock = pygame.time.Clock()

            self.score = 0
        
    
    # -------- Main Program Loop ----------- 
    
    def run_game(self):

        """ Main program function. Calls on all existing functions and variables to first initialize 
        the game and then allow the player block to move and collect the game blocks. The player is
        moved using the arrow keys, as detailed within the for loop. Code within loop inspired by
        https://www.edureka.co/blog/snake-game-with-pygame/#install and 
        http://programarcadegames.com/python_examples/show_file.php?file=sprite_collect_blocks.py but has
        been modified. Modified into a method to be more easily accessible

        Return
        ----------
        No singular variable is returned, but running this function creates the game in a seperate 
        window that can be played by the user"""

        pygame.init()
        
        # The function use_blocks is called to create blocks as previously detailed within the game
        self.use_blocks()
        
        # Loop to quit game - this seems to be non-functional and does not close the game like it is 
        # supposed to. Force Quit is need to close the application
        game_over = False
        if game_over == True:
            pygame.quit()
            
        while not game_over:
            x1_change = 0
            y1_change = 0
            
            # The following loop directs the player on how to move dependent on each keystroke
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -self.one_unit
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = +self.one_unit
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        x1_change = 0
                        y1_change = -self.one_unit
                    elif event.key == pygame.K_DOWN:
                        x1_change = 0
                        y1_change = +self.one_unit

            pygame.display.flip()
            
            # Updates the players position based on keystrokes
            self.x1 += x1_change
            self.y1 += y1_change
            self.player.rect.x = self.x1
            self.player.rect.y = self.y1

            # Clear the screen
            self.screen.fill(self.periwinkle)
            pygame.display.update()

            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            # Check the list of collisions.
            for self.block in blocks_hit_list:
                self.score += 1
                print(self.score)

            # Draw all game blocks within screen
            self.all_sprites_list.draw(self.screen)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit to 60 frames per second
            self.clock.tick(60)

        pygame.display.quit()
        pygame.quit()
