import pygame as p
import chess

class Dragger:

	""" Dragger is a class that handles the dragging of pieces.
	The first event: Click the piece
	The second event: Drag the piece
	The third event: Drop the piece
	"""
	def __init__(self):
		self.x_coor = 0
		self.y_coor = 0

	def update_position(self, position):
		self.x_coor = position[0] # x coordinate
		self.y_coor = position[1] # y coordinate
