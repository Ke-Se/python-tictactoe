# Author: Nicolai Staubo
# Program: Tic-Tac-Toe

# import the pygame module
from curses import KEY_BACKSPACE, KEY_DOWN
import pygame
from pygame.locals import *
 
# Define our square object and call super to
# give it all the properties and methods of pygame.sprite.Sprite
# Define the class for our square objects
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
         
        # Define the dimension of the surface
        # Here we are making squares of side 25px
        self.surf = pygame.Surface((25, 25))
         
        # Define the color of the surface using RGB color coding.
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
 
# initialize pygame
pygame.init()
 
# Define the dimensions of screen object
screen = pygame.display.set_mode((800, 600))

gameOn = True

# Our game loop
while gameOn:
    # for loop through the event queue
    for event in pygame.event.get():
         
        # Check for KEYDOWN event
        if event.type == KEY_DOWN:
             
            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == KEY_BACKSPACE:
                gameOn = False
                 
        # Check for QUIT event
        elif event.type == quit:
            gameOn = False
 

for y in range(height):
    for x in range(width):
        rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        pygame.draw.rect(window, color, rect)