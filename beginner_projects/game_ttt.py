import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)] #we will use a single list to rep 3x3 board 
        self.current_winner = None

    def print_board(self):
        # this is getting the rows
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print("| " + " | ".join(row) + " |")
    
    @staticmethod
    def print_board_nums():
        # 0 |  1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        moves = []
        return [i for i, spot in enumerate(self.board) if spot == " "]
            #the below code is the same but not list comprehension  
        # for (i,spot) in enumerate(self.board):
        #     #["x","x","o"] ---> [(0, "x")(1, "x")(2, "o")]
        #     if spot == " ":
        #         moves.append(i)
        #     return moves

    def empty_squares(self):
        return " " in self.board
    
    def num_empty_squares(self):
        return self.board.count(" ")
    
    def make_move(self,square, letter):
        #if valid move, then make the move (assign square to letter)
        # then return true. If invalid, return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner is 3 in a row anywhere.... we need to check all those

        #check row
        row_ind = square //3
        row = self.board[row_ind*3 : (row_ind +1) *3]
        if all(spot == letter for spot in row):
            return True
        
        #check column
        col_ind = square %3
        column =  [self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True
        
        #check diagonals
        # but only if the squares are an even number (0,2,4,6,8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #top left to bottom right diagonal win
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] #top right to bottom left diagonal win
            if all(spot == letter for spot in diagonal2):
                return True
            
        # if all these checks fail
        return False
    
def play(game, x_player, o_player, print_game = True):
    # returns the winner of the game! (the letter) or returns None for a tie
    if print_game:
        game.print_board_nums()

    letter = "x" #starting letter
    
    # iterate while the game has empty squares (we dont have to worry about winner because we'll just return that which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player 
        if letter == "o":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # lets define a function that lets player make a move

        if game.make_move(square, letter):
            if print_game:
                print(letter+ f" makes a move to square {square}")
                game.print_board()
                print("")


            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            # after we make our move, we need to alternate letters.
            letter = "o" if letter == "x" else "x" #switches players
            # the bottom code is the same as the code above
            # if letter == "x":
            #     letter = "o"
    
            # else:
            #     letter = "x"

        #making a tiny pause of 8 seconds to give us time to process the moves.
        time.sleep(0.8)
    if print_game:
        print("It's a tie!")

if __name__ == "__main__":
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer("o")
    t = TicTacToe()
    play(t,x_player, o_player, print_game=True)