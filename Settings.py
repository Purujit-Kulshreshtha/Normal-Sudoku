#dimensions
WIDTH = 600
HEIGHT = 600

#colors
BG = (22, 22, 22)
WHITE =  (255, 255, 255)
CO_1 = (120, 10, 0)


#gird
BOARD = [[y for y in range (0, 9)] for x in range(0, 9)]
BOARD_2 = [[1, 7, 8, 8, 9, 0, 6, 8, 0],
          [6, 5, 2, 3, 5, 7, 3, 7, 3],	
          [2, 5, 8, 1, 2, 4, 9, 9, 2],	
          [0, 4, 4, 8, 7, 2, 0, 2, 3],	
          [8, 4, 5, 9, 6, 2, 0, 2, 7],	
          [8, 7, 5, 8, 1, 3, 5, 8, 8],	
          [5, 0, 5, 8, 6, 8, 4, 2, 4],	
          [5, 0, 4, 4, 2, 3, 4, 3, 6],	
          [4, 4, 0, 2, 1, 2, 0, 4, 0]]

#transform
grid_pos = (75, 100)
GRID_TRANS = (grid_pos[0], grid_pos[1], WIDTH - 150, HEIGHT - 150)
CELL_SIZE = 50
GRID_SIZE = CELL_SIZE*9

