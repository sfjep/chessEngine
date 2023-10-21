import pygame as p
import chess
import sys
from chess.gui.dragger import Dragger
from chess.utils import get_rank_file_from_square_int

class GUI:
	WIDTH = HEIGHT = 512
	DIMENSION = 8
	SQUARE_SIZE = HEIGHT // DIMENSION
	MAX_FPS = 12
	IMAGES = {}
	VALID_MOVE_COLOR = p.Color(235,155,155)
	LIGHT_SQ_COLOR = p.Color(248,220,180)
	DARK_SQ_COLOR = p.Color(180,134,99)

	def __init__(self):
		p.init()
		self.screen = p.display.set_mode((self.WIDTH, self.HEIGHT))
		p.display.set_caption('Chess')
		self._load_images()
		self.dragger = Dragger()
		self.dragging = False
		self.original_position = None

	def _load_images(self):
		for piece in chess.PIECE_STRINGS:
			self.IMAGES[piece] = p.transform.scale(
				p.image.load(f"src/chess/images/{piece}.png"),
				(self.SQUARE_SIZE, self.SQUARE_SIZE)
			)

	def run(self, state):
		clock = p.time.Clock()
		self.dragging = False
		self.valid_moves_drawn = False
		self.valid_moves = []

		while True:
			clock.tick(self.MAX_FPS)
			self.show_background()
			self._draw_pieces(state.board)

			if self.dragging:
				if not self.valid_moves_drawn:
					self.valid_moves = state.get_actions_from_origin_square(7 - self.clicked_rank, self.clicked_file)
					self.valid_moves_drawn = True  # Set the flag to True after drawing them once

			for event in p.event.get():
				if event.type == p.MOUSEBUTTONDOWN:
					position = event.pos
					self.clicked_rank = position[1] // self.SQUARE_SIZE
					self.clicked_file = position[0] // self.SQUARE_SIZE

					if state.board.square_has_piece(self.clicked_rank, self.clicked_file):
						print("Clicked on a piece")
						self.dragging = True
						self.original_position = (self.clicked_rank, self.clicked_file)
						self.valid_moves = state.get_actions_from_origin_square(7 - self.clicked_rank, self.clicked_file)

						print("Clicked rank: ", self.clicked_rank)
						print("Clicked file: ", self.clicked_file)
						piece = state.board.get_piece_name_from_board_dim(self.clicked_rank, self.clicked_file)
						self.dragger.update_position(position, self.IMAGES[piece])

				# Drag piece
				elif event.type == p.MOUSEMOTION:
					if self.dragging:
						self.dragger.update_position(event.pos)

				# Drop
				elif event.type == p.MOUSEBUTTONUP:
					if self.dragging:

						# Logic for placing the piece or reverting the move if it's invalid
						new_position = (event.pos[1] // self.SQUARE_SIZE, event.pos[0] // self.SQUARE_SIZE)

						# If the move is invalid, you can set new_position to original_position to revert the piece
						self.dragging = False
						self.valid_moves_drawn = False  # Reset the flag when the piece is dropped
						self.valid_moves = []  # Clear the valid moves

					self.dragger.clear()  # clear the piece from the dragger

				# Quit
				elif event.type == p.QUIT:
					p.quit()
					sys.exit()

			if self.dragging and self.dragger.get_piece():
				self.screen.blit(self.dragger.get_piece(), (self.dragger.x_coor - self.SQUARE_SIZE // 2, self.dragger.y_coor - self.SQUARE_SIZE // 2))

			p.display.flip()


	# Show methods
	def show_background(self):
		for rank in range(self.DIMENSION):
			for file in range(self.DIMENSION):
				if self.dragging and ((7-rank) * 8 + file) in self.valid_moves:
					color = self.VALID_MOVE_COLOR
				else:
					color = self._get_square_color(rank, file)
				p.draw.rect(
					self.screen,
					color,
					p.Rect(
						file * self.SQUARE_SIZE,
						rank * self.SQUARE_SIZE,
						self.SQUARE_SIZE,
						self.SQUARE_SIZE
					)
				)

	def _get_square_color(self, rank: int, file: int) -> p.Color:
		if (rank+file)%2==0:
			return self.LIGHT_SQ_COLOR
		else:
			return self.DARK_SQ_COLOR


	def _draw_pieces(self, board):
		"Split into separate methods as we may want to do piece highlighting"
		for rank in range(self.DIMENSION):
			for file in range(self.DIMENSION):
				if self.dragging and (rank, file) == self.original_position:
					# Skip drawing the piece being dragged
					continue
				piece = board.get_piece_name_from_board_dim(rank, file)
				if piece != " ":
					self.screen.blit(
						self.IMAGES[piece],
						p.Rect(
                            file * self.SQUARE_SIZE,
                            rank * self.SQUARE_SIZE,
                            self.SQUARE_SIZE * 0.8,
                            self.SQUARE_SIZE * 0.8
                        )
                    )

	def draw_valid_moves(self, valid_moves):
		print(valid_moves)
		for valid_move in valid_moves:
			rank, file = get_rank_file_from_square_int(valid_move)
			p.draw.rect(
				self.screen,
				self.VALID_MOVE_COLOR,
				p.Rect(
					file * self.SQUARE_SIZE,
					(7-rank) * self.SQUARE_SIZE,
					self.SQUARE_SIZE,
					self.SQUARE_SIZE,
				)
			)
			p.display.update()
