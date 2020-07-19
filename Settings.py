#dimensions
WIDTH = 600
HEIGHT = 600

#colors
BG = (22, 22, 22)
WHITE =  (255, 255, 255)

#gird
BOARD = [[y for y in range (0, 9)] for x in range(0, 9)]

#transform
grid_pos = (75, 100)
GRID_TRANS = (grid_pos[0], grid_pos[1], WIDTH - 150, HEIGHT - 150)
CELL_SIZE = 50
GRID_SIZE = CELL_SIZE*9
