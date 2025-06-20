def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end='  ')
        print()

def ask_input(w, board):
    r = int(input("In which row do you want to place your mark? : "))
    c = int(input("In which cell / column do you want to place your mark? : "))

    while c < 1 or c > w or r < 1 or r > w or board[r - 1][c - 1] != '-':
        print("Invalid input.")
        r = int(input("In which row do you want to place your mark? : "))
        c = int(input("In which cell / column do you want to place your mark? : "))

    return r, c

def is_game_over(board):
    w = len(board)
    for mark in ('X', 'O'):
        for i in range(w):
            if all(cell in ('X', 'O') for row in board for cell in row):
                return True

            if all(cell == mark for cell in board[i]):
                return True
            
            if all(board[row][i] == mark for row in range(w)):
                return True
            
        if all(board[i][i] == mark for i in range(w)) or all(board[i][w - 1 - i] == mark for i in range(w)):
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

            spot_marked = ask_input(w, board)
            board[spot_marked[0] - 1][spot_marked[1] - 1] = mark
            
            display_board(board)

            if is_game_over(board):
                print(f"Game over, ", end=" ")
                if all(cell in ('X', 'O') for row in board for cell in row):
                    print("it's a tie!")
                else:
                    print(f"{mark} wins!")
                playing = False
                break



if __name__ == "__main__":
    main()

