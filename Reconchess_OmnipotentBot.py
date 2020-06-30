# Modified RandomBot with Various strategies
import random
from reconchess import *
"""
Strategies = [
    # Opening move, knight to protect weak spot in case of Scholar's Mate
    [chess.Move(chess.G1, chess.H3)],
    #[chess.Move.from_uci('g1h3')],
    #[chess.Move(chess.G1,chess.H3)],
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

"""

class RandomBot(Player):
    Strategies = None
    def __init__(self):
        # for i in (Strategies):
        #    self.move_sequence=i
        #    print(self.move_sequence)
        #    test_strat.append(i)
        # print(test_strat)
        #self.move_sequence = Player.choose_move(self,Strategies,0.5)
        self.move_sequence = []
        self.board = None
        self.color = None
        self.my_piece_captured_square = None
        #self.move_sequence=None
        self.Strategies=[
            # Opening move, knight to protect weak spot in case of Scholar's Mate
            [chess.Move(chess.G1, chess.H3)],
            # [chess.Move.from_uci('g1h3')],
            # [chess.Move(chess.G1,chess.H3)],
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

    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        self.board = board
        self.color = color
        print(self.color)
        if self.color == chess.BLACK:
            self.board = board.mirror()
            print(self.board)
            return print("BLACK")
        else:
            return print("White")
        print(self.board)
        pass

    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        # print(capture_square)
        if captured_my_piece:
            self.board.remove_piece_at(capture_square)
        pass

    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> \
            Optional[Square]:
        return random.choice(sense_actions)

    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        for square, piece in sense_result:
            self.board.set_piece_at(square, piece)
            # if there is a piece at E7, it will be removed-not sure if it works perfectly, but not running error
            if piece is None:
                self.board.remove_piece_at(chess.E7)
            else:
                self.board.set_piece_at(square, piece)
        pass

    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        #print(self.Strategies)
        #for moves in move_actions:
        #    print("This is a move",moves)
        # return random.choice(move_actions + [None])
        #print(move_actions)
        #print(move_actions)
        enemy_king = self.board.king(not self.color)
        if enemy_king:
            enemy_king_attack = self.board.attackers(self.color, enemy_king)
            if enemy_king_attack:
                attack_square = enemy_king_attack.pop()
                return chess.Move(attack_square, enemy_king)
        #if 'g8h6' in move_actions:
        #    print("It is working")
        #pass
        for i in self.Strategies:
            idx=None
            for j in i:
                #self.move_sequence.append(j)
                #move_actions.append(self.move_sequence)
                #move_actions.append(j)
                #print(move_actions[-1])
                if j in move_actions:
                    print("It is here")
                    idx=move_actions.index(j)
                    self.Strategies.push(j)
                    return (move_actions[idx])
                #print(move_actions)
                #print(self.move_sequence)
                #print(self.move_sequence.pop(0))
                #return(self.move_sequence.move)
                #return(self.move_sequence.pop(0))
                #return (move_actions[-1])
                else:
                    print("It is not working")
                    continue
            return(self.Strategies[0][0])



    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move],
                           captured_opponent_piece: bool, capture_square: Optional[Square]):
            #return(self.choice.move_sequence)
        pass

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        print(self.board)
        pass
