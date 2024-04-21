import numpy as np

def create_blocker_bitboards(movement_bb: int):
	"""This function generates blocker bitboards for a given movement bitboard."""

	# Create an array with the square indices of the movement bitboard
	movement_square_indices = np.array([], dtype=int)
	for i in range(64):
		if ((movement_bb >> i) & 1) == 1:
			movement_square_indices = np.append(movement_square_indices, i)

	# Create the blocker bitboards
	number_of_blocker_arrangements = 1 << movement_square_indices.size
	blocker_bitboards = np.zeros(number_of_blocker_arrangements, dtype=int)

	# For each blocker arrangement
	for blocker_arrangement_idx in range(number_of_blocker_arrangements):

		# For each square in the movement bitboard
		for bit_idx in range(movement_square_indices.size):

			# Check if the bit is set in the pattern
			bit = (blocker_arrangement_idx >> bit_idx) & 1

			# If the bit is set, set the corresponding bit in the blocker bitboard
			blocker_bitboards[blocker_arrangement_idx] |= bit << movement_square_indices[bit_idx]

	return blocker_bitboards

