import random
import pygame

pygame.init()

# Scene variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_DIM = 4
CELL_DIM = SCREEN_HEIGHT // GRID_DIM 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")

background = pygame.image.load("img/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

startScene = pygame.image.load("img/firstScene.png")
startScene = pygame.transform.scale(startScene, (SCREEN_WIDTH, SCREEN_HEIGHT))

blank = pygame.image.load("img/blank.png")
blank = pygame.transform.scale(blank, (CELL_DIM, CELL_DIM))

transparent = pygame.image.load("img/red.png")
transparent = pygame.transform.scale(transparent, (CELL_DIM, CELL_DIM))

image1 = pygame.image.load("img/image1.png")
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

rowT1 = NotImplemented
rowT2 = NotImplemented 
columnT1 = NotImplemented
columnT2 = NotImplemented

def createGrid(righe, colonne): #Create a grid
    grid = []
    for _ in range(righe):
        row = [""] * colonne
        grid.append(row)
    return grid

def insertInGrid(grid, coperture, immagini):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            grid[row][column] = immagini.pop()
            coperture[row][column] = blank

def hideCoperture(row, column):
    global background
    screen.blit(background, (column * CELL_DIM, row * CELL_DIM), (column * CELL_DIM, row * CELL_DIM, CELL_DIM, CELL_DIM))
    pygame.display.update()

def showTessere(row, column):
    global grid
    img = grid[row][column]
    screen.blit(img, (column * CELL_DIM, row * CELL_DIM))
    pygame.display.update()

def drawTessere():
    global grid
    for row in range(GRID_DIM):
        for column in range(GRID_DIM):
            screen.blit(grid[row][column], (column * CELL_DIM, row * CELL_DIM))

def drawCoperture():
    global coperture
    for row in range(GRID_DIM):
        for column in range(GRID_DIM):
            screen.blit(coperture[row][column], (column * CELL_DIM, row * CELL_DIM))

def hideTessere(row, column):
    global coperture
    screen.blit(coperture[row][column], (column * CELL_DIM, row * CELL_DIM))
    pygame.display.update()

def hideGrid():
    for row in range(GRID_DIM):
        for column in range(GRID_DIM):
            screen.blit(coperture[row][column], (column * CELL_DIM, row * CELL_DIM))

def foundCellClicked(pos):
    x, y = pos
    column = x // CELL_DIM
    row = y // CELL_DIM
    return row, column

def drawGrid():
    for row in range(GRID_DIM):
        for column in range(GRID_DIM):
            pygame.draw.rect(screen, (255, 255, 255), (column * CELL_DIM, row * CELL_DIM, CELL_DIM, CELL_DIM), 2)
            pygame.display.update()

def equalCells(coppia1, coppia2):
    return coppia1 == coppia2

def deleteCoppia():
    global grid, coperture
    row1 = rowT1 
    column1 = columnT1
    row2 = rowT2 
    column2 = columnT2
    grid[row1][column1] = background
    grid[row2][column2] = background
    coperture[row1][column1] = background
    coperture[row2][column2] = background
    
    drawTessere()
    drawCoperture()


def getPositionrowcolumn(coppia):
    for row in range(GRID_DIM):
        for column in range(GRID_DIM):
            if grid[row][column] == coppia:
                return row, column

def drawStartScreen():
    # Draw the initial screen with the "Start" button
    screen.blit(startScene, (0, 0))
    start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25, 100, 50)
    pygame.draw.rect(screen, (255, 219, 88), start_button_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Play", True, (0, 0, 0))
    text_rect = text.get_rect(center = start_button_rect.center)
    screen.blit(text, text_rect)

    # Draw a label
    label_font = pygame.font.SysFont(None, 40)
    if gameEnded:
        label_text = label_font.render("GAME END!", True, (255, 255, 255))
    else:
        label_text = label_font.render("MARICAO'S MEMORY GAME", True, (255, 255, 255))
    label_text_rect = label_text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(label_text, label_text_rect)
    
    pygame.display.update()

def resetVariables():
    global coppiaScoperta, rowT1, rowT2, columnT1, columnT2, coppia1, coppia2, coppieDaScoprire, grid, coperture, tessere, coppieTessere
    coppiaScoperta = 0
    rowT1 = NotImplemented
    rowT2 = NotImplemented
    columnT1 = NotImplemented
    columnT2 = NotImplemented
    coppia1 = NotImplemented
    coppia2 = NotImplemented
    grid = NotImplemented
    coperture = NotImplemented
    tessere = NotImplemented
    coppieTessere = NotImplemented
    coppieDaScoprire = 8

def initialize():
    global runPlay, grid, coperture, tessere, coppieTessere
    resetVariables()
    runPlay = True
    grid = createGrid(GRID_DIM, GRID_DIM)
    coperture = createGrid(GRID_DIM, GRID_DIM)
    # Creazione della lista delle coppie di immagini
    tessere = [image1, image2, image3, image4, image5, image6, image7, image8]
    coppieTessere = tessere * 2
    random.shuffle(coppieTessere)
    insertInGrid(grid, coperture, coppieTessere)
    screen.blit(background, (0, 0))
    hideGrid() # Tessere scoperte

def gamePlay():
    initialize()
    global coppiaScoperta, rowT1, rowT2, columnT1, columnT2, coppia1, coppia2, coppieDaScoprire, runPlay, gameEnded
    while runPlay:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #exit
                runPlay = False
            elif event.type == pygame.MOUSEBUTTONDOWN: #click
                if event.button == 1:  # left click
                    row, column = foundCellClicked(event.pos)
                    
                    if coppiaScoperta < 2:  # Verifica se non sono state scoperte più di due coppie
                        hideCoperture(row, column)
                        showTessere(row, column)
                        if coppiaScoperta == 0:
                            coppia1 = grid[row][column]
                            rowT1 = row
                            columnT1 = column
                        elif coppiaScoperta == 1:
                            coppia2 = grid[row][column]
                            rowT2 = row
                            columnT2 = column
                        coppiaScoperta += 1
                        if rowT1 == rowT2 and columnT1 == columnT2:
                            coppiaScoperta -= 1
                        if coppiaScoperta == 2:
                            if equalCells(coppia1, coppia2): # coppia uguale
                                deleteCoppia()
                                coppieDaScoprire -= 1
                                coppiaScoperta = 0
                                pygame.time.delay(900)
                            else: #coppia non uguale allora reset
                                pygame.time.delay(300)  
                                drawCoperture()
                                coppia1 = NotImplemented
                                coppia2 = NotImplemented
                                rowT1 = NotImplemented
                                rowT2 = NotImplemented
                                columnT1 = NotImplemented
                                columnT2 = NotImplemented
                                coppiaScoperta = 0
        if coppieDaScoprire == 0:
            runPlay = False
            gameEnded = True
            print("Game ended!")
        pygame.display.update()

def main():
    global run, gameEnded
    gameEnded = False
    run = True
    while run:
        drawStartScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25, 100, 50)
                    if start_button_rect.collidepoint(mouse_pos):
                        gamePlay()

main()
pygame.quit()
