import os
from time import sleep
from gospergun import gospergun


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def evolve_cell(field, x, y):
    neighbor_count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < len(field) and 0 <= j < len(field[x]) and (i != x or j != y):
                neighbor_count += field[i][j]
    return int(neighbor_count == 3 or neighbor_count == 2 and field[x][y] == 1)


def evolve_field(field):
    next_field = []
    for i in range(len(field)):
        row = []
        for j in range(len(field[i])):
            new = evolve_cell(field, i, j)
            row.append(new)
        next_field.append(row)
    return next_field


def print_field(field):
    for row in field:
        for cell in row:
            if cell == 0:
                print("░░", end='')
            if cell == 1:
                print("▓▓", end='')
        print()
    return


def run_game(field):
    while True:
        cls()
        field = evolve_field(field)
        print_field(field)
        sleep(0.2)


blinker = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]


cls()
run_game(gospergun)
