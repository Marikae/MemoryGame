import pygame

pygame.init()

# scene variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW = SCREEN_HEIGHT * SCREEN_WIDTH

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
