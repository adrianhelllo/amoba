def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end='  ')
        print()

def ask_input(w):
    r = int(input("In which row do you want to place your mark? : "))
    c = int(input("In which cell / column do you want to place your mark? : "))

    while c < 1 or c > w or r < 1 or r > w:
        print("Invalid input.")
        r = int(input("In which row do you want to place your mark? : "))
        c = int(input("In which cell / column do you want to place your mark? : "))

    return r, c

def is_game_over(board):
    for mark in ('X', 'O'):
        for i in range(len(board)):
            if all(cell in ('X', 'O') for row in board for cell in row):
                return True

            if all(cell == mark for cell in board[i]):
                return True
            
            if all(board[row][i] == mark for row in range(len(board))):
                return True
           
        if all(board[i][i] == mark for i in range(len(board))) or all(board[len(board) - 1 - i][len(board) - 1 - i] for i in range(len(board))):
            return True
        
    return False
        
            


def main():
    w = int(input("How wide should the board be? [width > 2]: "))
    while w < 3:
        print("Invalid input")
        w = int(input("How wide should the board be? [width > 2]: "))

    board = [['-' for _ in range(w)] for _ in range(w)]

    playing = True

    while playing:
        for mark in ('X', 'O'):
            print(f"{mark} is up next.")

            spot_marked = ask_input(w)
            board[spot_marked[0] - 1][spot_marked[1] - 1] = mark
            
            display_board(board)

            if is_game_over(board):
                print("Game over!")
                playing = False
                break



if __name__ == "__main__":
    main()