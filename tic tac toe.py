board=["-","-","-",
       "-","-","-",
       "-","-","-"]
def print_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])
def print_turn(player):
    print(player+"'s turn")
    position=input("enter position from 1-9:")
    while position not in ["1","2","3","4","5","6","7","8","9"]:
        print("invalid choice(1-9)")
    position=int(position)-1
    while board[position] != "-":
        position=int(input("position already taken :"))
    board[position]=player
    print_board()
def check_game_over():
    if (board[0] == board[1] == board[2] !="-") or \
    (board[3] == board[4] == board[5] !="-") or \
    (board[6] == board[7] == board[8] !="-") or \
    (board[0] == board[3] == board[6] != "-") or \
	(board[1] == board[4] == board[7] != "-") or \
	(board[2] == board[5] == board[8] != "-") or \
	(board[0] == board[4] == board[8] != "-") or \
	(board[2] == board[4] == board[6] != "-"):
        return "win"
    elif "-" not in board:
        return "tie"
    else:
        return "play"
def play_game():
    print_board()
    current_player="X"
    game_over = False
    while not game_over:
        print_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"
play_game()