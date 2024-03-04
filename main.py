import random
import pygame

pygame.init()

# Scene variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_DIM = 4
CELL_DIM = SCREEN_WIDTH // GRID_DIM

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")

background = pygame.image.load("img/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

blank = pygame.image.load("img/blank.png")
blank = pygame.transform.scale(blank, (CELL_DIM, CELL_DIM))

pika = pygame.image.load("img/pika.jpg")
pika = pygame.transform.scale(pika, (CELL_DIM, CELL_DIM))

def crea_griglia(righe, colonne):
    griglia = []
    for _ in range(righe):
        riga = [""] * colonne
        griglia.append(riga)
    return griglia

def popola_griglia(griglia, immagini):
    coppie = immagini * 2
    random.shuffle(coppie)
    for riga in griglia:
        for i in range(len(riga)):
            riga[i] = coppie.pop()

def mostra_immagine(riga, colonna):
    global griglia
    img = griglia[riga][colonna]
    screen.blit(img, (colonna * CELL_DIM, riga * CELL_DIM))
    pygame.display.update()
    #pygame.time.delay(1000)
    #nascondi_immagine(riga, colonna)

def nascondi_immagine(riga, colonna):
    global blank
    screen.blit(blank, (colonna * CELL_DIM, riga * CELL_DIM))
    pygame.display.update()

def nascondiGriglia(griglia):
    for riga in range(GRID_DIM):
        for colonna in range(GRID_DIM):
            nascondi_immagine(riga, colonna)

run = True
#clock = pygame.time.Clock()

griglia = crea_griglia(4, 4)
popola_griglia(griglia, [pika, pika, pika, pika, pika, pika, pika, pika])

for riga in range(GRID_DIM):
    for colonna in range(GRID_DIM):
        pygame.draw.rect(screen, (255, 255, 255), (colonna * CELL_DIM, riga * CELL_DIM, CELL_DIM, CELL_DIM), 2)
        pygame.display.update()
screen.blit(background, (0, 0))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    nascondiGriglia(griglia)

pygame.quit()
