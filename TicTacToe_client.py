import socket      
import sys

host = "127.0.0.1"
port = 5001


try:
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect((host, port))       
except Exception as err:
    print(err)
    sys.exit()
print("Connection established with success...")




print("TRIS")
print("Client is O and Server is X")


while 1:
    board = my_sock.recv(256)
    if board.decode() == "break":
        print("break\n")
        break
    print("\nClient make your move according this scheme:\n1 | 2 | 3\n--+---+--\n4 | 5 | 6\n--+---+--\n7 | 8 | 9\n")
    print(board.decode())
    move = input("Make your move-> ")
    my_sock.send(move.encode())


result = my_sock.recv(256)
print(result.decode())

my_sock.close()
