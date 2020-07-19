import pygame
import sys
from Settings import * 

class App:
	def __init__(self):
		pygame.init()
		self.window = pygame.display.set_mode((WIDTH, HEIGHT))
		self.running = True
		self.board = BOARD
		self.selected = None
		self.mouse_pos = None

	def run(self):
		while self.running:
			self.events()
			self.update()
			self.draw()
		pygame.quit()
		sys.exit()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				selected = self.mouse_on_grid(self.mouse_pos)
				if selected:
					print("Mouse on grid.")
				else:
					print("Mouse not on grid.")

	def update(self):
		self.mouse_pos = pygame.mouse.get_pos()
		

	def draw(self):
		self.window.fill(BG)
		self.draw_grid(self.window)
		pygame.display.update()

	def draw_grid(self, window):
		pygame.draw.rect(window, WHITE, GRID_TRANS, 2)
		for x in range(0, 9):
			if x % 3 != 0:
				pygame.draw.line(window, WHITE, (GRID_TRANS[0] + x*(CELL_SIZE), GRID_TRANS[1]), (GRID_TRANS[0] + x*(CELL_SIZE), GRID_TRANS[1] + 450)) #vertical lines
				pygame.draw.line(window, WHITE, (GRID_TRANS[0], GRID_TRANS[1] + x*(CELL_SIZE)), (GRID_TRANS[0] + 450, GRID_TRANS[1] + x*(CELL_SIZE))) # horizontal lines
			else:
				pygame.draw.line(window, WHITE, (GRID_TRANS[0] + x*(CELL_SIZE), GRID_TRANS[1]), (GRID_TRANS[0] + x*(CELL_SIZE), GRID_TRANS[1] + 450), 2) #vertical lines bold
				pygame.draw.line(window, WHITE, (GRID_TRANS[0], GRID_TRANS[1] + x*(CELL_SIZE)), (GRID_TRANS[0] + 450, GRID_TRANS[1] + x*(CELL_SIZE)), 2) #horizontal lines bold

	def mouse_on_grid(self, mouse_pos):
		in_grid = [False, False]
		if mouse_pos[0] >= grid_pos[0] and mouse_pos[0] <= grid_pos[0] + GRID_SIZE:
			in_grid[0] = True
		if mouse_pos[1] >= grid_pos[1] and mouse_pos[1] <= grid_pos[1] + GRID_SIZE:
			in_grid[1] = True
		if in_grid[0] == True and in_grid[1] == True:
			return True
		else:
			return False
