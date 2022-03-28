from turtle import Screen, width
import pygame, sys
import numpy

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLORS = 3
# RGB fargekode
LINE_COLOR = (50, 50, 50)
BG = (86, 87, 89)



sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption( 'Tre på rad: Av Nicolai' )
sc.fill( BG )

brd = numpy.zeros( (BOARD_ROWS, BOARD_COLORS) )

def drw_lines():

    # Horisontale linjer:
    pygame.draw.line( sc, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH )
    pygame.draw.line( sc, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH )

    # Vertikale Linjer:
    pygame.draw.line( sc, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH )
    pygame.draw.line( sc, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH )

def mark_square(row, colr, playr):
    brd[row][colr] = playr

def avbl_square(row, colr):
    return brd[row][colr] == 0

def is_brd_full():
    for row in range(BOARD_ROWS):
        for colr in range(BOARD_COLORS):
            if brd[row][colr] == 0:
                 return False
    return True

print(is_brd_full())
for row in range(BOARD_ROWS):
        for colr in range(BOARD_COLORS):
            mark_square( row, colr, 1 )
print(is_brd_full())


# Er midtfirkanten tilgjengelig?
print (avbl_square ( 1, 1 ) )
mark_square(1, 1, 2)
print (avbl_square ( 1, 1 ) )


drw_lines()

mark_square(0, 0, 1)
mark_square(1, 1, 2)

print(brd)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0] # Dette er X
            mouseY = event.pos[1] # Dette er Y

    pygame.display.update()

