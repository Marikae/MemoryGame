import pygame

pygame.init()

# scene variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW = SCREEN_HEIGHT * SCREEN_WIDTH

GRID_DIM = 4
CELL_DIM = SCREEN_WIDTH // GRID_DIM

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")
background = pygame.image.load("img\\background.png")  #immagine di sfondo
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

def drawGrid(griglia):
    for riga in range(GRID_DIM):
        for colonna in range(GRID_DIM):
            x = colonna * CELL_DIM
            y = riga * CELL_DIM
            pygame.draw.rect(screen, (255, 255, 255), (x, y, CELL_DIM, CELL_DIM), 2)
            font = pygame.font.Font(None, 36)
            testo = font.render(griglia[riga][colonna], True, (255, 255, 255))
            testo_rettangolo = testo.get_rect(center=(x + CELL_DIM / 2, y + CELL_DIM / 2))
            screen.blit(testo, testo_rettangolo)


run = True
while run:
    grid = [['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H']]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    screen.blit(background, (0, 0)) #color the screen
    drawGrid(grid)
    pygame.display.update() #aggiorna la finestra di gioco or pygame.display.flip()

pygame.quit() #chiude programma
