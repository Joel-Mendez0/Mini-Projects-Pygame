import random
import time
import pygame

def print_val(Grid):
    for row in Grid:
        for column in row:
            print(column, end = " ")
        print()
    print()

def print_grid(Grid):
    for row in Grid:
        for column in row:
            if column == 1:
                print("White", end = " ")
            else:
                print("Black", end = " ")
        print()
    print()

def display_grid(screen, WIDTH, HEIGHT, Grid):  
    cell_height = HEIGHT/len(Grid)
    cell_width = WIDTH/len(Grid[0])
    cell_x = 0
    cell_y = 0
   
    for row in range(len(Grid)):
        for col in range(len(Grid[row])):
            if Grid[row][col] == 1:
                cell_x = cell_width*col
                cell_y = cell_height*row
                r = random.randint(25,255)
                g = random.randint(25,255)
                b = random.randint(25,255)
                pygame.draw.rect(screen, (r,g,b), pygame.Rect(cell_x, cell_y, cell_width, cell_height))

def find_neighbors(row, column, Grid):
    neighbors = 0
    if (row+1) < len(Grid) and Grid[row+1][column] == 1:
        neighbors += 1
    if (row-1) > -1 and Grid[row-1][column] == 1:
        neighbors += 1
    if (column+1) < len(Grid[row]) and Grid[row][column+1] == 1:
        neighbors += 1
    if (column-1) > -1 and Grid[row][column-1] == 1:
        neighbors += 1

    return neighbors

def update_cells(Grid):
    new_grid = []
    for row in range(len(Grid)):
        new_row = []
        for column in range(len(Grid[row])):
            neighbors = find_neighbors(row,column,Grid)
            cell_status = Grid[row][column]
            if cell_status == 1:
                if neighbors > 2:
                    new_row.append(0)
                else:
                    new_row.append(1)
            else:
                for neighbor in range(neighbors):
                    cell_status = random.choice([0,0,1])
                    if cell_status:
                        break
                new_row.append(cell_status)
        new_grid.append(new_row)

    return new_grid

def initialize_pygames(WIDTH, HEIGHT):
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    return screen

Grid = []
rows = int(input("number of rows: "))
columns = int(input("number of columns: "))

for r in range(rows):
    temp_row = []
    for c in range(columns):
        temp_row.append(0)
    Grid.append(temp_row)

row = random.randint(0,len(Grid)-1)
column = random.randint(0,len(Grid[0])-1)
Grid[row][column] = 1

WIDTH = 1300
HEIGHT = 1300
screen = initialize_pygames(WIDTH, HEIGHT)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))
    
    #time.sleep(1)
    
    display_grid(screen, WIDTH, HEIGHT, Grid)
    #print_val(Grid)
    #print_grid(Grid)
    
    Grid = update_cells(Grid)

    clock.tick(60)
    
    pygame.display.flip()

pygame.quit()












