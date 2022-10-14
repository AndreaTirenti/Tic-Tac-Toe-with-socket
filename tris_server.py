import socket       
import sys
from tris import Tris

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


print("TRIS")
print("Client is X and Server is O")

while 1:
    board = conn.recv(256)
    if board.decode() == "break":
        print("break\n")
        break
    print("\nServer make your move according this scheme:\n1 | 2 | 3\n--+---+--\n4 | 5 | 6\n--+---+--\n7 | 8 | 9\n")
    print(board.decode())
    move = input("Make your move-> ")
    conn.send(move.encode())
    
result = conn.recv(256)
print(result.decode())


conn.close()
my_sock.close()
