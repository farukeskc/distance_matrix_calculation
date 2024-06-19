from docs.cell import Cell

ALFA = 10
BETA = 5
GAMMA = 20
OMEGA = 15


def vertical_distance_in_same_block(cell1: Cell, cell2: Cell, s: int):
    if cell1.x == cell2.x:
        return BETA*abs(cell1.y - cell2.y)
    else:
        if (cell1.y + cell2.y) < s:
            return BETA*min(2*s - cell1.y - cell2.y, cell1.y + cell2.y)
        else:
            return BETA*((s-cell1.y) + (s-cell2.y) + 2)


def horizontal_distance(cell1: Cell, cell2: Cell):
    return abs(cell1.x - cell2.x)*(2*ALFA + GAMMA)


def calculate_distance_in_same_block(cell1: Cell, cell2: Cell, s: int):
    return vertical_distance_in_same_block(cell1, cell2, s) + horizontal_distance(cell1, cell2)