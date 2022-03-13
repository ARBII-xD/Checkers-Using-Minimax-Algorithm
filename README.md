# A checkers AI using the minimax algorithm.

## ABOUT THE GAME:
It is the modern implementation of the classical Checkers game. It is 
implemented in python using Minimax Algorithm with the help of 
popular module pygame.

## WORKING OF MINIMAX ALGORITHM
The Minimax algorithm relies on systematic searching, or more accurately said - on brute force and a simple evaluation function. Let's assume that every time during deciding the next move we search through a whole tree, all the way down to leaves. Effectively we would look into all the possible outcomes and every time we would be able to determine the best possible move.

However, for non-trivial games, that practice is inapplicable. Even searching to a certain depth sometimes takes an unacceptable amount of time. Therefore, Minimax applies search to a fairly low tree depth aided with appropriate heuristics, and a well designed, yet simple evaluation function.

With this approach we lose the certainty in finding the best possible move, but the majority of cases the decision that minimax makes is much better than any human's.

Now, let's take a closer look at the evaluation function we've previously mentioned. In order to determine a good (not necessarily the best) move for a certain player, we have to somehow evaluate nodes (positions) to be able to compare one to another by quality.

The evaluation function is a static number, that in accordance with the characteristics of the game itself, is being assigned to each node (position).

It is important to mention that the evaluation function must not rely on the search of previous nodes, nor of the following. It should simply analyze the game state and circumstances that both players are in.

It is necessary that the evaluation function contains as much relevant information as possible, but on the other hand - since it's being calculated many times - it needs to be simple.

Usually it maps the set of all possible positions into symmetrical segment: 
F:P→[−M,M]

Value of M is being assigned only to leaves where the winner is the first player, and value -M to leaves where the winner is the second player.

In zero-sum games, the value of the evaluation function has an opposite meaning - what's better for the first player is worse for the second, and vice versa. Hence, the value for symmetric positions (if players switch roles) should be different only by sign.

A common practice is to modify evaluations of leaves by subtracting the depth of that exact leaf, so that out of all moves that lead to victory the algorithm can pick the one that does it in the smallest number of steps (or picks the move that postpones loss if it is inevitable).

## • GAME PLAY:
Checkers is played with two players sitting across from each other the 
board is positioned with the light-colored square in the bottom right 
corner the checkers for each player are set up on the dark colored 
squaresthe object of the game is to capture all your opponent’s checkers 
or trap your opponent so no move can be made.
Player 1 begins the game by making the first move the checkers can 
move diagonally forward one space player 2 moves a checker for his turn 
players take turns moving one checker at a time a checker is captured by 
jumping the opponent's checker with your own checker a jump can be 
made when the square behind your opponent's checker is open more 
than one checker can be captured during a turn by multiple jumps being
made with the same checker player 2 is able to capture two of player 1's
checkers on this turn players continue to take turns making moves
skipping ahead if a player is able to move his checker to the other side of
the board that checker is kinged player 2 got a checker to the other side 
of the board and a checker is stacked on top to signify the checker being 
kinged a king checker can move forwards and backwards on the board
skipping ahead again player 2 is able to capture player 1's last two 
checkers and wins this game

## • GAME RULES:
A single checker can only move and jump going forward if a player can 
make a capture, he has to make the capture if a player cannot make a 
move, he loses that wraps up how to play checkers.
