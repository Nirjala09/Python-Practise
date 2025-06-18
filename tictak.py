class TicTacToe:
    
        # Initialize an empty 3x3 board
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def display_board(self):
        print()
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("__|__|__")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("__|__|__")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print()

    def make_move(self, position):
        # If the position is empty, make the move
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        # All winning combinations
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)             
        ]

        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return True
        return False

    def is_draw(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.display_board()

        while True:
            try:
                move = int(input(f"Player {self.current_player}, enter position (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid position. Try again.")
                    continue

                if not self.make_move(move):
                    print("That spot is already taken. Try again.")
                    continue

                self.display_board()

                if self.check_winner():
                    print(f"Player {self.current_player} wins!")
                    break

                if self.is_draw():
                    print("It's a draw!")
                    break

                self.switch_player()

            except ValueError:
                print("Invalid input. Please enter a number from 1 to 9.")

# Run the game
game = TicTacToe()
game.play()
