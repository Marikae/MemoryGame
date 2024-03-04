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

image1 = pygame.image.load("img/pika.jpg")
image1 = pygame.transform.scale(image1, (CELL_DIM, CELL_DIM))

image2 = pygame.image.load("img/image2.png")
image2 = pygame.transform.scale(image2, (CELL_DIM, CELL_DIM))

image3 = pygame.image.load("img/image3.png")
image3 = pygame.transform.scale(image3, (CELL_DIM, CELL_DIM))

image4 = pygame.image.load("img/image4.png")
image4 = pygame.transform.scale(image4, (CELL_DIM, CELL_DIM))

image5 = pygame.image.load("img/image5.jpg")
image5 = pygame.transform.scale(image5, (CELL_DIM, CELL_DIM))

image6 = pygame.image.load("img/image6.png")
image6 = pygame.transform.scale(image6, (CELL_DIM, CELL_DIM))

image7 = pygame.image.load("img/image7.jpg")
image7 = pygame.transform.scale(image7, (CELL_DIM, CELL_DIM))

image8 = pygame.image.load("img/image8.jpg")
image8 = pygame.transform.scale(image8, (CELL_DIM, CELL_DIM))

transparent = pygame.image.load("img/transparent.png")
transparent = pygame.transform.scale(transparent, (CELL_DIM, CELL_DIM))

coppiaScoperta = 0
coppieSelezionate = []


def crea_griglia(righe, colonne):
    griglia = []
    for _ in range(righe):
        riga = [""] * colonne
        griglia.append(riga)
    return griglia

def popola_griglia(griglia, immagini):
    for riga in griglia:
        for i in range(len(riga)):
            riga[i] = immagini.pop()

def togliCopertura(riga, colonna):
    global background
    screen.blit(background, (colonna * CELL_DIM, riga * CELL_DIM), (colonna * CELL_DIM, riga * CELL_DIM, CELL_DIM, CELL_DIM))
    pygame.display.update()

def mostra_immagine(riga, colonna):
    global griglia
    img = griglia[riga][colonna]
    screen.blit(img, (colonna * CELL_DIM, riga * CELL_DIM))
    pygame.display.update()

def nascondi_immagine(riga, colonna):
    global coperture
    screen.blit(coperture[riga][colonna], (colonna * CELL_DIM, riga * CELL_DIM))
    pygame.display.update()

def nascondiGriglia(griglia):
    for riga in range(GRID_DIM):
        for colonna in range(GRID_DIM):
            nascondi_immagine(riga, colonna)

def trova_cella_cliccata(pos):
    x, y = pos
    colonna = x // CELL_DIM
    riga = y // CELL_DIM
    return riga, colonna

def disegna_griglia():
    for riga in range(GRID_DIM):
        for colonna in range(GRID_DIM):
            pygame.draw.rect(screen, (255, 255, 255), (colonna * CELL_DIM, riga * CELL_DIM, CELL_DIM, CELL_DIM), 2)
            pygame.display.update()

def coppiaUguale(coppia1, coppia2):
    return coppia1 == coppia2

def deleteCoppia(coppia1, coppia2):
    global griglia, coperture
    for riga in range(GRID_DIM):
        for colonna in range(GRID_DIM):
            if griglia[riga][colonna] == coppia1 or griglia[riga][colonna] == coppia2:
                griglia[riga][colonna] = transparent
                coperture[riga][colonna] = transparent
    pygame.display.update()

run = True
coperture = crea_griglia(GRID_DIM, GRID_DIM) 
griglia = crea_griglia(GRID_DIM, GRID_DIM)

# Creazione della lista delle coppie di immagini
immagini = [image1, image2, image3, image4, image5, image6, image7, image8]
coppie_immagini = immagini * 2
random.shuffle(coppie_immagini)

coperture = [[blank] * GRID_DIM for _ in range(GRID_DIM)]

popola_griglia(griglia, coppie_immagini)

screen.blit(background, (0, 0))
nascondiGriglia(griglia)

while run:
    disegna_griglia()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic sinistro
                riga, colonna = trova_cella_cliccata(event.pos)
                if coppiaScoperta < 3:  # Verifica se non sono state scoperte più di due coppie
                    togliCopertura(riga, colonna)
                    mostra_immagine(riga, colonna)
                    coppieSelezionate.append(griglia[riga][colonna])
                    coppiaScoperta += 1
                    if coppiaScoperta == 2:
                        if coppiaUguale(coppieSelezionate[0], coppieSelezionate[1]):
                            coppiaScoperta = 0
                            coppieSelezionate = []
                            deleteCoppia(coppieSelezionate[0], coppieSelezionate[1])
                        else:
                            # Nascondi le immagini e resetta le coppie selezionate
                            pygame.time.delay(1000)  # Attendi un secondo
                            nascondiGriglia(griglia)
                            coppiaScoperta = 0
                            coppieSelezionate = []
    pygame.display.update()

pygame.quit()
