class Tris():
    def __init__(self, player1, player2, board):
        self.board = board
        self.PLAYER1_SIGN = player1
        self.PLAYER2_SIGN = player2


    def Print_Board(self, board):
        return f"{board[1]} | {board[2]} | {board[3]}\n--+---+--\n{board[4]} | {board[5]} | {board[6]}\n--+---+--\n{board[7]} | {board[8]} | {board[9]}\n"

    def Player_Move(self, board, player):
        move = int(input("> "))
        if board[move] != "_":
            print("WRONG MOVE!")
            exit(0)
        board[move] = player

    def Check_Win(self, board): 
        win_case=[[1,2,3] , [4,5,6] , [7,8,9] , [1,4,7] , [2,5,8] , [3,6,9] , [1,5,9] , [3,5,7]]
        for i in range(0,8):
            if(board[win_case[i][0]] != "_" and board[win_case[i][0]] == board[win_case[i][1]] and board[win_case[i][0]] == board[win_case[i][2]]):
                if board[win_case[i][0]] == "X":              
                    return 10
                else:
                    return -10    
        return 0