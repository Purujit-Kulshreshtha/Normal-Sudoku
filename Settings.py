#dimensions
WIDTH = 600
HEIGHT = 600

#colors
BG = (22, 22, 22)
WHITE =  (255, 255, 255)
CO_1 = (120, 10, 0)
LOCKED_CO = (60, 60, 60)


#gird
BOARD = [[y for y in range (0, 9)] for x in range(0, 9)]
BOARD_2 = [[0,6,0,2,0,0,8,3,1],
         [0,0,0,0,8,4,0,0,0],
         [0,0,7,6,0,3,0,4,9],
         [0,4,6,8,0,2,1,0,0],
         [0,0,3,0,9,6,0,0,0],
         [1,2,0,7,0,5,0,0,6],
         [7,3,0,0,0,1,0,2,0],
         [8,1,5,0,2,9,7,0,0],
         [0,0,0,0,7,0,0,1,5]]

BOARD_2_FINISHED =  [[5,3,4,6,7,8,9,1,2],
         	     [6,7,2,1,9,5,3,4,8],
         	     [1,9,8,3,4,2,5,6,7],
         	     [8,5,9,7,6,1,4,2,3],
         	     [4,2,6,8,5,3,7,9,1],
         	     [7,1,3,9,2,4,8,5,6],
         	     [9,6,1,5,3,7,2,8,4],
         	     [2,8,7,4,1,9,6,3,5],
         	     [3,4,5,2,8,6,1,7,0]]

#transform
grid_pos = (75, 100)
GRID_TRANS = (grid_pos[0], grid_pos[1], WIDTH - 150, HEIGHT - 150)
CELL_SIZE = 50
GRID_SIZE = CELL_SIZE*9

