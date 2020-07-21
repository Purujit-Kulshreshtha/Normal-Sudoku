import pygame
from Settings import *

class Button:
	def __init__(self, x, y, width, height, text=None, color=WHITE, high_color=CO_1, function=None, params=None):
		self.image = pygame.Surface((width, height))
		self.pos = (x, y)
		self.rect = self.image.get_rect()
		self.rect.topleft = self.pos
		self.text = text
		self.color = color
		self.high_color = high_color
		self.function = function
		self.params = params
		self.highlighted = False

	def update(self, mouse):
		if self.rect.collidepoint(mouse):
			self.highlighted = True
		else:
			self.highlighted = False

	def draw(self, window):
		if self.highlighted:
			self.image.fill(self.high_color)
		else:
			self.image.fill(self.color)
		window.blit(self.image, self.pos)

	def click(self):
		if self.params:
			self.function(self.params)
		else:
			self.function()
