from Generator import *

#dimensions
WIDTH = 600
HEIGHT = 600

#colors
BG = (22, 22, 22)
WHITE =  (255, 255, 255)
CO_1 = (0, 10, 120)
LOCKED_CO = (60, 60, 60)
INCORRECT = (120, 10, 0)
BUTTON_CO_NORM = (66, 66, 66)
BUTTON_CO_HIGH = (0, 100, 240)


#gird
BOARD = make_board()

#transform
grid_pos = (75, 100)
GRID_TRANS = (grid_pos[0], grid_pos[1], WIDTH - 150, HEIGHT - 150)
CELL_SIZE = 50
GRID_SIZE = CELL_SIZE*9

