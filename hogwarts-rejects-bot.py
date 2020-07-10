#importing things
import chess.engine
import chess
import random
from reconchess import *
import os
##################################################################
STOCKFISH_ENV_VAR = 'STOCKFISH_EXECUTABLE'
class TroutBot(Player):
#this is all from the troutbot script. we are just initalizing the environemtal variable and setting up the chess board
    def __init__(self):
            self.board = None
            self.color = None
            self.my_piece_captured_square = None

        # make sure stockfish environment variable exists
            if STOCKFISH_ENV_VAR not in os.environ:
                raise KeyError(
                    'TroutBot requires an environment variable called "{}" pointing to the Stockfish executable'.format(
                        STOCKFISH_ENV_VAR))

        # make sure there is actually a file
            stockfish_path = os.environ[STOCKFISH_ENV_VAR]
            if not os.path.exists(stockfish_path):
                raise ValueError('No stockfish executable found at "{}"'.format(stockfish_path))

        # initialize the stockfish engine
            self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path, setpgrp=True)
######################################################################################################           
#this next part will check the directories for previous .json files of chess games. 
path = os.getcwd()
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".json")
            print('you are in the correct directory')
        else
            print('please check which directory you are in')
#now we will start the game
def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
self.board = board
    self.color = color
###########################################################################
#next we will define handling if a piece is captured 
def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        # if the opponent captured our piece, remove it from our board.
        self.my_piece_captured_square = capture_square
        if captured_my_piece:
            self.board.remove_piece_at(capture_square)
####################################################################################
#now we will handle dealing with the history of past games to use to our advantage
opponent_moves = history.collect(history.taken_move, history.turns(not self.color))
target_senses = [move.to_square for move in opponent_moves]
#get the first turn and move of the game
turn = history.first_turn()
first-move = history.sense(turn)
if turn.iskeyword('WHITE') = True
   try:
            self.board.turn = self.color
            self.board.clear_stack()
            result = self.engine.play(self.board, chess.engine.Limit(time=0.5))
            return result.move
        except chess.engine.EngineTerminatedError:
            print('Stockfish Engine died')
        except chess.engine.EngineError:
            print('Stockfish Engine bad state at "{}"'.format(self.board.fen()))

else
    #this will be a random move
    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> \
            Optional[Square]:
             # if our piece was just captured, sense where it was captured
        if self.my_piece_captured_square:
            return self.my_piece_captured_square
        for square, piece in self.board.piece_map().items():
                if piece.color == self.color:
                 sense_actions.remove(square)
            return random.choice(sense_actions)
             # if we might capture a piece when we move, sense where the capture will occur
        future_move = self.choose_move(move_actions, seconds_left)
        if future_move is not None and self.board.piece_at(future_move.to_square) is not None:
            return future_move.to_square
        #otherwise we will base our move on the opponents last move
        turn = history.last_turn()
    def choose_move_(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        return random.choice(move_actions + [None])
              
###############################################################################################################
#now we will update our board
def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        # add the pieces in the sense result to our board
        for square, piece in sense_result:
            self.board.set_piece_at(square, piece)
#################################################################################################################
 #next we will analyse the board to determine our next movee
def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        # if we might capture a piece when we move, sense where the capture will occur
        future_move = self.choose_move(move_actions, seconds_left)
        if future_move is not None and self.board.piece_at(future_move.to_square) is not None:
            return future_move.to_square
        #otherwise we will base our move on the opponents last move
        turn = history.last_turn()
        for turn in history.turns(self.color):
            if history.has_move(turn):
                move = history.requested_move(turn)
                bboard = history.truth_board_before_move(turn)
                board = chess.Board()
                #castle to protect the king 
                if board.castling_rights == True:
                    chess.Move(from_square: Square, to_square: Square, promotion: Optional[PieceType] = None, drop: Optional[PieceType] = None)
                    chess.ROOK
                    from_square: chess.A1 
                    to_square: chess.C1
                    moving = uci ()
                    board.push(moving)
                else: 
                    #do a random move here using the stockfish engine
                    try:
                    self.board.turn = self.color
                     self.board.clear_stack()
                    result = self.engine.play(self.board, chess.engine.Limit(time=0.5))
                     return result.move
                    except chess.engine.EngineTerminatedError:
                    print('Stockfish Engine died')
                    except chess.engine.EngineError:
                    print('Stockfish Engine bad state at "{}"'.format(self.board.fen()))
                    notify_opponent_move_results(game: reconchess.game.Game, player: reconchess.player.Player):

        # if all else fails, pass
        return None


                       
                #based off of this information, try to take the king
        enemy_king_attackers = self.board.attackers(self.color, enemy_king_square)
        if enemy_king_attackers:
            attacker_square = enemy_king_attackers.pop()
            return chess.Move(attacker_square, enemy_king_square)
        # otherwise, try to move with the stockfish chess engine
        try:
            self.board.turn = self.color
            self.board.clear_stack()
            result = self.engine.play(self.board, chess.engine.Limit(time=0.5))
            return result.move
        except chess.engine.EngineTerminatedError:
            print('Stockfish Engine died')
        except chess.engine.EngineError:
            print('Stockfish Engine bad state at "{}"'.format(self.board.fen()))
        notify_opponent_move_results(game: reconchess.game.Game, player: reconchess.player.Player):

        # if all else fails, pass
        return None
#########################################################################################################
#closing out the game and recording the results
    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move],
                           captured_opponent_piece: bool, capture_square: Optional[Square]):
        # if a move was executed, apply it to our board
        if taken_move is not None:
            self.board.push(taken_move)

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        try:
            # if the engine is already terminated then this call will throw an exception
            self.engine.quit()
        except chess.engine.EngineTerminatedError:
            pass
        
    