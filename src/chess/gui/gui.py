import pygame as p
import chess
import sys
from chess.gui.dragger import Dragger

class GUI:
	WIDTH = HEIGHT = 512
	DIMENSION = 8
	SQUARE_SIZE = HEIGHT // DIMENSION
	MAX_FPS = 15
	IMAGES = {}

	def __init__(self):
		p.init()
		self.screen = p.display.set_mode((self.WIDTH, self.HEIGHT))
		p.display.set_caption('Chess')
		self._load_images()
		self.dragger = Dragger()

	def _load_images(self):
		for piece in chess.PIECE_STRINGS:
			self.IMAGES[piece] = p.transform.scale(
				p.image.load(f"src/chess/images/{piece}.png"),
				(self.SQUARE_SIZE, self.SQUARE_SIZE)
			)

	def run(self, state):
		while True:
			self.show_background()
			self._draw_pieces(state.board)
			for event in p.event.get():

				# Click
				if event.type == p.MOUSEBUTTONDOWN:
					self.dragger.update_position(event.pos)
					clicked_rank = self._get_y_coordinate()
					clicked_file = self._get_x_coordinate()

					if state.board.square_has_piece(clicked_rank, clicked_file):
						print("Clicked on a piece")
						# Get piece object - how?! Perhaps Square class??


				# Drag piece
				elif event.type == p.MOUSEMOTION:
					pass

				# Drop
				elif event.type == p.MOUSEBUTTONUP:
					pass

				# Quit
				elif event.type == p.QUIT:
					p.quit()
					sys.exit()

				p.display.update()

	# Show methods
	def show_background(self):
		for row in range(self.DIMENSION):
			for col in range(self.DIMENSION):
				color = self._get_square_color(row, col)
				p.draw.rect(
					self.screen,
					color,
					p.Rect(
						col * self.SQUARE_SIZE,
						row * self.SQUARE_SIZE,
						self.SQUARE_SIZE,
						self.SQUARE_SIZE
					)
				)

	@staticmethod
	def _get_square_color(row: int, col: int) -> p.Color:
		if (row+col)%2==0:
			return p.Color(248,220,180)
		else:
			return p.Color(180,134,99)


	def _draw_pieces(self, board):
		"""
		Split into separate methods as we may want to do piece highlighting
		"""
		for row in range(self.DIMENSION):
			for col in range(self.DIMENSION):
				piece = board.get_piece_name_from_board_dim(row, col)
				if piece != " ":
					self.screen.blit(
						self.IMAGES[piece],
						p.Rect(
							col * self.SQUARE_SIZE,
							row * self.SQUARE_SIZE,
							self.SQUARE_SIZE * 0.8,
							self.SQUARE_SIZE * 0.8
						)
					)

	def _get_x_coordinate(self):
		return self.dragger.x_coor // self.SQUARE_SIZE

	def _get_y_coordinate(self):
		return self.dragger.y_coor // self.SQUARE_SIZE