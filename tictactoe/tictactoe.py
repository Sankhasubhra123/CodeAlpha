import math
import sys

# The board is a list of 9 strings
board = [' ' for _ in range(9)]

def print_board():
    """Prints the current state of the board"""
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")
    print("\n")

def is_winner(b, player):
    """Checks if the specific player has won"""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Cols
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    return any(b[x] == b[y] == b[z] == player for x, y, z in win_conditions)

def is_draw(b):
    """Checks if the board is full"""
    return ' ' not in b

def minimax(b, depth, is_maximizing):
    """The AI brain: Recursive function to find the best move"""
    if is_winner(b, 'O'): return 1
    if is_winner(b, 'X'): return -1
    if is_draw(b): return 0
    
    if is_maximizing: # AI's turn (O)
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else: # Human's turn (X)
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def computer_move():
    """Calculates and plays the best move for AI"""
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'
    print(f"AI chose position {move + 1}")

# --- Main Game Loop ---
def play_game():
    print("="*40)
    print("   Unbeatable Tic-Tac-Toe AI")
    print("   You are 'X' | AI is 'O'")
    print("   Enter positions 1-9 to play.")
    print("="*40)
    
    print_board()

    while True:
        # 1. Player Move
        try:
            choice = input("Enter position (1-9): ")
            if choice.lower() == 'exit': break
            
            pos = int(choice) - 1
            if pos < 0 or pos > 8 or board[pos] != ' ':
                print("Invalid move! Try again.")
                continue
            
            board[pos] = 'X'
            
        except ValueError:
            print("Please enter a valid number.")
            continue

        print_board()

        # Check Player Win
        if is_winner(board, 'X'):
            print("You won! (This is rare!)")
            break
        if is_draw(board):
            print("It's a Draw!")
            break

        # 2. AI Move
        print("AI is thinking...")
        computer_move()
        print_board()

        # Check AI Win
        if is_winner(board, 'O'):
            print("AI Wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a Draw!")
            break

if __name__ == "__main__":
    play_game()