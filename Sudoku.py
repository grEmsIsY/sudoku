import pygame
import sys
from pygame.locals import *
import random

import numpy as np

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
board_solve = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]
board_valid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


# print board
def print_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
    print('= = = = = = = = = = = = =')


def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)  # row, col


def reset_board():
    for i in range(9):
        for j in range(9):
            board_solve[i][j] = 0
            board[i][j] = 0
            board_valid[i][j] = 0


# initialization board with n cell have value
def int_board(n=40):
    x = list(range(9))
    y = list(range(9))
    digits = list(range(1, 10))
    digits2 = []
    digits3 = []
    t = random.choice(x)
    for i in range(9):
        digits2.append(random.randint(1, 9))
        digits3.append(random.randint(1, 9))
        pos_x = random.choice(x)
        if len(x) > 1:
            x.pop(x.index(pos_x))
        pos_y = random.choice(y)
        if len(y) > 1:
            y.pop(y.index(pos_y))
        int_digit = random.choice(digits)
        if len(digits) > 1:
            digits.pop(digits.index(int_digit))
        board[pos_x][pos_y] = int_digit
        board_solve[pos_x][pos_y] = int_digit
        board_valid[pos_x][pos_y] = int_digit
    print_board(board)
    solve(board_solve)
    pos = []
    for i in range(9):
        for j in range(9):
            pos.append([i, j])
    for i in range(n):
        t = random.choice(pos)
        board[t[0]][t[1]] = board_solve[t[0]][t[1]]
        board_valid[t[0]][t[1]] = board_solve[t[0]][t[1]]
    print_board(board)


int_board()


def new_game(n: int):
    reset_board()
    int_board(n)


# clean board on screen
def clean_board():
    backgroud = pygame.display.set_mode((630, 700))
    color = (204, 255, 255)

    # Changing surface color
    backgroud.fill(color)
    # pygame.display.flip()

    Color_line = (0, 0, 0)
    pygame.draw.line(backgroud, Color_line, (70, 0), (70, 630))
    pygame.draw.line(backgroud, Color_line, (140, 0), (140, 630))
    pygame.draw.line(backgroud, Color_line, (210, 0), (210, 630), 2)
    pygame.draw.line(backgroud, Color_line, (280, 0), (280, 630))
    pygame.draw.line(backgroud, Color_line, (350, 0), (350, 630))
    pygame.draw.line(backgroud, Color_line, (420, 0), (420, 630), 2)
    pygame.draw.line(backgroud, Color_line, (490, 0), (490, 630))
    pygame.draw.line(backgroud, Color_line, (560, 0), (560, 630))
    pygame.draw.line(backgroud, Color_line, (630, 0), (630, 630))
    pygame.draw.line(backgroud, Color_line, (0, 70), (630, 70))
    pygame.draw.line(backgroud, Color_line, (0, 140), (630, 140))
    pygame.draw.line(backgroud, Color_line, (0, 210), (630, 210), 2)
    pygame.draw.line(backgroud, Color_line, (0, 280), (630, 280))
    pygame.draw.line(backgroud, Color_line, (0, 350), (630, 350))
    pygame.draw.line(backgroud, Color_line, (0, 420), (630, 420), 2)
    pygame.draw.line(backgroud, Color_line, (0, 490), (630, 490))
    pygame.draw.line(backgroud, Color_line, (0, 560), (630, 560))
    pygame.draw.line(backgroud, Color_line, (0, 630), (630, 630))
    pygame.font.init()
    button()


# print('board_solve')
# print_board(board_solve)
# print()
print('_________solve______________')


# show solved board
def solved_board():
    board_check = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    board_value = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(9):
        for j in range(9):
            if board[i][j] != board_solve[i][j]:
                board_check[i][j] = 1
                if board[i][j] != 0:
                    board_value[i][j] = board[i][j]
    clean_board()
    for i in range(9):
        for j in range(9):
            if board_check[i][j] == 0:
                text_surface = my_font.render(str(board_solve[i][j]), False, (51, 0, 102))
                backgroud.blit(text_surface, (i * 70 + 25, j * 70 + 15))
            else:
                text_surface = my_font.render(str(board_solve[i][j]), False, (255, 0, 0))
                backgroud.blit(text_surface, (i * 70 + 25, j * 70 + 15))
                if board_value[i][j] != 0:
                    text_surface = mmini_font.render(str(board_value[i][j]), False, (0, 0, 255))
                    backgroud.blit(text_surface, (i * 70 + 40, j * 70 + 5))
    pygame.display.flip()


# show unsolved board
def show_board():
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                if board_valid[i][j] == 0:
                    text_surface = my_font.render(str(board[i][j]), False, (35, 35, 35))
                    backgroud.blit(text_surface, (i * 70 + 25, j * 70 + 15))
                    pygame.display.flip()
                else:
                    text_surface = my_font.render(str(board[i][j]), False, (102, 0, 51))
                    backgroud.blit(text_surface, (i * 70 + 25, j * 70 + 15))
                    pygame.display.flip()


# show button
def button():
    solve_img = pygame.image.load('solve.png').convert_alpha()
    solve_img = pygame.transform.scale(solve_img, (150, 30))
    e_img = pygame.image.load('e.png').convert_alpha()
    e_img = pygame.transform.scale(e_img, (30, 30))
    m_img = pygame.image.load('m.png').convert_alpha()
    m_img = pygame.transform.scale(m_img, (30, 30))
    h_img = pygame.image.load('h.png').convert_alpha()
    h_img = pygame.transform.scale(h_img, (30, 30))
    evil_img = pygame.image.load('evil.png').convert_alpha()
    evil_img = pygame.transform.scale(evil_img, (30, 30))
    backgroud.blit(e_img, (80, 650))
    backgroud.blit(m_img, (130, 650))
    backgroud.blit(h_img, (190, 650))
    backgroud.blit(evil_img, (250, 650))
    backgroud.blit(solve_img, (400, 650))
    pygame.display.flip()


# control action on button
def game_mode():
    t = pygame.mouse.get_pos()
    if (t[0] <= 550) and (t[0] >= 400) and (t[1] <= 680) and (t[1] >= 650):
        if pygame.mouse.get_pressed()[0]:
            solved_board()
    if (t[0] <= 110) and (t[0] >= 80) and (t[1] <= 680) and (t[1] >= 650):
        if pygame.mouse.get_pressed()[0]:
            new_game(50)
            clean_board()
            show_board()
    if (t[0] <= 160) and (t[0] >= 130) and (t[1] <= 680) and (t[1] >= 650):
        if pygame.mouse.get_pressed()[0]:
            new_game(30)
            clean_board()
            show_board()
    if (t[0] <= 220) and (t[0] >= 190) and (t[1] <= 680) and (t[1] >= 650):
        if pygame.mouse.get_pressed()[0]:
            new_game(15)
            clean_board()
            show_board()
    if (t[0] <= 280) and (t[0] >= 250) and (t[1] <= 680) and (t[1] >= 650):
        if pygame.mouse.get_pressed()[0]:
            new_game(5)
            clean_board()
            show_board()


# update value of cell when input value
def get_cell_value():
    t = pygame.mouse.get_pos()
    x = t[0] // 70
    y = t[1] // 70
    value = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_0:
            if board_valid[x][y] == 0:
                clean_board()
                board[x][y] = 0
        if event.key == pygame.K_1:
            if board_valid[x][y] == 0:
                clean_board()
                board[x][y] = 1
        if event.key == pygame.K_2:
            if board_valid[x][y] == 0:
                clean_board()
                board[x][y] = 2
        if event.key == pygame.K_3:
            if board_valid[x][y] == 0:
                clean_board()
                board[x][y] = 3
        if event.key == pygame.K_4:
            if board_valid[x][y] == 0:
                clean_board()
                board[x][y] = 4
        if event.key == pygame.K_5:
            if board_valid[x][y] == 0:
                clean_board()
                board[x][y] = 5
        if event.key == pygame.K_6:
            if board_valid[x][y] == 0:
                clean_board()
                board[x][y] = 6
        if event.key == pygame.K_7:
            if board_valid[x][y] == 0:
                clean_board()
                board[x][y] = 7
        if event.key == pygame.K_8:
            if board_valid[x][y] == 0:
                clean_board()
                board[x][y] = 8
        if event.key == pygame.K_9:
            if board_valid[x][y] == 0:
                clean_board()
                board[x][y] = 9
        show_board()


# check win
def check_win():
    winner = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == board_solve[i][j]:
                winner += 1
    if winner == 81:
        winner_img = pygame.image.load('winner.jpg').convert_alpha()
        winner_img = pygame.transform.scale(winner_img, (630, 630))
        backgroud.blit(winner_img, (0, 0))
        pygame.display.flip()


pygame.init()
backgroud = pygame.display.set_mode((630, 700))
color = (204, 255, 255)

# Changing surface color
backgroud.fill(color)
# pygame.display.flip()

Color_line = (0, 0, 0)
# draw line
pygame.draw.line(backgroud, Color_line, (70, 0), (70, 630))
pygame.draw.line(backgroud, Color_line, (140, 0), (140, 630))
pygame.draw.line(backgroud, Color_line, (210, 0), (210, 630), 2)
pygame.draw.line(backgroud, Color_line, (280, 0), (280, 630))
pygame.draw.line(backgroud, Color_line, (350, 0), (350, 630))
pygame.draw.line(backgroud, Color_line, (420, 0), (420, 630), 2)
pygame.draw.line(backgroud, Color_line, (490, 0), (490, 630))
pygame.draw.line(backgroud, Color_line, (560, 0), (560, 630))
pygame.draw.line(backgroud, Color_line, (630, 0), (630, 630))
pygame.draw.line(backgroud, Color_line, (0, 70), (630, 70))
pygame.draw.line(backgroud, Color_line, (0, 140), (630, 140))
pygame.draw.line(backgroud, Color_line, (0, 210), (630, 210), 2)
pygame.draw.line(backgroud, Color_line, (0, 280), (630, 280))
pygame.draw.line(backgroud, Color_line, (0, 350), (630, 350))
pygame.draw.line(backgroud, Color_line, (0, 420), (630, 420), 2)
pygame.draw.line(backgroud, Color_line, (0, 490), (630, 490))
pygame.draw.line(backgroud, Color_line, (0, 560), (630, 560))
pygame.draw.line(backgroud, Color_line, (0, 630), (630, 630))
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
my_font = pygame.font.SysFont('venada', 64)
mmini_font = pygame.font.SysFont('venada', 20)
button()
show_board()
pygame.display.flip()
test_text = ""
running = True
while running:
    for event in pygame.event.get():
        get_cell_value()
        check_win()
        game_mode()
        if event.type == pygame.QUIT:
            running = False
