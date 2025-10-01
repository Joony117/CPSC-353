#import socket module
import socket
import sys # In order to terminate the program

FILENAME = "helloworld.html"

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server = socket.gethostbyname("localhost")
except socket.gaierror:
    print("Failed to resolve host name")
    sys.exit()

clientSocket.connect((server,6789))
request = "GET /"+FILENAME+" HTTP/1.1\r\nHost: localhost\r\n\r\n"
clientSocket.send(request.encode())
responce = clientSocket.recv(1024).decode()

print(responce)

clientSocket.close()
