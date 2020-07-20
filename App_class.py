import pygame
import sys
from Settings import * 
from ButtonClass import *

#create app class
class App:
	def __init__(self):
		pygame.init()
		self.window = pygame.display.set_mode((WIDTH, HEIGHT))
		self.running = True #game variable
		#board making
		self.board = BOARD_2
		self.locked = []
		#other variables
		self.selected = None #box selection variable
		self.mouse_pos = None 
		self.state = "playing" #the state of the game(menu, playing, ended etc.)
		#buttons for each state
		self.playing_buttons = []
		self.menu_buttons = []
		self.end_buttons = []
		self.load()
		#text
		self.render_font = pygame.font.SysFont("arial", CELL_SIZE//2)

	def run(self):
		while self.running:
			if self.state == "playing":
				self.playing_events()
				self.playing_update()
				self.playing_draw()
		pygame.quit()
		sys.exit()

	#### Playing-state Functions ###

	def playing_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False #to quit

			#on click
			if event.type == pygame.MOUSEBUTTONDOWN:
				selected = self.mouse_on_grid(self.mouse_pos) #get position of selected box
				if selected:
					self.selected = selected #store               ^
				else:
					print("Mouse not on grid.")
					self.selected = None

			#on key input
			if event.type == pygame.KEYDOWN:
				if self.selected != None and self.selected not in self.locked:
					if self.is_int(event.unicode):
						self.board[self.selected[1]][self.selected[0]] = int(event.unicode)

	def playing_update(self):
		self.mouse_pos = pygame.mouse.get_pos() #get postition of mouse at every frame

		for button in self.playing_buttons:
			button.update(self.mouse_pos)

		
	def playing_draw(self):
		self.window.fill(BG) #main window

		for button in self.playing_buttons:
			button.draw(self.window)

		if self.selected: #fill selected box
			self.draw_selection(self.window, self.selected)

		self.draw_locked(self.window, self.locked)

		self.draw_numbers(self.window) #function to draw the numbers on screen

		self.draw_grid(self.window) #draw grid
		pygame.display.update()

	### Helper Functions ###

	def is_int(self, value):
		if value.isnumeric():
			return True
		else:
			return False

	def draw_locked(self, window, locked):
		for cell in locked:
			pygame.draw.rect(self.window, LOCKED_CO, (cell[0]*CELL_SIZE+grid_pos[0], cell[1]*CELL_SIZE+grid_pos[1], CELL_SIZE, CELL_SIZE))

	def draw_numbers(self, window):

		for yindex, row in enumerate(self.board):
			for xindex, num in enumerate(row):
				if num != 0:
					pos = [(xindex*CELL_SIZE)+grid_pos[0], (yindex*CELL_SIZE)+grid_pos[1]]
					self.text_to_screen(window, str(num), pos)

	def draw_grid(self, window):
		pygame.draw.rect(window, WHITE, GRID_TRANS, 2) #draw grid box
		for x in range(0, 9): #draw grid lines
			if x % 3 != 0: 
				pygame.draw.line(window, WHITE, (GRID_TRANS[0] + x*(CELL_SIZE), GRID_TRANS[1]), (GRID_TRANS[0] + x*(CELL_SIZE), GRID_TRANS[1] + 450)) #vertical lines
				pygame.draw.line(window, WHITE, (GRID_TRANS[0], GRID_TRANS[1] + x*(CELL_SIZE)), (GRID_TRANS[0] + 450, GRID_TRANS[1] + x*(CELL_SIZE))) # horizontal lines
			else:
				pygame.draw.line(window, WHITE, (GRID_TRANS[0] + x*(CELL_SIZE), GRID_TRANS[1]), (GRID_TRANS[0] + x*(CELL_SIZE), GRID_TRANS[1] + 450), 4) #vertical lines bold
				pygame.draw.line(window, WHITE, (GRID_TRANS[0], GRID_TRANS[1] + x*(CELL_SIZE)), (GRID_TRANS[0] + 450, GRID_TRANS[1] + x*(CELL_SIZE)), 4) #horizontal lines bold

	def mouse_on_grid(self, mouse_pos):
		in_grid = [False, False] 
		if mouse_pos[0] >= grid_pos[0] and mouse_pos[0] <= grid_pos[0] + GRID_SIZE:
			in_grid[0] = True
		if mouse_pos[1] >= grid_pos[1] and mouse_pos[1] <= grid_pos[1] + GRID_SIZE:
			in_grid[1] = True
		if in_grid[0] == True and in_grid[1] == True:
			mouse_pos = list(mouse_pos)
			#manipulate position values as required
			mouse_pos[0] -= grid_pos[0]
			mouse_pos[0] = mouse_pos[0]//CELL_SIZE
			mouse_pos[1] -= grid_pos[1]
			mouse_pos[1] = mouse_pos[1]//CELL_SIZE
			mouse_pos = tuple(mouse_pos)
			return mouse_pos
		else:
			return False

	def draw_selection(self, window, pos): #fill selected box function
		pygame.draw.rect(window, CO_1, ((pos[0]*CELL_SIZE)+grid_pos[0], ( pos[1]*CELL_SIZE)+grid_pos[1],  CELL_SIZE, CELL_SIZE))

	def load_buttons(self):
		self.playing_buttons.append(Button(20, 40, 100, 40))

	def text_to_screen(self, window, text, pos):
		font = self.render_font.render(text, False, WHITE)
		font_width = font.get_width()
		font_height = font.get_height()
		pos[0] += (CELL_SIZE - font_width)//2
		pos[1] += (CELL_SIZE - font_height)//2
		window.blit(font, pos)

	def load(self):
		self.load_buttons()

		#adding locked cells to list
		for yindex, row in enumerate(self.board):
			for xindex, num in enumerate(row):
				if num == 0:
					continue
				self.locked.append([xindex, yindex])
