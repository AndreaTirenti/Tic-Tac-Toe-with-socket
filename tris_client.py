import socket      
import sys
from tris import Tris

host = "127.0.0.1"
port = 5001



try:
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect((host, port))       
except Exception as err:
    print(err)
    sys.exit()
print("Connection established with success...")





board = {
        1 : "_", 2 : "_" , 3 : "_" ,
        4 : "_", 5 : "_" , 6 : "_" ,
        7 : "_", 8 : "_" , 9 : "_" ,
        }

PLAYER1 = "X"
PLAYER2 = "O"

tris = Tris(PLAYER1, PLAYER2, board)


print("TRIS")
print("Client is X and Server is O")

turn = 0

while 1:
    if tris.Check_Win(board) != 0:
        my_sock.send("break".encode())
        break

    if turn % 2 == 0:
        print("Client make your move according this scheme:\n1 | 2 | 3\n--+---+--\n4 | 5 | 6\n--+---+--\n7 | 8 | 9\n")
        print(tris.Print_Board(board)) 
        tris.Player_Move(board, PLAYER1)
        if tris.Check_Win(board) != 0:
            my_sock.send("break".encode())
            break
        else:
            my_sock.send(tris.Print_Board(board).encode())
    else:
        move = my_sock.recv(256)
        if board[int(move.decode())] != "_":
            print("WRONG MOVE!")
            exit(0)
        board[int(move.decode())] = PLAYER2

    turn+=1

result = tris.Check_Win(board)
if result == 0:
    print(tris.Print_Board(board))
    print("DRAW!")
    my_sock.send("DRAW!".encode())
elif result == 10:
    print(tris.Print_Board(board))
    print("CLIENT WINS!")
    my_sock.send("CLIENT WINS!".encode())
elif result == -10:
    print(tris.Print_Board(board))
    print("SERVER WINS!")
    my_sock.send("SERVER WINS!".encode())


my_sock.close()
