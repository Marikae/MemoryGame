import random
import pygame

pygame.init()

# Scene variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_DIM = 4
CELL_DIM = SCREEN_WIDTH // GRID_DIM 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")

background = pygame.image.load("img/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

blank = pygame.image.load("img/blank.png")
blank = pygame.transform.scale(blank, (CELL_DIM, CELL_DIM))

transparent = pygame.image.load("img/red.png")
transparent = pygame.transform.scale(transparent, (CELL_DIM, CELL_DIM))

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

coppiaScoperta = 0 #How many pairs are discovered
coppieDaScoprire = 8 #How many pairs to discover
#coppieSelezionate = [] #Selected pairs
rigaT1 = NotImplemented
rigaT2 = NotImplemented 
colonnaT1 = NotImplemented
colonnaT2 = NotImplemented

def crea_griglia(righe, colonne): #Create a grid
    griglia = []
    for _ in range(righe):
        riga = [""] * colonne
        griglia.append(riga)
    return griglia

def popola_griglia(griglia, coperture, immagini):
    for riga in range(len(griglia)):
        for colonna in range(len(griglia[riga])):
            griglia[riga][colonna] = immagini.pop()
            coperture[riga][colonna] = blank

def togliCopertura(riga, colonna):
    global background
    screen.blit(background, (colonna * CELL_DIM, riga * CELL_DIM), (colonna * CELL_DIM, riga * CELL_DIM, CELL_DIM, CELL_DIM))
    pygame.display.update()

def mostra_immagine(riga, colonna):
    global griglia
    img = griglia[riga][colonna]
    screen.blit(img, (colonna * CELL_DIM, riga * CELL_DIM))
    pygame.display.update()

def disegnaTessere():
    global griglia
    for riga in range(GRID_DIM):
        for colonna in range(GRID_DIM):
            screen.blit(griglia[riga][colonna], (colonna * CELL_DIM, riga * CELL_DIM))
    

def disegnaCoperture():
    global coperture
    for riga in range(GRID_DIM):
        for colonna in range(GRID_DIM):
            screen.blit(coperture[riga][colonna], (colonna * CELL_DIM, riga * CELL_DIM))
    


def nascondi_immagine(riga, colonna):
    global coperture
    screen.blit(coperture[riga][colonna], (colonna * CELL_DIM, riga * CELL_DIM))
    pygame.display.update()

def nascondiGriglia():
    for riga in range(GRID_DIM):
        for colonna in range(GRID_DIM):
            screen.blit(coperture[riga][colonna], (colonna * CELL_DIM, riga * CELL_DIM))

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

def deleteCoppia():
    global griglia, coperture
    
    riga1 = rigaT1 
    colonna1 = colonnaT1
    riga2 = rigaT2 
    colonna2 = colonnaT2

    griglia[riga1][colonna1] = background
    griglia[riga2][colonna2] = background

    coperture[riga1][colonna1] = background
    coperture[riga2][colonna2] = background
    
    disegnaTessere()
    disegnaCoperture()


def getPositionRigaColonna(coppia):
    for riga in range(GRID_DIM):
        for colonna in range(GRID_DIM):
            if griglia[riga][colonna] == coppia:
                return riga, colonna

run = True

griglia = crea_griglia(GRID_DIM, GRID_DIM)
coperture = crea_griglia(GRID_DIM, GRID_DIM)

# Creazione della lista delle coppie di immagini
tessere = [image1, image2, image3, image4, image5, image6, image7, image8]
coppieTessere = tessere * 2
random.shuffle(coppieTessere)

popola_griglia(griglia, coperture, coppieTessere)
screen.blit(background, (0, 0))
nascondiGriglia() # Tessere scoperte

while run:
    disegna_griglia()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exit
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #click
            if event.button == 1:  # left click
                riga, colonna = trova_cella_cliccata(event.pos)
                
                if coppiaScoperta < 2:  # Verifica se non sono state scoperte più di due coppie
                    togliCopertura(riga, colonna)
                    mostra_immagine(riga, colonna)
                    if coppiaScoperta == 0:
                        coppia1 = griglia[riga][colonna]
                        rigaT1 = riga
                        colonnaT1 = colonna
                    elif coppiaScoperta == 1:
                        coppia2 = griglia[riga][colonna]
                        rigaT2 = riga
                        colonnaT2 = colonna
                    coppiaScoperta += 1
                    if coppiaScoperta == 2:
                        if coppiaUguale(coppia1, coppia2): # coppia uguale
                            deleteCoppia()
                            coppieDaScoprire -= 1
                            coppiaScoperta = 0
                            pygame.time.delay(500)
                        else: #coppia non uguale allora reset
                            pygame.time.delay(300)  
                            disegnaCoperture()
                            coppia1 = NotImplemented
                            coppia2 = NotImplemented
                            rigaT1 = NotImplemented
                            rigaT2 = NotImplemented
                            colonnaT1 = NotImplemented
                            colonnaT2 = NotImplemented
                            coppiaScoperta = 0
    if coppieDaScoprire == 0:
        run = False
        print("Hai vinto!")
    pygame.display.update()

pygame.quit()
