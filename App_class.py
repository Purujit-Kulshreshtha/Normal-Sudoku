import pygame
import sys
from Settings import * 

class App:
	def __init__(self):
		pygame.init()
		self.window = pygame.display.set_mode((WIDTH, HEIGHT))
		self.running = True
		self.board = BOARD

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

	def update(self):
		pass

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
