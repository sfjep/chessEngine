
import pygame as p
import chess

class GUI:
	WIDTH = HEIGHT = 512
	DIMENSION = 8
	SQUARE_SIZE = HEIGHT // DIMENSION
	MAX_FPS = 15
	IMAGES = {}

	def __init__(self):
		p.init()
		self.screen = p.display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = p.time.Clock()
		self.screen.fill(p.Color("white"))

	def load_images(self):
		for piece in chess.PIECE_STRINGS:
			self.IMAGES[piece] = p.transform.scale(
				p.image.load(f"src/chess/images/{piece}.png"),
				(self.SQUARE_SIZE, self.SQUARE_SIZE)
			)

	def run(self, board):
		running = True
		while running:
			for e in p.event.get():
				if e.type==p.QUIT:
					running=False
			self.draw_board()
			self.draw_pieces(board)
			self.clock.tick(self.MAX_FPS)
			p.display.flip()

	def draw_board(self):
		colors = [p.Color(248,220,180), p.Color(180,134,99)]
		for row in range(self.DIMENSION):
			for column in range(self.DIMENSION):
				color = colors[((row+column)%2)]
				p.draw.rect(
					self.screen,
					color,
					p.Rect(
						column * self.SQUARE_SIZE,
						row * self.SQUARE_SIZE,
						self.SQUARE_SIZE,
						self.SQUARE_SIZE
					)
				)

	def draw_pieces(self, board):
		"""
		Split into separate methods as we may want to do piece highlighting
		"""
		for row in range(self.DIMENSION):
			for column in range(self.DIMENSION):
				piece = board.get_piece_name_from_board_dim(row, column)
				if piece != " ":
					self.screen.blit(
						self.IMAGES[piece],
						p.Rect(
							column * self.SQUARE_SIZE,
							row * self.SQUARE_SIZE,
							self.SQUARE_SIZE * 0.8,
							self.SQUARE_SIZE * 0.8
						)
					)