import random
from reconchess import *
from operator import itemgetter

Strategies_white = [
    # Opening move, knight to protect weak spot in case of Scholar's Mate
    [chess.Move(chess.G1, chess.H3)],
    # Queen side knight attack method #1
    [chess.Move(chess.B1, chess.C3), chess.Move(chess.C3, chess.B5), chess.Move(chess.B5, chess.D6),
     chess.Move(chess.D6, chess.E8)],
    # Queen side knight attack method #2
    [chess.Move(chess.B1, chess.C3), chess.Move(chess.C3, chess.E4), chess.Move(chess.E4, chess.F6),
     chess.Move(chess.F6, chess.E8)],
    # Scholar's Mate
    [chess.Move(chess.E2, chess.E4), chess.Move(chess.F1, chess.C4), chess.Move(chess.D1, chess.H5), chess.Move(
        chess.C4, chess.F7), chess.Move(chess.F7, chess.E8), chess.Move(chess.H5, chess.E8)],
    # Castling
    [chess.Move(chess.E1, chess.G1)],
    # King side knight attack
    [chess.Move(chess.H3, chess.F4), chess.Move(chess.D1, chess.H5), chess.Move(
        chess.C4, chess.F7), chess.Move(chess.F7, chess.E8), chess.Move(chess.H5, chess.E8)],
    # Bring out the other bishop
    [chess.Move(chess.D2, chess.D3), chess.Move(chess.C1, chess.G5)]
]

Strategies_black = [
    # Opening move, knight to protect weak spot in case of Scholar's Mate
    [chess.Move(chess.G1, chess.H3)],
    # Queen side knight attack method #1
    [chess.Move(chess.B8, chess.C6), chess.Move(chess.C6, chess.B4), chess.Move(chess.B4, chess.D3),
     chess.Move(chess.D3, chess.E1)],
    # Queen side knight attack method #2
    [chess.Move(chess.B8, chess.C6), chess.Move(chess.C6, chess.E5), chess.Move(chess.E5, chess.F3),
     chess.Move(chess.F3, chess.E1)],
    # Scholar's Mate
    [chess.Move(chess.E7, chess.E5), chess.Move(chess.F8, chess.C5), chess.Move(chess.D8, chess.H4), chess.Move(
        chess.C5, chess.F2), chess.Move(chess.F2, chess.E1), chess.Move(chess.H4, chess.E1)],
    # Castling
    [chess.Move(chess.E8, chess.G8)],
    # King side knight attack
    [chess.Move(chess.H6, chess.F5), chess.Move(chess.D8, chess.H4), chess.Move(
        chess.C5, chess.F2), chess.Move(chess.F2, chess.E1), chess.Move(chess.H4, chess.E1)],
    # Bring out the other bishop
    [chess.Move(chess.D7, chess.D6), chess.Move(chess.C8, chess.G4)]]


class omnipotentbot_1(Player):
    def __init__(self):
        self.move_sequence = list(map(itemgetter(0), Strategies_white))
        self.turn = None
        self.board = None
        self.color = None
        self.my_piece_captured_square = None

    
    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        pass

    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        pass

    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> Square:
        return random.choice(sense_actions)

    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        pass

    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        while len(self.move_sequence) > 0 and self.move_sequence[0] not in move_actions:
            self.move_sequence.pop(0)
        if len(self.move_sequence) == 0:
            return None
        else:
            return self.move_sequence.pop(0)

    def handle_move_result(self, requested_move: chess.Move, taken_move: chess.Move,
                           captured_opponent_piece: bool, capture_square: Optional[Square]):
        print(self.move_sequence)

    pass

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        print(self.board)
        pass
