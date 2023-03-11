import chess
from chess.utils import get_bb_from_square_int
from chess.moves import SQUARE_XRAYS

def mask_own_pieces_upward_range(range_bb: chess.Bitboard, own_pieces: chess.Bitboard):
    """
    Input:
        A range BB (vertical, horizontal or diagonal) from the current position UPWARDS or RIGHTWARD
        and the BB of squares occupied by current player.
    Output:
        BB of squares on that range that the acting player CANNOT move to given its own pieces.
    Note: This function works ONLY for movements from a square i (curreny position) to a square j,
        where i < j, for i,j in [0..63].
        Minus 1 flips the sign of all less significant bits from the LEAST significant 1-bit in player occupied
        For example, subtracting 1 from the binary number 0b1010 gives you 0b1001.
        If you then take the complement of this mask with ~(bitboard2 | (bitboard2 - 1)),
        you get a mask with all the bits set above the most significant bit in bitboard2.
        This mask can be used to filter out any values in bitboard1 that have a bit set below the most significant bit in bitboard2.
    """
    _mask = range_bb & own_pieces
    return range_bb & ~((_mask) | (_mask - 1)) | (_mask)

def mask_own_pieces_downward_range(range_bb: chess.Bitboard, own_pieces: chess.Bitboard):
    """
    Input:
        A range BB (vertical, horizontal or diagonal) from the current position DOWNWARDS or LEFTWARD
        and the BB of squares occupied by current player.
    Output:
        BB of squares on that range that the acting player CANNOT move to given its own pieces.
        Note: This function works ONLY for movements from a square i (curreny position) to a square j,
        where i > j, for i,j in [0..63].
    """
    msb_index = (range_bb & own_pieces).bit_length()
    if msb_index == 0:
        return 0
    # bit_length is counting from 1, index is counting from 0, therefore we subtract 1 from the bit length to get the index
    _mask = get_bb_from_square_int(msb_index-1) - 1
    return (_mask | own_pieces) & range_bb

def mask_own_pieces(current_square: int, directions: list, own_pieces: chess.Bitboard, mask_upwards: bool):
    """
    Input:
        current_position: Bitboard with single 1 that indicates the current position of the piece to be moved.
        directions: list of string that corresponds to keys in XRAYS dictionary.
        own_pieces: bitboard with 1s where the player has pieces.
        mask_upwards: true if we are masking for movements from a square i (curreny position) to a square j,
        where i > j, for i,j in [0..63].
    Output:
        BB of squares on that range that the acting player CANNOT move to given its own pieces.
    """
    masking_function = mask_own_pieces_upward_range if mask_upwards else mask_own_pieces_downward_range
    target_squares = chess.BB_EMPTY
    for direction in directions:
        xray = SQUARE_XRAYS[current_square][direction]
        target_squares |= masking_function(xray, own_pieces)
    return target_squares

def mask_opponent_pieces_upward(range_bb: chess.Bitboard, opponent_pieces: chess.Bitboard):
    """
    Input:
        A range BB (vertical, horizontal or diagonal) from the current position UPWARDS or RIGHTWARD
        and the BB of squares occupied by opponent.
    Output:
        BB of squares on that range that the acting player CANNOT move to given its opponents pieces.
    Note: This function works ONLY for movements from a square i (curreny position) to a square j,
        where i < j, for i,j in [0..63].
    """
    _mask = range_bb & opponent_pieces
    return _mask & (_mask - 1)

def mask_opponent_pieces_downward_range(range_bb: chess.Bitboard, opponent_pieces: chess.Bitboard):
    """
    Input:
        A range BB (vertical, horizontal or diagonal) from the current position DOWNWARDS or LEFTWARD
        and the BB of squares occupied by current player.
    Output:
        BB of squares on that range that the acting player CANNOT move to given its own pieces.
        Note: This function works ONLY for movements from a square i (curreny position) to a square j,
        where i > j, for i,j in [0..63].
    """
    msb_index = (range_bb & opponent_pieces).bit_length()
    if msb_index == 0:
        return 0
    # bit_length is counting from 1, index is counting from 0, therefore we subtract 1 from the bit length to get the index
    _mask = get_bb_from_square_int(msb_index-1) - 1
    return _mask & range_bb

def mask_opponent_pieces(current_square: int, directions: list, opponent_pieces: chess.Bitboard, mask_upwards: bool):
    masking_function = mask_opponent_pieces_upward if mask_upwards else mask_opponent_pieces_downward_range
    target_squares = chess.BB_EMPTY
    for direction in directions:
        xray = SQUARE_XRAYS[current_square][direction]
        target_squares |= masking_function(xray, opponent_pieces)
    return target_squares