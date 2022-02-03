from copy import deepcopy
import pygame



RED = (0,100,100)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:     #maximum depth reach or someone has won, returning position along with evaluating the position
        return position.evaluate(), position            #position where we move to
    
    if max_player:                  #maximizing player..
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]     #recursive call to minimax algo
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move


        
        return maxEval, best_move
    else:
        minEval = float('inf')      #minimizing the player
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]          #recursive call to minimax algo
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)        #copy all of the pieces that are stored in board
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()                     #to simulate all possible move of all checkers before any move
    # pygame.time.delay(100)                    #just delay 1 second before AI checkers move

