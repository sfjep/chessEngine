import pygame as p
import chess
import sys
from chess.gui.dragger import Dragger

class GUI:
	WIDTH = HEIGHT = 512
	DIMENSION = 8
	SQUARE_SIZE = HEIGHT // DIMENSION
	MAX_FPS = 60
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
		clock = p.time.Clock()  # to control the game's frame rate
		self.dragging = False
		
		while True:
			clock.tick(self.MAX_FPS)
			self.show_background()
			self._draw_pieces(state.board)

			for event in p.event.get():
				if event.type == p.MOUSEBUTTONDOWN:
					position = event.pos
					clicked_rank = position[1] // self.SQUARE_SIZE
					clicked_file = position[0] // self.SQUARE_SIZE

					if state.board.square_has_piece(clicked_rank, clicked_file):
						print("Clicked on a piece")
						self.dragging = True
						self.original_position = (clicked_rank, clicked_file)

						(flipped_rank, flipped_file) = self.get_rank_and_file_from_position(event.pos)
						print("Clicked rank: ", clicked_rank)
						print("Flipped rank: ", flipped_rank)

						print("Clicked file: ", clicked_file)
						print("Flipped file: ", flipped_file)
						valid_moves = state.get_actions_from_origin_square(flipped_rank, flipped_file)
						print(valid_moves)
						self.draw_valid_moves(valid_moves)
						piece = state.board.get_piece_name_from_board_dim(clicked_rank, clicked_file)
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

	def _get_x_coordinate(self):
		return self.dragger.x_coor // self.SQUARE_SIZE

	def _get_y_coordinate(self):
		return self.dragger.y_coor // self.SQUARE_SIZE
	
	def draw_valid_moves(self, valid_moves):
		for valid_move in valid_moves:
			print(valid_move)
			rank, file = self.get_rank_file_from_move(valid_move)
			print("rank, file", rank, file)
			p.draw.rect(
				self.screen,
				self.VALID_MOVE_COLOR,
				p.Rect(
					file * self.SQUARE_SIZE,
					rank * self.SQUARE_SIZE,
					self.SQUARE_SIZE,
					self.SQUARE_SIZE,
				)
			)

	def get_rank_and_file_from_position(self, event_pos):
		return (7 - event_pos[1] // self.SQUARE_SIZE, event_pos[0] // self.SQUARE_SIZE)
	