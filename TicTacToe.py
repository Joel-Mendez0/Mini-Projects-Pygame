import pygame
import time

pygame.display.init()
pygame.font.init()

def draw_lines():
    white = (255,255,255)
    pygame.draw.line(screen,white,(Length/3,0),(Length/3,Width),6)
    pygame.draw.line(screen,white,(2*Length/3,0),(2*Length/3,Width),6)
    pygame.draw.line(screen,white,(0,Width/3),(Length,Width/3),6)
    pygame.draw.line(screen,white,(0,2*Width/3),(Length,2*Width/3),6)

def make_a_move_player_1():
    global Turn
    global Count
    for row in range(3):
        for col in range(3):
            if mx < (col + 1) * Length/3 and my < (row + 1) * Width/3 and left_click == True and Turn == 0 and board[row][col] == 0:
                board[row][col] = 1
                Turn = 1
                Count += 1

def make_a_move_player_2():
    global Turn
    global Count
    for row in range(3):
        for col in range(3):
            if mx < (col + 1) * Length/3 and my < (row + 1) * Width/3 and right_click == True and Turn == 1 and board[row][col] == 0:
                board[row][col] = 2
                Turn = 0
                Count += 1

def draw_x():
    white = (255, 255, 255)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                x1 = j * Length / 3
                y1 = i * Width / 3
                x2 = (j + 1) * Length / 3
                y2 = (i + 1) * Width / 3
                pygame.draw.line(screen, white, (x1, y1), (x2, y2), 6)
                pygame.draw.line(screen, white, (x2, y1), (x1, y2), 6)
def draw_circle():
    white = (255, 255, 255)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 2:
                x = (j + 0.5) * Length / 3
                y = (i + 0.5) * Width / 3
                pygame.draw.circle(screen, white, (int(x), int(y)), 100)

def player_1_win_conditions():
    if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
        return True
    if board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
        return True
    if board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
        return True
    if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        return True
    if board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        return True
    if board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        return True
    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        return True
    if board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1:
        return True
    return False
    
def player_2_win_conditions():
    if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
        return True
    if board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
        return True
    if board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
        return True
    if board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        return True
    if board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        return True
    if board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
        return True
    if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        return True
    if board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 2:
        return True
    return False
def draw_conditions():
    global Count
    if Count % 9 == 0 and Count != 0:
        return True
    return False

board = [[0,0,0],[0,0,0],[0,0,0]]

Length, Width = 800, 800

screen = pygame.display.set_mode((Length,Width))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

Turn = 0
Count = 0

done = False

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0,0,0))
    draw_lines()

    left_click, middle, right_click = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    if Turn == 0:
        make_a_move_player_1()
    else:
        make_a_move_player_2()

    draw_x()
    draw_circle()
    
    clock.tick(60)

    if player_1_win_conditions():
        print("Player 1 Wins!")
        done = True
    elif player_2_win_conditions():
        print("Player 2 Wins!")
        done = True
    elif draw_conditions():
        print("Draw")
        done = True
    else:
        done = False
    
    if Turn % 2 == 0:
        font = pygame.font.Font('freesansbold.ttf',32)
        text = font.render('X to move',True,(0,255,0),(0,0,255))
        textRect = text.get_rect()
        textRect.bottomright = (Length, Width)
    else:
        font = pygame.font.Font('freesansbold.ttf',32)
        text = font.render('O to move',True,(0,255,0),(0,0,255))
        textRect = text.get_rect()
        textRect.bottomright = (Length, Width)

    screen.blit(text, textRect)

    pygame.display.flip()

pygame.quit()