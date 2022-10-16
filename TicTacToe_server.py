import socket       
import sys
from TicTacToe import TicTacToe

host = "127.0.0.1"  
port = 5001

try:
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.bind((host, port))          
    my_sock.listen(1)                   
except Exception as err:
    print(err)
    sys.exit()

print("Server listening...")
conn, addr = my_sock.accept()
print ('Incoming connection from', addr)


board = {
        1 : "_", 2 : "_" , 3 : "_" ,
        4 : "_", 5 : "_" , 6 : "_" ,
        7 : "_", 8 : "_" , 9 : "_" ,
        }

PLAYER1 = "X"
PLAYER2 = "O"

tris = TicTacToe(PLAYER1, PLAYER2, board)

turn = 0

print("TRIS")
print("Client is O and Server is X")

while 1:
    if tris.Check_Win(board) != 0:
        conn.send("break".encode())
        break

    if turn % 2 == 0:
        print("Server make your move according this scheme:\n1 | 2 | 3\n--+---+--\n4 | 5 | 6\n--+---+--\n7 | 8 | 9\n")
        print(tris.Print_Board(board)) 
        tris.Player_Move(board, PLAYER1)
        if tris.Check_Win(board) != 0:
            conn.send("break".encode())
            break
        else:
            conn.send(tris.Print_Board(board).encode())
    else:
        move = conn.recv(256)
        if board[int(move.decode())] != "_":
            print("WRONG MOVE!")
            exit(0)
        board[int(move.decode())] = PLAYER2

    turn+=1
    
result = tris.Check_Win(board)
if result == 0:
    print(tris.Print_Board(board))
    print("DRAW!")
    conn.send("DRAW!".encode())
elif result == 10:
    print(tris.Print_Board(board))
    print("SERVER WINS!")
    conn.send("SERVER WINS!".encode())
elif result == -10:
    print(tris.Print_Board(board))
    print("CLIENT WINS!")
    conn.send("CLIENT WINS!".encode())
    


conn.close()
my_sock.close()
