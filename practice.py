from turtle import Screen, width
import pygame, sys

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
# RGB fargekode
LINE_COLOR = (50, 50, 50)
BG = (86, 87, 89)



sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption( 'Tre på rad: Av Nicolai' )
sc.fill( BG )

# pygame.draw.line( sc, LINE_COLOR  , (10, 10), (300, 300), 10 )

def drw_lines():

    # Horisontale linjer:
    pygame.draw.line( sc, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH )
    pygame.draw.line( sc, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH )

    # Vertikale Linjer:
    pygame.draw.line( sc, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH )
    pygame.draw.line( sc, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH )

drw_lines()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
