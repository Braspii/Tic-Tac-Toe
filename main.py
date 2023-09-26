from colorama import Fore, Style, init

init(autoreset=True)

PLAYER_X_COLOR = Fore.GREEN
PLAYER_O_COLOR = Fore.BLUE
DRAW_COLOR = Fore.YELLOW
HEADER_COLOR = Fore.CYAN + Style.BRIGHT

print(HEADER_COLOR + "TIC-TAC-TOE" + Style.RESET_ALL)

board = {

    1: 0, 2: 0, 3: 0,
    4: 0, 5: 0, 6: 0, 
    7: 0, 8: 0, 9: 0

}
turns = ["X", "O"] * 5
def main():
    while True:
        display_board(board)
        user_turn(turns[0])
        turns.pop(0)
        if type(is_solved(board)) == str:
            display_board(board)
            print(f"{is_solved(board)} won!")
            break
        if is_solved(board) == 0:
            
            print("Its a draw!")
            break

        
def display_board(board):
    board_copy = board.copy()
    for key in board_copy:
        if board_copy[key] == 0:
            board_copy[key] = ' '

    print(f" {board_copy[1]} | {board_copy[2]} | {board_copy[3]} ")
    print("---+---+---")
    print(f" {board_copy[4]} | {board_copy[5]} | {board_copy[6]} ")
    print("---+---+---")
    print(f" {board_copy[7]} | {board_copy[8]} | {board_copy[9]} ")

def user_turn(player):
    while True:
        try:
            move = int(input(f"{player}, Enter your move (1-9): "))
            if 1 <= move <= 9 and board[move] == 0:
                board[move] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number (1-9).")

def player_color(player):
    return PLAYER_X_COLOR if player == 'X' else PLAYER_O_COLOR

def board_color(cell):
    return PLAYER_X_COLOR if cell == 'X' else PLAYER_O_COLOR if cell == 'O' else cell

def is_solved(board):
    board = [[board[i] for i in range(1, 4)],[board[i] for i in range(4, 7)],[board[i] for i in range(7, 10)]]
    flat_rows = board
    flat_collumns = [ [board[i][x] for i in range(3)]for x in range(3)]
    flat_diagnol = [[board[i][i] for i in range(3)]] + [[board[::-1][i][i] for i in range(3)]]
    win_conditions = flat_rows + flat_collumns + flat_diagnol
    
    return next((condition[0] for condition in win_conditions if len(set(condition)) == 1 and condition[0] != 0), -1 if any(0 in row for row in board) else 0)

main()
