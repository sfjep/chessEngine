import pygame as p
import chess
import sys
from chess.utils import convert_rank_and_file_to_square_int
from chess.gui.dragger import Dragger
from chess.gui.button import Button
from chess.audio import Audio
from chess.action import ActionType

class GUI:
	FULL_WIDTH = 1920
	FULL_HEIGHT = 1080
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
		display_info = p.display.Info()
		self.FULL_WIDTH, self.FULL_HEIGHT = display_info.current_w, display_info.current_h
		self.chess_screen = p.Surface((self.WIDTH, self.HEIGHT))

		self.full_screen = p.display.set_mode((self.FULL_WIDTH, self.FULL_HEIGHT), p.FULLSCREEN)

		p.display.set_caption('Chess')
		self._load_images()
		self.dragger = Dragger()
		self.revert_button = Button("Undo Move", (50, 400), (200, 50))
		self.dragging = False
		self.original_position = None
		self.audio = Audio()

	def _load_images(self):
		for piece in chess.PIECE_STRINGS:
			self.IMAGES[piece] = p.transform.scale(
				p.image.load(f"src/chess/images/{piece}.png"),
				(self.SQUARE_SIZE, self.SQUARE_SIZE)
			)

	def run(self, state):
		clock = p.time.Clock()
		self.dragging = False
		self.possible_actions_drawn = False
		self.possible_actions = []

		while True:
			clock.tick(self.MAX_FPS)
			self.destination_action_dict = {action.destination_square : action for action in self.possible_actions}
			self.show_background()
			self._draw_pieces(state.board)

			if self.dragging:
				if not self.possible_actions_drawn:
					self.possible_actions_drawn = True  # Set the flag to True after drawing them once

			for event in p.event.get():
				if event.type == p.MOUSEBUTTONDOWN:
					position = event.pos

					if event.button == 1:
						print(self.revert_button.is_clicked(position))
						if self.revert_button.is_clicked(position):
							state = state.undo_action()

					if position[0] >= (self.FULL_WIDTH - self.WIDTH) and position[1] <= self.HEIGHT:
						self.clicked_rank = self.gui_row_to_rank(position[1])
						self.clicked_file = self.gui_col_to_file(position[0])

						if state.board.square_has_piece(7-self.clicked_rank, self.clicked_file):
							print("Clicked on a piece")
							self.dragging = True
							self.original_position = (7-self.clicked_rank, self.clicked_file)
							self.possible_actions = state.get_actions_from_origin_square(self.clicked_rank, self.clicked_file)

							print("Clicked rank: ", self.clicked_rank)
							print("Clicked file: ", self.clicked_file)
							piece = state.board.get_piece_name_from_board_dim(self.clicked_rank, self.clicked_file)
							self.dragger.update_position(position, self.IMAGES[piece])

				# Drag piece
				elif event.type == p.MOUSEMOTION:
					if self.dragging:
						translated_pos = (event.pos[0] - (self.FULL_WIDTH - self.WIDTH), event.pos[1])
						self.dragger.update_position(translated_pos)

				# Drop
				elif event.type == p.MOUSEBUTTONUP:
					if self.dragging:

						# Logic for placing the piece or reverting the move if it's invalid
						rank = self.gui_row_to_rank(event.pos[1])
						file = self.gui_col_to_file(event.pos[0])
						dest_sq = convert_rank_and_file_to_square_int(rank, file)
						try:
							action = self.destination_action_dict[dest_sq]
							if action.type == ActionType.ATTACK or action.type == ActionType.EN_PASSANT:
								Audio.capture()
							else:
								Audio.move()
							state.apply_action(self.destination_action_dict[dest_sq])
						except KeyError:
							print('Invalid location or color')
							pass
						# print(new_position)

						# If the move is invalid, you can set new_position to original_position to revert the piece
						self.dragging = False
						self.possible_actions_drawn = False  # Reset the flag when the piece is dropped
						self.possible_actions = []  # Clear the valid moves

					self.dragger.clear()  # clear the piece from the dragger

				# Quit
				elif event.type == p.QUIT:
					p.quit()
					sys.exit()

			if self.dragging and self.dragger.get_piece():
				self.chess_screen.blit(self.dragger.get_piece(), self.dragger.get_position_tuple(self.SQUARE_SIZE))


			self.render_settings(state)
			self.full_screen.blit(self.chess_screen, (self.FULL_WIDTH - self.WIDTH, 0))
			p.display.flip()


	# Show methods
	def show_background(self):
		for rank in range(self.DIMENSION):
			for file in range(self.DIMENSION):
				if self.dragging and ((7-rank) * 8 + file) in self.destination_action_dict.keys():
					color = self.VALID_MOVE_COLOR
				else:
					color = self._get_square_color(rank, file)
				p.draw.rect(
					self.chess_screen,
					color,
					p.Rect(
						file * self.SQUARE_SIZE,
						rank * self.SQUARE_SIZE,
						self.SQUARE_SIZE,
						self.SQUARE_SIZE
					)
				)

	def gui_col_to_file(self, event_pos):
		return (event_pos - (self.FULL_WIDTH - self.WIDTH)) // self.SQUARE_SIZE

	def gui_row_to_rank(self, event_pos):
		return (7-event_pos // self.SQUARE_SIZE)

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
				piece = board.get_piece_name_from_board_dim(7-rank, file)
				if piece != " ":
					self.chess_screen.blit(
						self.IMAGES[piece],
						p.Rect(
                            file * self.SQUARE_SIZE,
                            rank * self.SQUARE_SIZE,
                            self.SQUARE_SIZE * 0.8,
                            self.SQUARE_SIZE * 0.8
                        )
                    )

	def render_settings(self, state):
		# Create back screen
		self.full_screen.fill(p.Color('black'), (0, 0, self.FULL_WIDTH - self.WIDTH, self.FULL_HEIGHT))

        # Set the fonts for the settings text
		font_header = p.font.Font(None, 36)
		font_text = p.font.Font(None, 28)

		header = font_header.render('Game Settings', True, p.Color('white'))
		fen_str = font_text.render('FEN: ' + state.fen, True, p.Color('white'))
		halfmove_count = font_text.render('Halfmove count: ' + str(state.halfmove_count), True, p.Color('white'))
		move_count = font_text.render('Move count: ' + str(state.move_count), True, p.Color('white'))
		is_check = font_text.render(f'In check: ' + str(state.in_check), True, p.Color('white'))
		numberOfPlayerMoves = font_text.render(f'#: {len(state.get_legal_moves())}', True, p.Color('white'))

		self.full_screen.blit(header, (50, 50))
		self.full_screen.blit(fen_str, (50, 100))
		self.full_screen.blit(halfmove_count, (50, 150))
		self.full_screen.blit(move_count, (50, 200))
		self.full_screen.blit(is_check, (50, 250))
		self.full_screen.blit(numberOfPlayerMoves, (50, 300))
		self.revert_button.draw(self.full_screen)

		# If there are valid moves, render them
		if self.possible_actions:
			# Construct the string for valid moves
			actions_string = ", ".join(str(move) for move in self.possible_actions)
			actions_surface = font_text.render('Possible actions: ' + actions_string, True, p.Color('white'))
			self.full_screen.blit(actions_surface, (50, 350))

		# if state.opponent_moves:
		# 	actions_string = ", ".join(str(move) for move in state.opponent_moves)
		# 	actions_surface = font_text.render('Opponent moves: ' + actions_string, True, p.Color('white'))
		# 	self.full_screen.blit(actions_surface, (50, 600))

        # Redraw the chess screen on the right side
		self.full_screen.blit(self.chess_screen, (self.FULL_WIDTH - self.WIDTH, self.FULL_HEIGHT))

        # Update the display
		p.display.flip()