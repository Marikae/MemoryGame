import pygame

pygame.init()

# scene variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW = SCREEN_HEIGHT * SCREEN_WIDTH

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("img\\background.png")  #immagine di sfondo
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(background, (0, 0)) #color the screen
    pygame.display.update() #aggiorna la finestra di gioco or pygame.display.flip()

pygame.quit() #chiude programma
