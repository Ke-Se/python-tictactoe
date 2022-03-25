from turtle import width
import pygame, sys

pygame.init()

WIDTH = 600
HEIGHT = 600

sc = pygame.display.set_mode((WIDTH, HEIGHT))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
